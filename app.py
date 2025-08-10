from question_validator import question_validator  

import os
from dotenv import load_dotenv
load_dotenv()  

print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("PINECONE_API_KEY:", os.getenv("PINECONE_API_KEY"))

import streamlit as st
from your_rag_code import augmented_query, ask_gpt, primer  

st.set_page_config(page_title="WWII RAG QA Assistant", layout="centered")
st.title("🪖 Welcome to Historic")
st.markdown("Ask any question related to World War II and I will assist you in the best possible way.")

user_question = st.text_area("Type your WWII-related question:", height=120)

if st.button("Ask") and user_question.strip():
    is_valid, error_msg = question_validator(user_question)  
    
    if not is_valid:
        st.warning(error_msg)
    else:
        with st.spinner("Thinking..."):
            full_prompt = augmented_query(user_question)
            answer = ask_gpt(system_prompt=primer, user_prompt=full_prompt)
        st.success("Done!")
        st.markdown("### ✅ Answer")
        st.markdown(answer)