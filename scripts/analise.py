"""Reproduz a Tabela 2 e o Gráfico 1 da Seção 4 do trabalho.

Uso:
    python scripts/analise.py

Lê dados/frequencias.csv e gera, na pasta saida/:
  - tabela_descritiva.csv  média, mediana, desvio-padrão amostral e % por ponto da escala
  - grafico_distribuicao.png
"""
import statistics as st
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ESCALA = ["1 – Discordo totalmente", "2 – Discordo parcialmente", "3 – Neutro",
          "4 – Concordo parcialmente", "5 – Concordo totalmente"]
CORES = ["#b2182b", "#ef8a62", "#d9d9d9", "#67a9cf", "#2166ac"]


def expandir(linha) -> list[int]:
    """Converte as contagens 1–5 na lista de respostas equivalente."""
    return [p for p in range(1, 6) for _ in range(int(linha[f"n_{p}"]))]


def main() -> None:
    raiz = Path(__file__).resolve().parent.parent
    df = pd.read_csv(raiz / "dados" / "frequencias.csv")
    saida = raiz / "saida"
    saida.mkdir(exist_ok=True)

    linhas = []
    for _, r in df.iterrows():
        v = expandir(r)
        n = len(v)
        linhas.append({
            "questao": r["questao"], "n": n,
            "media": round(st.mean(v), 2), "mediana": st.median(v),
            "desvio_padrao": round(st.stdev(v), 2),
            **{f"pct_{p}": round(r[f"n_{p}"] / n * 100, 1) for p in range(1, 6)},
            "pct_concordancia": round((r["n_4"] + r["n_5"]) / n * 100, 1),
            "pct_discordancia": round((r["n_1"] + r["n_2"]) / n * 100, 1),
        })
    tab = pd.DataFrame(linhas)
    tab.to_csv(saida / "tabela_descritiva.csv", index=False)
    print(tab.to_string(index=False))

    fig, ax = plt.subplots(figsize=(9, 4.2))
    for i, (_, r) in enumerate(df.iloc[::-1].iterrows()):
        n = sum(r[f"n_{p}"] for p in range(1, 6))
        esquerda = 0
        for p in range(1, 6):
            w = r[f"n_{p}"] / n * 100
            if w:
                ax.barh(i, w, left=esquerda, color=CORES[p - 1], edgecolor="white", height=0.62)
                ax.text(esquerda + w / 2, i, f"{w:.1f}%".replace(".", ","), ha="center", va="center", fontsize=8.5)
            esquerda += w
    ax.set_yticks(range(len(df)))
    ax.set_yticklabels(df["questao"][::-1])
    ax.set_xlim(0, 100)
    ax.set_xlabel(f"% dos respondentes (n = {n})")
    ax.legend([plt.Rectangle((0, 0), 1, 1, color=c) for c in CORES], ESCALA,
              loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=3, fontsize=8, frameon=False)
    plt.tight_layout()
    plt.savefig(saida / "grafico_distribuicao.png", dpi=220)
    print("\nArquivos gerados em", saida)


if __name__ == "__main__":
    main()
