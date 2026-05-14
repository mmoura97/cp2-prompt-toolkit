TASKS = [
    {
        "nome": "classificacao_sentimento",
        "tipo": "classificacao",
        "instrucao": "Classifique o sentimento do texto.",
        "formato_output": "Responda apenas POSITIVO, NEGATIVO ou MISTO.",
        "exemplos_fewshot": [
            {
                "input": "Excelente produto",
                "output": "POSITIVO"
            },
            {
                "input": "Péssima qualidade",
                "output": "NEGATIVO"
            }
        ],
        "passos_cot": [
            "Analise palavras positivas",
            "Analise palavras negativas",
            "Defina o sentimento final"
        ],
        "persona": "analista_cx"
    },
    {
        "nome": "extracao_dados",
        "tipo": "extracao",
        "instrucao": "Extraia produto, preço e defeito.",
        "formato_output": "Responda em JSON.",
        "exemplos_fewshot": [
            {
                "input": "Notebook Dell R$3500 com tela quebrada",
                "output": '{"produto":"Notebook Dell","preco":"R$3500","defeito":"tela quebrada"}'
            }
        ],
        "passos_cot": [
            "Identifique produto",
            "Identifique preço",
            "Identifique defeito"
        ],
        "persona": "especialista_suporte"
    },
    {
        "nome": "sumarizacao",
        "tipo": "sumarizacao",
        "instrucao": "Resuma o texto abaixo.",
        "formato_output": "Resumo em até 3 linhas.",
        "exemplos_fewshot": [
            {
                "input": "Texto longo...",
                "output": "Resumo curto"
            }
        ],
        "passos_cot": [
            "Identifique tema principal",
            "Remova detalhes irrelevantes",
            "Escreva resumo final"
        ],
        "persona": "redator_executivo"
    }
]