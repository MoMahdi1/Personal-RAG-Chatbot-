import streamlit as st
import os
from modules import loader
from modules import llm
from modules import prompt

st.set_page_config(
    page_title="Personal RAG Chatbot",
    layout="wide",
    page_icon="🤖"
)

# ---------------- Session State ---------------- #

if "all_docs" not in st.session_state:
    st.session_state.all_docs = []


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
# ---------------- Header ---------------- #

st.markdown(
    """
    <h1 style='text-align:center;color:#7C5CFF;'>
        🤖 Personal RAG Chatbot
    </h1>
    <p style='text-align:center;color:gray;font-size:18px;'>
        Chat with your own documents using RAG
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("")

# ---------------- Layout ---------------- #

col1, col2 = st.columns([1, 3], gap="large")

# ================= LEFT PANEL ================= #

with col1:

    with st.container(border=True):

        st.subheader("📂 Upload Documents")

        files = st.file_uploader(
            "Choose your files",
            accept_multiple_files=True,
            type=["pdf", "txt", "docx"]
        )

        st.write("")

        col_1, col_2 = st.columns(2)

        with col_1:
            loadbutton = st.button(
                "📥 Load",
                use_container_width=True
            )

        with col_2:
            clearbutton = st.button(
                "🗑️ Clear",
                use_container_width=True
            )

    st.write("")

    if files:
        with st.container(border=True):

            st.subheader("📄 Uploaded Files")

            for f in files:
                st.success(f.name)

    if clearbutton:
        st.session_state.all_docs = []
        st.rerun()

    if loadbutton and files:

        os.makedirs("temp", exist_ok=True)

        # مسح البيانات القديمة
        st.session_state.all_docs = []

        for uploaded_file in files:

            temp_path = os.path.join("temp", uploaded_file.name)

            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            docs = loader.load_document(temp_path)
            chunks = loader.split_documents(docs)

            st.session_state.all_docs.extend(chunks)

            # حذف الملف المؤقت
            os.remove(temp_path)

        # إنشاء موديل الـ Embeddings
        embeddings_model = loader.embedding_documents()

        # إنشاء FAISS
        vector_db = loader.create_vectorstore(
            st.session_state.all_docs,
            embeddings_model
        )

        # حفظ قاعدة البيانات
        loader.save_vectorstore(vector_db)

        st.success(
            f"✅ Loaded {len(st.session_state.all_docs)} chunks successfully!"
        )

        st.success("✅ FAISS Vector Database Saved Successfully!")

# ================= RIGHT PANEL ================= #

# ================= RIGHT PANEL ================= #

with col2:

    st.subheader("🤖 How Can I Help?")

    
    for chat in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(chat["question"])
        with st.chat_message("assistant"):
            st.write(chat["answer"])

    question = st.chat_input("Ask a question about your documents...")

    if question:

        # تحميل موديل الـ Embeddings
        embedding_model = loader.embedding_documents()

        # تحميل قاعدة بيانات FAISS
        vector_db = loader.load_vectorstore(embedding_model)

        # البحث عن أكثر 3 أجزاء تشابهًا
        retriever = vector_db.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 5}
        )
        results = retriever.invoke(question)

        # إنشاء الـ Context
        context = "\n\n".join(
            [doc.page_content for doc in results]
        )
        
        history =""

        for chat in st.session_state.chat_history[-10:]:
          history +=(
            f"User: {chat['question']}\n"
            f"Assistant: {chat['answer']}\n\n"
             )

        # إنشاء الـ Prompt
        final_prompt = prompt.build_prompt(
            context=context,
            history=history,
            question=question
        )
        
        response, model_used = llm.invoke_with_fallback(final_prompt)
        st.caption(f"Model used: {model_used}")
        
        st.session_state.chat_history.append({
            "question": question,
            "answer": response.content
        })

        # عرض السؤال
        st.subheader("❓ Question")
        st.write(question)

        # عرض الإجابة
        st.subheader("🤖 Answer")
        st.write(response.content)
      