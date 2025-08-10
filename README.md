# Historic-The-Truth-Bot
Created a RAG Pipeline using Open AI models and Pinecone for World War II related Specific use case

A **Retrieval-Augmented Generation (RAG)** system built with **Streamlit**, **OpenAI**, and **Pinecone**, designed to answer detailed questions about **World War II** based strictly on provided historical documents.  
The system includes **input guardrails** to prevent prompt injection and **output guardrails** to ensure historically accurate responses.

---

## 📜 Project Overview

This project enables users to:
- Ask **WWII-related** questions in natural language.
- Retrieve **relevant historical context** from a Pinecone vector database.
- Generate accurate, context-based answers using **OpenAI GPT models**.
- Automatically correct **historical inaccuracies** in user queries.
- Handle both **technical and non-technical** audiences with clear explanations.

---

## 🏗 Features

- **RAG Pipeline**: Combines semantic search from Pinecone with OpenAI GPT for context-aware answers.
- **Guardrails**:
  - **Input Guardrail** — Validates and filters user queries before embedding.
  - **Output Guardrail** — Enforces historian-style factual responses from the system prompt.
- **Historical Accuracy**: Answers only from trusted WWII documents, avoiding hallucinations.
- **Polite Corrections**: Detects and corrects historical inaccuracies in user queries.
- **Evaluation with RAGAS**: Measures answer relevancy, faithfulness, and context quality.
- **Streamlit Interface**: Simple, interactive UI for Q&A.

---

## 📂 Project Structure

Historic/
│
├── app.py # Main Streamlit app
├── your_rag_code.py # RAG pipeline functions (retrieval + generation)
├── question_validator.py # Input guardrail to validate queries
├── .env # Environment variables (API keys)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── data/ # Historical WWII context documents


---

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/WWII-RAG-QA](https://github.com/MD-AHTESHAMUDDIN/Historic-The-Truth-Bot.git
   cd Historic-The-Truth-Bot
2. python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
3. pip install -r requirements.txt
4. OPENAI_API_KEY=your_openai_key_here
PINECONE_API_KEY=your_pinecone_key_here
5. streamlit run app.py

