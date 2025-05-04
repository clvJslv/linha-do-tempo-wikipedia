# src/visualizacao.py 
import pandas as pd
import plotly.express as px

def criar_linha_do_tempo(df_eventos, retornar_figura=False):
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