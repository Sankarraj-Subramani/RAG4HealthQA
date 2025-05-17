import os
from dotenv import load_dotenv
from langchain.llms import Cohere
from langchain.chains import RetrievalQA
from app.vector_store import get_retriever

# Load API keys from .env
load_dotenv()

def get_answer(question: str) -> str:
    cohere_api_key = os.getenv("COHERE_API_KEY")
    if not cohere_api_key:
        raise EnvironmentError("Cohere API key is missing. Add COHERE_API_KEY to your .env file.")

    retriever = get_retriever()
    llm = Cohere(model="command", cohere_api_key=cohere_api_key)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain.run(question)
