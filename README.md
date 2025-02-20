# Desafio prático para Cognitiva Brasil  

Este projeto compara as respostas geradas por diferentes Modelos de Linguagem de Grande Escala (LLMs) ao responderem a uma mesma pergunta. A avaliação das respostas é assistida por IA.  

## Modelos Utilizados:
-- *Mistral (via `mistralai`)*  
-- *Gemini (via `google-generativeai`)*  
-- *DeepSeek (via `ollama`)*  

## Requisitos:
-- Python 3.12.8+  
-- Ambiente virtual  
-- Dependências necessárias instaladas  
-- acesso as API's  

## Instalação:
**1. Clone esse repositório**  
```bash
git clone https://github.com/CaioCasemiro/desafio-Cognitiva-Brasil.git
cd desafio-Cognitiva-Brasil
```

**2. Instale as dependências necessárias**  
```bash
pip instal -r requirements.txt
```

**3. Crie e ative o ambiente virtual**   
```bash
python -m venv venv
.\venv\Scripts\activate
```

**4. Configure as variáveis de ambiente**  
Crie um arquivo .env na raiz do projeto e adicione as chaves de API dos serviços utilizados. O arquivo deve seguir o seguinte formato:
```bash
GEMINI_API_KEY=sua_chave_api
MISTRAL_API_KEY=sua_chave_api
```
OBS.: Substitua "sua_chave_api" por suas chaves API reais  

### *LINKS para pegar API Keys:*  
*Mistral*  
```bash
https://console.mistral.ai/api-keys/
```
*Gemini*  
```bash
https://aistudio.google.com/app/apikey
```

**5. Instale o ollama**  
Para acessar o DeepSeek você precisará instalar o Ollama no site:    
```bash
https://ollama.com/
```  
Após a instalação do Ollama, execute o seguinte comando para instalar o modelo do DeepSeek  
```bash
ollama run deepseek-r1:1.5b
```

## Execução:  
Utilize o seguinte comando para execução do código:  
```bash
python main.py
```

## Estrutura do projeto:  
As pastas e arquivos devem está estruturados da seguinte forma:  
```bash
├── models
│   ├── deepseek.py
│   ├── gemini.py
│   └── mistral.py
├── service
│   └── comparador.py
├── .env
├── main.py
└── requirements.txt
```

## Contribuições  
Contribuições são bem-vindas! Se você encontrar bugs ou quiser melhorar o projeto, sinta-se à vontade para enviar um pull request.
