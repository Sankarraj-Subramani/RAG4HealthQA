from langchain.document_loaders import TextLoader
import os

def load_documents(directory):
    loaders = []
    for file in os.listdir(directory):
        if file.endswith(('.txt', '.md')):
            loaders.append(TextLoader(os.path.join(directory, file)))
    docs = []
    for loader in loaders:
        docs.extend(loader.load())
    return docs
