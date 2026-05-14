# 🤖 Prompt Toolkit — CP02

Projeto desenvolvido para o Checkpoint 02 da disciplina  
**Prompt Engineering & Artificial Intelligence — FIAP**

---

## 📚 Objetivo

Este projeto implementa um toolkit em Python capaz de comparar diferentes técnicas de prompting aplicadas a tarefas de negócio utilizando Large Language Models (LLMs).

O sistema automatiza:
- geração de prompts
- execução via Ollama Cloud
- avaliação de respostas
- análise de custo e desempenho
- geração de gráficos comparativos

---

## 🧠 Técnicas de Prompting

O projeto compara 4 estratégias:

* Zero-Shot Prompting
* Few-Shot Prompting
* Chain-of-Thought Prompting
* Role Prompting

---

## 📌 Tarefas Avaliadas

As técnicas foram aplicadas em:

* Classificação de Sentimento
* Extração de Dados
* Sumarização de Texto

---

## 🚀 Tecnologias Utilizadas

* Python 3
* Ollama Cloud API
* Modelo `gpt-oss:120b`
* pandas
* matplotlib
* tiktoken
* python-dotenv
* Git & GitHub

---

## 📁 Estrutura do Projeto

```text
prompt_toolkit/
│
├── main.py
├── requirements.txt
├── README.md
├── .env.example
│
├── src/
│   ├── llm_client.py
│   ├── prompt_builder.py
│   ├── evaluator.py
│   ├── report.py
│   ├── tasks.py
│   └── techniques.py
│
├── prompts/
│
├── data/
│
└── output/

⚙️ Configuração

Crie um arquivo .env na raiz do projeto:

OLLAMA_API_KEY=sua_chave_aqui
OLLAMA_HOST=https://ollama.com
MODEL_NAME=gpt-oss:120b
TIMEOUT=120

⚠️ O arquivo .env não deve ser enviado ao GitHub.

▶️ Como executar

1️⃣ Criar ambiente virtual
python -m venv venv

2️⃣ Ativar ambiente virtual

Windows PowerShell
.\venv\Scripts\Activate.ps1

Linux / MacOS
source venv/bin/activate

3️⃣ Instalar dependências

pip install -r requirements.txt


4️⃣ Executar projeto
python main.py

📊 Métricas Avaliadas

O sistema mede automaticamente:

Acurácia
Tokens utilizados
Tempo de resposta
Consistência
Custo médio por técnica
📈 Resultados Gerados

Após a execução, o projeto gera:

resultados.csv
recomendacoes.csv
gráfico de acurácia
gráfico de custo
gráfico de consistência

🔄 Fluxo do Sistema
Inputs
→ Prompt Builder
→ Técnicas de Prompting
→ Ollama Cloud
→ Avaliação
→ Relatórios
→ Gráficos

🔐 Segurança

A chave da API deve permanecer apenas no arquivo .env.

O repositório contém apenas o arquivo .env.example.

👥 Integrantes
Nome Integrante 1
Nome Integrante 2
Nome Integrante 3

🎯 Disciplina

Prompt Engineering & Artificial Intelligence — FIAP