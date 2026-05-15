import json

from src.tasks import TASKS
from src.techniques import zero_shot, few_shot, chain_of_thought, role_prompting
from src.llm_client import LLMClient
from src.evaluator import medir_acuracia, testar_temperatura
from src.report import (
    gerar_tabela,
    grafico_acuracia,
    grafico_custo,
    grafico_temperatura,
    recomendar,
)


def carregar_json(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def main():
    inputs = carregar_json("data/inputs.json")
    personas = carregar_json("prompts/system_prompts.json")

    client = LLMClient()

    conectado, mensagem = client.verificar_conexao()
    print(mensagem)

    if not conectado:
        print(
            "\nAtenção: o projeto continuará, mas as respostas virão vazias até o Ollama estar ativo."
        )

    resultados = []
    primeiro_prompt_valido = None
    primeiro_esperado_valido = None
    primeiro_system_valido = ""

    for tarefa in TASKS:
        nome = tarefa["nome"]
        dados = inputs[nome]

        for item in dados:
            texto = item["input"]
            esperado = item["esperado"]

            tecnicas = {
                "zero_shot": zero_shot(tarefa, texto),
                "few_shot": few_shot(tarefa, texto, tarefa["exemplos_fewshot"]),
                "chain_of_thought": chain_of_thought(
                    tarefa, texto, tarefa["passos_cot"]
                ),
            }

            persona = personas[tarefa["persona"]]
            system, role_prompt = role_prompting(tarefa, texto, persona)
            tecnicas["role_prompting"] = role_prompt

            for tecnica, prompt in tecnicas.items():
                system_prompt = system if tecnica == "role_prompting" else ""

                if primeiro_prompt_valido is None:
                    primeiro_prompt_valido = prompt
                    primeiro_esperado_valido = esperado
                    primeiro_system_valido = system_prompt

                resposta = client.chat(prompt, system=system_prompt)
                acuracia = medir_acuracia(resposta["resposta"], esperado)
                tokens_total = resposta["tokens_prompt"] + resposta["tokens_resposta"]

                resultados.append(
                    {
                        "tarefa": nome,
                        "tecnica": tecnica,
                        "input": texto,
                        "esperado": esperado,
                        "resposta": resposta["resposta"],
                        "erro": resposta["erro"],
                        "tokens_prompt": resposta["tokens_prompt"],
                        "tokens_resposta": resposta["tokens_resposta"],
                        "tokens_total": tokens_total,
                        "tempo_ms": resposta["tempo_ms"],
                        "acuracia": acuracia,
                    }
                )

    resultado_df = gerar_tabela(resultados)
    grafico_acuracia(resultado_df)
    grafico_custo(resultado_df)

    temperaturas = testar_temperatura(
        client,
        primeiro_prompt_valido,
        esperado=primeiro_esperado_valido,
        system=primeiro_system_valido,
    )

    grafico_temperatura(temperaturas)
    recomendar(resultado_df)


if __name__ == "__main__":
    main()
