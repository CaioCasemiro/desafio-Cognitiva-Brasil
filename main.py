from models.gemini import acessar_gemini
from models.deepseek import acessar_deepseek
from models.mistral import acessar_mistral
from service.comparador import comparar_respostas
.
def main():
    pergunta = "De forma resumida, em português, qual é a importância da inteligência artificial na sociedade moderna?"
    
    respostas = {
        "Mistral": acessar_mistral(pergunta),
        "Gemini": acessar_gemini(pergunta),
        "DeepSeek": acessar_deepseek(pergunta)
    }
    
    print("\n--- Respostas obtidas ---\n")
    for modelo, resposta in respostas.items():
        print(f"{modelo}:\n{resposta}\n")
    
    print("\n--- Avaliação comparativa ---\n")
    avaliacao = comparar_respostas(respostas)
    print(avaliacao)

if __name__ == "__main__":
    main()
