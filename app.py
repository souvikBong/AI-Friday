from dotenv import load_dotenv
load_dotenv()



import streamlit as st
from core.llm_client import LLMClient
from core.rag_engine import RAGEngine

st.set_page_config(page_title="AI-Friday", layout="wide")
st.title("AI-Friday AI System")

mode = st.sidebar.selectbox("Select Mode", ["Chat", "Predict", "Explain", "RAG"])

llm = LLMClient()
rag = RAGEngine()

if mode == "Chat":
    user_input = st.text_input("Ask something:")
    if st.button("Send"):
        response = llm.ask(user_input)
        st.write(response)

elif mode == "RAG":
    query = st.text_input("Ask from knowledge base:")
    if st.button("Search"):
        answer = rag.ask(query, llm)
        st.write(answer)
