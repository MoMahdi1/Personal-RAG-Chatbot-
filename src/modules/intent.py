import re

GREETINGS = [
    "hi",
    "Hi",
    "Hello",
    "ازيك",
    "أزيك",
    "hello",
    "hey",
    "السلام",
    "السلام عليكم",
    "اهلا",
    "أهلا",
    "مرحبا",
    "صباح الخير",
    "مساء الخير",
]

def is_greeting(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)

    return any(word in text for word in GREETINGS)


def greeting_response():
    return (
        "👋 أهلاً بيك!\n\n"
        " Personal RAG Chatbot أنا.\n\n"
        "ارفع ملفاتك واسألني أي سؤال عنها، وأنا هساعدك\n\n"
    )