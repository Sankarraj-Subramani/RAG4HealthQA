from app.embedding_config import get_embedding_model
from app.utils import load_documents
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_retriever():
    docs = load_documents("data")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = splitter.split_documents(docs)
    embed_model = get_embedding_model()

    # ✅ Use FAISS instead of Chroma
    vector_db = FAISS.from_documents(splits, embed_model)
    return vector_db.as_retriever()
