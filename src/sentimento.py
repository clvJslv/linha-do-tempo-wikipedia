# src/sentimento.py
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

sia = SentimentIntensityAnalyzer()

def analisar_sentimentos(df_eventos):
    """
    Adiciona a coluna 'sentimento' ao dataframe de eventos com base na análise de sentimento.
    """
    sentimentos = df_eventos["evento"].apply(lambda texto: sia.polarity_scores(texto)["compound"])
    df_eventos["sentimento"] = sentimentos.apply(
        lambda score: "positivo" if score > 0.2 else "negativo" if score < -0.2 else "neutro"
    )
    return df_eventos