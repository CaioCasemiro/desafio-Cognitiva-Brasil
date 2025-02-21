import ollama
.
def acessar_deepseek(pergunta):
    try:
        resposta = ollama.chat(
            model="deepseek-r1:1.5b",
            messages=[
                {"role": "system", "content": "Responda em português, sem o marcador <think>."},
                {"role": "user", "content": pergunta}
            ])
        return resposta["message"]["content"]
    except Exception as e:
        return print(f"Erro ao acessar o deepseek: {str(e)}")