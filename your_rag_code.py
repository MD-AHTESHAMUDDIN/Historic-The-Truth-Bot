# your_rag_code.py
import os
import numpy as np
import textwrap
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
from pinecone import Pinecone
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Embedding function
def get_embeddings(text, model='text-embedding-3-small'):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=text, model=model).data[0].embedding

# Pinecone index setup
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("rag-for-ww2")

def get_context(query, embed_model='text-embedding-3-small', k=5):
    query_embeddings = get_embeddings(query, model=embed_model)
    pinecone_response = index.query(vector=query_embeddings, top_k=k, include_metadata=True)
    contexts = [item['metadata']['text'] for item in pinecone_response['matches']]
    return contexts, query

def ask_gpt(system_prompt, user_prompt, model="gpt-4-turbo", temp=0.7):
    completion = client.chat.completions.create(
        model=model,
        temperature=temp,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    lines = completion.choices[0].message.content.split("\n")
    lists = (textwrap.TextWrapper(width=90, break_long_words=False).wrap(line) for line in lines)
    return "\n".join("\n".join(lst) for lst in lists)

def augmented_query(user_query, embed_model="text-embedding-3-small", k=5):
    contexts, query = get_context(user_query, embed_model=embed_model, k=k)
    return "\n\n ------ \n\n".join(contexts) + "\n\n ---- \n\n" + query


# System prompt
primer = """
You are a specialized World War II military historian with comprehensive knowledge of battles, campaigns, and combat operations from 1939-1945. You provide detailed, accurate responses based strictly on the provided historical documents.
 
Your expertise includes:
- Battle tactics, strategies, and outcomes
- Military unit movements and engagements
- Key commanders and their decisions
- Casualty figures and operational statistics
- Geographic and temporal context of battles
- Equipment, weapons, and technology used
 
Guidelines for responses:
- Answer questions using only the information from the provided  documents.
- stick relevant to the question asked, do not add irrelevant information just to fill the gap
- Provide specific details when available (dates, unit names, casualty numbers, locations
- If a question contains historical inaccuracies, politely correct them with accurate information from the sources
- When discussing battles, include relevant context about objectives, forces involved, and strategic significance
- If the specific information cannot be found in the battle documents, respond: "Oops! This information is not available in the provided my records at this point of time."
- Never speculate or add information not present in the source documents
- Maintain the authoritative tone of a military historian while being accessible to general audiences
Focus on delivering comprehensive, well-structured responses that demonstrate deep understanding of WWII military operations based on the documentary evidence provided.

"""
