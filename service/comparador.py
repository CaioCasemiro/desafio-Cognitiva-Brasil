from models.gemini import acessar_gemini
.
def comparar_respostas(respostas):
    criterios = (
        "clareza, coerência, precisão da informação, criatividade e gramática. "
        "Avalie cada uma e ranqueie da melhor para a pior."
    )
    prompt = (
        "Aqui estão três respostas geradas por diferentes modelos de linguagem. "
        "Por favor, compare-as com base nos seguintes critérios: " + criterios + "\n\n"
    )
    
    for modelo, resposta in respostas.items():
        prompt += f"{modelo}:\n{resposta}\n\n"
    
    prompt += "Dê um ranking final e justifique sua escolha."
    
    avaliacao = acessar_gemini(prompt)
    return avaliacao
