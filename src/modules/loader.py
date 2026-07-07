import os 
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


def load_document(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
    elif ext == ".txt":
        loader = TextLoader(file_path , encoding="utf-8")
    elif ext == ".docx":
        loader = Docx2txtLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
    
    docs = loader.load()

    return docs

def split_documents(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    
    chunks = text_splitter.split_documents(docs)
    
    return chunks

def embedding_documents():
    embeddings = HuggingFaceEmbeddings(
        model_name = "intfloat/multilingual-e5-small",
        
    )
    
    return embeddings


def create_vectorstore(chunks, embeddings):
    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )
    return vectorstore

def save_vectorstore(vector_db):
    vector_db.save_local("faiss_index")
    

def load_vectorstore(embeddings):
    vector_db = FAISS.load_local("faiss_index",
                                 embeddings,
                                 allow_dangerous_deserialization=True
    )
    return vector_db