from src.prompt_builder import montar_prompt, adicionar_exemplos, adicionar_cot


def zero_shot(tarefa, texto):
    return montar_prompt(
        tarefa["instrucao"], "Resolva a tarefa abaixo.", texto, tarefa["formato_output"]
    )


def few_shot(tarefa, texto, exemplos):
    prompt = montar_prompt(
        tarefa["instrucao"],
        "Use os exemplos como referência.",
        texto,
        tarefa["formato_output"],
    )

    return adicionar_exemplos(prompt, exemplos)


def chain_of_thought(tarefa, texto, passos):
    prompt = montar_prompt(
        tarefa["instrucao"], "Analise cuidadosamente.", texto, tarefa["formato_output"]
    )

    return adicionar_cot(prompt, passos)


def role_prompting(tarefa, texto, persona):
    prompt = montar_prompt(
        tarefa["instrucao"],
        "Atue conforme a persona definida.",
        texto,
        tarefa["formato_output"],
    )

    return persona, prompt
