# src/visualizacao.py
import pandas as pd
from datetime import datetime
import plotly.express as px

def criar_linha_do_tempo(df_eventos, retornar_figura=False):
    def normalizar_data(data_str):
        try:
            if data_str.lower().startswith("em "):
                return datetime.strptime(data_str[3:], "%Y")
            else:
                return datetime.strptime(data_str, "%d de %B de %Y")
        except Exception:
            return None

    df_eventos["data_convertida"] = df_eventos["data"].apply(normalizar_data)
    df_eventos = df_eventos.dropna(subset=["data_convertida"])
    df_eventos = df_eventos.sort_values("data_convertida")

    fig = px.scatter(
        df_eventos,
        x="data_convertida",
        y=["Linha do Tempo"] * len(df_eventos),
        hover_data={"data": True, "evento": True},
        text="data",
        labels={"data_convertida": "Data"},
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