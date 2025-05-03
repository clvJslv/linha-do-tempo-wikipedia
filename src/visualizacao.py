# src/visualizacao.py 
import pandas as pd
import plotly.express as px
import re


def extrair_ano_historico(data_str):
    data_str = str(data_str).lower().strip()

    # padrão século (ex: século VI a.C.)
    match_seculo = re.search(r"século\s+([ivxlcdm]+)\s*(a\.c\.|d\.c\.)", data_str)
    if match_seculo:
        romanos = {
            'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'v': 5, 'vi': 6,
            'vii': 7, 'viii': 8, 'ix': 9, 'x': 10
        }
        valor = romanos.get(match_seculo[1])
        if valor:
            ano = valor * 100 - 50
            return -ano if "a.c" in match_seculo[2] else ano

    # padrão (570–495 a.C.), (ca. 341-270 a.C.), etc.
    match_intervalo = re.search(r"(\d{1,4})\s*[-–—]\s*(\d{1,4})\s*(a\.c\.|d\.c\.)", data_str)
    if match_intervalo:
        ano = int(match_intervalo[1])
        return -ano if "a.c" in match_intervalo[3] else ano

    # padrão único (ex: 27 a.C.)
    match_acdc = re.search(r"(\d{1,4})\s*(a\.c\.|d\.c\.)", data_str)
    if match_acdc:
        ano = int(match_acdc[1])
        return -ano if "a.c" in match_acdc[2] else ano

    # padrão solto ex: "em 212", "por 54"
    match_livre = re.search(r"(por|em|no|ano)?\s*(\d{1,4})", data_str)
    if match_livre:
        return int(match_livre[2])

    return None


def criar_linha_do_tempo(df_eventos, retornar_figura=False):
    # Aplica a nova função para extrair anos históricos
    df_eventos["ano"] = df_eventos["data"].apply(extrair_ano_historico)
    df_eventos = df_eventos.dropna(subset=["ano"])
    df_eventos = df_eventos.sort_values("ano")

    fig = px.scatter(
        df_eventos,
        x="ano",
        y=["Linha do Tempo"] * len(df_eventos),
        hover_data={"data": True, "evento": True},
        text="data",
        labels={"ano": "Ano"},
        title="\U0001F4DC Linha do Tempo Histórica Interativa",
    )

    fig.update_traces(
        mode="markers+text",
        marker=dict(size=12, color="#1f77b4"),
        textposition="top center"
    )

    fig.update_layout(
        height=600,
        showlegend=False,
        xaxis=dict(showgrid=True),
        yaxis=dict(showticklabels=False),
        hoverlabel=dict(bgcolor="white", font_size=12)
    )

    if retornar_figura:
        return fig
    else:
        fig.show()