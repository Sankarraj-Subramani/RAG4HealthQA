import streamlit as st
from app.rag_pipeline import get_answer

st.set_page_config(page_title="RAG4HealthQA", layout="wide")
st.title("🩺 RAG4HealthQA - Healthcare QA Assistant")

query = st.text_input("Ask a health-related question:")

if query:
    with st.spinner("Thinking..."):
        response = get_answer(query)
        st.success("Answer:")
        st.write(response)
