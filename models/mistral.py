import os
from mistralai import Mistral
from dotenv import load_dotenv
.
load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

def acessar_mistral(pergunta):
    try:
        model = "mistral-small"
        cliente = Mistral(api_key=MISTRAL_API_KEY)
        resposta = cliente.chat.complete(
            model=model,
            messages= [
                {
                    "role": "user",
                    "content": pergunta,
                },
            ]
        )
        return resposta.choices[0].message.content
    except Exception as e:
        return print(f"Erro ao acessar o Mistral: {str(e)}")