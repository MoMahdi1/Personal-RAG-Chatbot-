from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv  
import os


load_dotenv()  # Load environment variables from .env file
api_key_gemini = os.getenv("Google_API_Key")
api_key_groq = os.getenv("Groq_API_Key")


def get_gemini():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        api_key=api_key_gemini
    )
    
    
def get_groq():
    return ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0,
        api_key=api_key_groq
    )
    
    
    
def invoke_with_fallback(prompt):
    try:
        llm = get_gemini()
        response = llm.invoke(prompt)
        return response, "Gemini"
    
    except Exception :
        llm = get_groq()
        response = llm.invoke(prompt)
        return response, "Groq"