import os
import pandas as pd
import matplotlib.pyplot as plt


def gerar_tabela(resultados):
    df = pd.DataFrame(resultados)
    os.makedirs("output", exist_ok=True)
    df.to_csv("output/resultados.csv", index=False, encoding="utf-8")
    print(df)
    return df


def grafico_acuracia(df):
    os.makedirs("output/graficos", exist_ok=True)
    media = df.groupby(["tarefa", "tecnica"])["acuracia"].mean().unstack()

    plt.figure(figsize=(10, 6))
    media.plot(kind="bar")
    plt.title("Acurácia por Técnica e Tarefa")
    plt.ylabel("Acurácia média")
    plt.xlabel("Tarefa")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig("output/graficos/acuracia.png")
    plt.close()


def grafico_custo(df):
    media = df.groupby("tecnica")["tokens_total"].mean()

    plt.figure(figsize=(8, 5))
    media.plot(kind="bar")
    plt.title("Custo Médio por Técnica")
    plt.ylabel("Tokens médios")
    plt.xlabel("Técnica")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig("output/graficos/custo.png")
    plt.close()


def grafico_temperatura(resultados_temp):
    os.makedirs("output/graficos", exist_ok=True)

    temps = [item["temperatura"] for item in resultados_temp]
    consistencias = [item["consistencia"] for item in resultados_temp]
    plt.figure(figsize=(8, 5))
    plt.plot(temps, consistencias, marker="o")

    plt.title("Consistência por Temperatura")
    plt.xlabel("Temperatura")
    plt.ylabel("Consistência (%)")
    plt.ylim(90, 101)
    plt.xticks(temps)
    for x, y in zip(temps, consistencias):
        plt.text(x, y + 0.2, f"{y:.0f}%", ha="center")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("output/graficos/temperatura.png")
    plt.close()


def recomendar(df):
    recomendacoes = []

    print("\nRecomendação por tarefa:")

    for tarefa, grupo in df.groupby("tarefa"):
        resumo = grupo.groupby("tecnica").agg(
            {"acuracia": "mean", "tokens_total": "mean", "tempo_ms": "mean"}
        )

        # Critério: melhor acurácia; em empate, menor custo em tokens.
        resumo = resumo.sort_values(
            by=["acuracia", "tokens_total"], ascending=[False, True]
        )

        melhor = resumo.index[0]
        linha = resumo.iloc[0]

        recomendacao = {
            "tarefa": tarefa,
            "melhor_tecnica": melhor,
            "acuracia_media": round(linha["acuracia"], 2),
            "tokens_medios": round(linha["tokens_total"], 2),
            "tempo_medio_ms": round(linha["tempo_ms"], 2),
        }

        recomendacoes.append(recomendacao)

        print(
            f"- {tarefa}: {melhor} "
            f"(acurácia={recomendacao['acuracia_media']}, "
            f"tokens={recomendacao['tokens_medios']})"
        )

    pd.DataFrame(recomendacoes).to_csv(
        "output/recomendacoes.csv", index=False, encoding="utf-8"
    )

    return recomendacoes
