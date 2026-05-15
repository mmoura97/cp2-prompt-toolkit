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

# ▶️ Como executar o projeto

## 1️⃣ Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

---

## 2️⃣ Entrar na pasta do projeto

```bash
cd cp2-prompt-toolkit
```

---

# 🐍 Criando ambiente virtual

## Windows

```bash
py -m venv venv
```

ou

```bash
python -m venv venv
```

### Ativar ambiente virtual (Windows PowerShell)

```bash
.\venv\Scripts\Activate.ps1
```

---

## Linux / MacOS

```bash
python3 -m venv venv
```

### Ativar ambiente virtual (Linux/MacOS)

```bash
source venv/bin/activate
```

---

# 📦 Instalar dependências

## Windows

```bash
pip install -r requirements.txt
```

---

## Linux / MacOS

```bash
pip install -r requirements.txt
```

---

# ⚙️ Configuração da API

Crie um arquivo `.env` na raiz do projeto:

```env
OLLAMA_API_KEY=sua_chave_aqui
OLLAMA_HOST=https://ollama.com
MODEL_NAME=gpt-oss:120b
TIMEOUT=120
```

---

# 🚀 Executando o projeto

## Windows

```bash
py main.py
```

ou

```bash
python main.py
```

---

## Linux / MacOS

```bash
python3 main.py
```

---

# 📊 Arquivos gerados

Após a execução, serão gerados:

```text
output/resultados.csv
output/recomendacoes.csv
output/graficos/acuracia.png
output/graficos/custo.png
output/graficos/temperatura.png
```

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