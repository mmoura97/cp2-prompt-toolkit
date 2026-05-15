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
    import os
    import matplotlib.pyplot as plt
    import numpy as np

    os.makedirs("output/graficos", exist_ok=True)

    media = df.groupby(["tarefa", "tecnica"])["acuracia"].mean().unstack()

    tarefas = media.index
    tecnicas = media.columns

    x = np.arange(len(tarefas))
    largura = 0.2

    plt.figure(figsize=(10, 6))

    for i, tecnica in enumerate(tecnicas):
        valores = media[tecnica]

        barras = plt.bar(x + i * largura, valores, largura, label=tecnica)

        # valores nas barras
        for barra in barras:
            altura = barra.get_height()

            plt.text(
                barra.get_x() + barra.get_width() / 2,
                altura + 0.02,
                f"{altura:.1f}",
                ha="center",
                va="bottom",
                fontsize=9,
            )

    plt.title("Acurácia por Técnica e Tarefa")
    plt.ylabel("Acurácia média")
    plt.xlabel("Tarefa")

    plt.xticks(x + largura * (len(tecnicas) - 1) / 2, tarefas, rotation=20)

    plt.ylim(0, 1.15)

    plt.legend(title="Técnica")

    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()

    plt.savefig("output/graficos/acuracia.png", dpi=300)

    plt.close()


def grafico_custo(df):
    import os
    import matplotlib.pyplot as plt

    os.makedirs("output/graficos", exist_ok=True)

    custo = df.groupby("tecnica")["tokens_total"].mean().sort_values(ascending=False)

    plt.figure(figsize=(9, 5))

    barras = plt.bar(custo.index, custo.values)

    plt.title("Custo Médio por Técnica")
    plt.xlabel("Técnica")
    plt.ylabel("Tokens médios")

    plt.xticks(rotation=30, ha="right")

    for barra in barras:
        altura = barra.get_height()
        plt.text(
            barra.get_x() + barra.get_width() / 2,
            altura + 1,
            f"{altura:.0f}",
            ha="center",
            va="bottom",
        )

    plt.tight_layout()
    plt.savefig("output/graficos/custo.png")
    plt.close()


def grafico_temperatura(resultados_temp):
    import os
    import matplotlib.pyplot as plt

    os.makedirs("output/graficos", exist_ok=True)

    temps = [item["temperatura"] for item in resultados_temp]
    consistencias = [item["consistencia"] for item in resultados_temp]

    labels = [str(t) for t in temps]

    plt.figure(figsize=(8, 5))

    barras = plt.bar(labels, consistencias)

    plt.title("Consistência por Temperatura")
    plt.xlabel("Temperatura")
    plt.ylabel("Consistência (%)")

    plt.ylim(90, 101)

    for barra in barras:
        altura = barra.get_height()
        plt.text(
            barra.get_x() + barra.get_width() / 2,
            altura + 0.2,
            f"{altura:.0f}%",
            ha="center",
            va="bottom",
        )

    plt.grid(axis="y", alpha=0.3)

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


def gerar_resumo_resultados(df):
    import os

    os.makedirs("output", exist_ok=True)

    resumo = (
        df.groupby(["tarefa", "tecnica"])
        .agg(
            acuracia_media=("acuracia", "mean"),
            tokens_medios=("tokens_total", "mean"),
            tempo_medio_ms=("tempo_ms", "mean"),
        )
        .reset_index()
    )

    resumo["acuracia_percentual"] = (resumo["acuracia_media"] * 100).round(1)

    resumo["tokens_medios"] = resumo["tokens_medios"].round(0).astype(int)

    resumo["tempo_medio_ms"] = resumo["tempo_medio_ms"].round(2)

    resumo = resumo[
        [
            "tarefa",
            "tecnica",
            "acuracia_percentual",
            "tokens_medios",
            "tempo_medio_ms",
        ]
    ]

    resumo.to_csv("output/resumo_resultados.csv", index=False, encoding="utf-8-sig")
