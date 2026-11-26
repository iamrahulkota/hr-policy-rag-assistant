"""Step 4: Store the embeddings in FAISS so we can search them later."""


import os
from langchain_community.vectorstores import FAISS

from hr_assistant import config
from hr_assistant.embeddings import get_embeddings_model


# build the vector stor using the FAISS library
def build_vector_store(chunks):
    """
        Build a FAISS vector store from the document chunks.
    """
    embeddings_model = get_embeddings_model()
    vector_store = FAISS.from_documents(chunks, embeddings_model)

    return vector_store


# save the vector store to disk for later use
def save_vector_store(vector_store, path: str = config.VECTOR_STORE_PATH) -> None:
    """
        Save the FAISS vector store to disk for later use.
    """
    vector_store.save_local(path)


# load the vector_store
def load_vector_store(path: str = config.VECTOR_STORE_PATH) -> FAISS:
    """
        Load the FAISS vector store from disk.
    """
    embeddings_model = get_embeddings_model()
    
    vector_store = FAISS.load_local(path, embeddings_model, allow_dangerous_deserialization=True)
    return vector_store


# check if the vector store exists
def vector_store_exists(path: str = config.VECTOR_STORE_PATH) -> bool:
    """
        Check if the FAISS vector store exists on disk.
    """
    return os.path.exists(path)


# get retriever
def get_retriever(vector_store: FAISS, k: int = config.TOP_K_RESULTS):
    """
        Turn a vector store into a retriever
    """
    retriever = vector_store.as_retriever(search_kwargs={"k": k})

    return retriever

