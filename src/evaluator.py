import json
import re
import tiktoken


def contar_tokens(texto):
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(str(texto)))


def normalizar(texto):
    return str(texto).strip().lower()


def medir_acuracia(resposta, esperado):
    resposta_norm = normalizar(resposta)
    esperado_norm = normalizar(esperado)

    if not resposta_norm:
        return 0

    # Caso esperado seja JSON/dict, tenta validar por chaves/valores.
    if isinstance(esperado, dict):
        try:
            resposta_json = json.loads(resposta)
            acertos = 0
            total = len(esperado)
            for chave, valor in esperado.items():
                if normalizar(resposta_json.get(chave, "")) == normalizar(valor):
                    acertos += 1
            return round(acertos / total, 2) if total else 0
        except Exception:
            return 0

    # Match exato ou por palavra-chave.
    if resposta_norm == esperado_norm:
        return 1

    if esperado_norm in resposta_norm:
        return 1

    return 0


def medir_consistencia(respostas):
    if not respostas:
        return 0

    respostas_normalizadas = [normalizar(r) for r in respostas]
    mais_comum = max(set(respostas_normalizadas), key=respostas_normalizadas.count)
    iguais = respostas_normalizadas.count(mais_comum)

    return round((iguais / len(respostas_normalizadas)) * 100, 2)


def testar_temperatura(client, prompt, esperado=None, system=""):
    temperaturas = [0.1, 0.5, 1.0]
    resultados = []

    for temp in temperaturas:
        respostas_temp = []

        for _ in range(3):
            resposta = client.chat(prompt, system=system, temp=temp)
            respostas_temp.append(resposta["resposta"])

        consistencia = medir_consistencia(respostas_temp)
        acuracia = (
            medir_acuracia(respostas_temp[0], esperado) if esperado is not None else 0
        )

        resultados.append(
            {
                "temperatura": temp,
                "respostas": respostas_temp,
                "consistencia": consistencia,
                "acuracia": acuracia,
            }
        )

    return resultados
