def montar_prompt(instrucao, contexto, input_dados, formato_output):
    componentes = [instrucao, contexto, input_dados, formato_output]

    for item in componentes:
        if not item:
            raise ValueError("Todos os componentes devem ser preenchidos")

    prompt = f"""
INSTRUÇÃO:
{instrucao}

CONTEXTO:
{contexto}

INPUT:
{input_dados}

FORMATO DE SAÍDA:
{formato_output}
"""

    return prompt


def adicionar_exemplos(prompt, exemplos):
    bloco = "\n\nEXEMPLOS:\n"

    for exemplo in exemplos:
        bloco += f'Input: {exemplo["input"]}\n'
        bloco += f'Output: {exemplo["output"]}\n\n'

    return prompt + bloco


def adicionar_cot(prompt, passos):
    bloco = "\nPENSE PASSO A PASSO:\n"

    for i, passo in enumerate(passos, start=1):
        bloco += f"{i}. {passo}\n"

    return prompt + bloco
