import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def acessar_gemini(pergunta):
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model=genai.GenerativeModel("gemini-1.5-flash")
        resposta = model.generate_content(pergunta)
        return resposta.text
    except Exception as e:
        return print(f"Erro ao acessar o Gemini: {str(e)}")