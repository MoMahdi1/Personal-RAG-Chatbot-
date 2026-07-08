# 🤖 Personal RAG Chatbot

A multilingual Retrieval-Augmented Generation (RAG) chatbot that allows users to upload their own documents and ask questions in natural language. The application retrieves the most relevant document chunks using FAISS semantic search and generates context-aware answers using Google Gemini with automatic fallback to Groq.

---

## ✨ Features

- Upload multiple document formats:
  - PDF
  - DOCX
  - TXT
- Automatic document loading
- Recursive text chunking
- Semantic search using FAISS
- Hugging Face multilingual embeddings
- Conversational memory
- Prompt engineering for grounded responses
- Google Gemini integration
- Automatic fallback to Groq when Gemini is unavailable
- Interactive Streamlit interface

---

## 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Hugging Face Embeddings
- Google Gemini
- Groq
- PyPDF
- Docx2txt

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
├── requirements.txt
└── .env
```

---

## ⚙️ Workflow

```
Upload Documents
        │
        ▼
Document Loader
        │
        ▼
Text Splitter
        │
        ▼
Hugging Face Embeddings
        │
        ▼
FAISS Vector Store
        │
        ▼
Similarity Search
        │
        ▼
Conversation History
        │
        ▼
Prompt Builder
        │
        ▼
Gemini
   │
   └──────────────► Groq (Fallback)
        │
        ▼
Final Answer
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YourUsername/Personal-RAG-Chatbot.git
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

## ▶️ Run

```bash
streamlit run src/app.py
```

---

## 💬 How It Works

1. Upload one or more documents.
2. Documents are loaded and split into chunks.
3. Chunks are converted into embeddings.
4. Embeddings are stored inside a FAISS vector database.
5. The user asks a question.
6. FAISS retrieves the most relevant chunks.
7. Conversation history is added to the prompt.
8. The prompt is sent to Gemini.
9. If Gemini is unavailable, the application automatically switches to Groq.
10. The generated answer is displayed in the chat interface.

---

## 📌 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Semantic Search
- Vector Databases
- Conversational AI
- LangChain
- FAISS
- Hugging Face Embeddings
- Streamlit

---

## 👨‍💻 Author

**Mohammed Mahdi**

- LinkedIn: [https://linkedin.com/in/your-profile](https://www.linkedin.com/in/mohammed-el-mahdi-670aaa205?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
