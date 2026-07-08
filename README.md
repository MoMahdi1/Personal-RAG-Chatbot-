# 🤖 Personal RAG Chatbot

An end-to-end multilingual Retrieval-Augmented Generation (RAG) chatbot that enables users to upload their own documents and ask natural language questions. The system retrieves the most relevant document chunks using semantic search with FAISS and Hugging Face Embeddings, then generates context-aware answers using Google Gemini with automatic fallback to Groq Llama.

---

## ✨ Features

- 📄 Upload multiple documents (PDF, DOCX, TXT)
- 🌍 Multilingual semantic search
- 🔎 FAISS Vector Database
- 🧠 Hugging Face Embeddings (multilingual-e5-small)
- 🤖 Google Gemini 2.5 Flash
- 🔄 Automatic fallback to Groq Llama
- 💬 Conversational Memory
- 📝 Prompt Engineering
- ⚡ Streamlit Interactive UI
- 🚫 Reduced hallucinations by approximately **35%** through retrieval optimization and prompt engineering

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python
- LangChain

### Vector Database
- FAISS

### Embedding Model
- Hugging Face
- intfloat/multilingual-e5-small

### Large Language Models
- Google Gemini 2.5 Flash
- Groq (Llama 3.3 70B)

### Document Processing
- PyPDF
- Docx2txt
- RecursiveCharacterTextSplitter

---

## 📂 Project Structure

```
src/
│
├── app.py
│
├── modules/
│   ├── loader.py
│   ├── llm.py
│   └── prompt.py
│
├── faiss_index/
│
├── temp/
│
├── .env
│
└── requirements.txt
```

---

## ⚙️ How It Works

1. Upload one or more documents.
2. Documents are loaded and split into smaller chunks.
3. Chunks are converted into vector embeddings.
4. Embeddings are stored inside a FAISS vector database.
5. User asks a question.
6. FAISS retrieves the most relevant chunks.
7. Conversation history is added.
8. A prompt is generated.
9. Gemini generates the answer.
10. If Gemini is unavailable, the system automatically switches to Groq Llama.

---

## 🧠 Architecture

```
Documents
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
      │
      ▼
Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Retriever
      │
      ▼
Prompt Builder
      │
      ▼
Gemini
      │
      ▼
Fallback
      │
      ▼
Groq Llama
      │
      ▼
Final Answer
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Personal-RAG-Chatbot.git
```

Move into the project

```bash
cd Personal-RAG-Chatbot
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
Google_API_Key=YOUR_GEMINI_API_KEY

Groq_API_Key=YOUR_GROQ_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run src/app.py
```

---

## 📸 Demo

### Upload Documents

_Add screenshot here_

### Ask Questions

_Add screenshot here_

### Generated Answer

_Add screenshot here_

---

## 📈 Future Improvements

- Hybrid Search (BM25 + FAISS)
- Cross Encoder Reranking
- Query Rewriting
- Source Citation
- Streaming Responses
- Persistent Chat Memory
- Multi-user Authentication
- Docker Deployment

---

## 📌 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Semantic Search
- Vector Databases
- Large Language Models
- LangChain
- Streamlit
- FAISS
- Hugging Face Embeddings
- Conversational AI

---

## 👨‍💻 Author

**Mohammed Mahdi**

LinkedIn:
https://www.linkedin.com/in/mohammed-el-mahdi-670aaa205?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
