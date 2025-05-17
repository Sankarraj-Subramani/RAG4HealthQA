import os
from dotenv import load_dotenv
from langchain_community.embeddings import CohereEmbeddings

load_dotenv()

def get_embedding_model():
    cohere_api_key = os.getenv("COHERE_API_KEY")
    if not cohere_api_key:
        raise EnvironmentError("Cohere API key is missing. Add COHERE_API_KEY to your .env file.")

    return CohereEmbeddings(
        model="embed-english-v3.0",
        cohere_api_key=cohere_api_key,
        user_agent="rag4healthqa/1.0"  # ✅ FIX HERE
    )
