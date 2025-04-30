#extracao.py
import spacy
import pandas as pd
import re

nlp = spacy.load("pt_core_news_lg")

def extrair_eventos_com_spacy(texto):
    """
    Usa spaCy para segmentar sentenças e regex para encontrar datas em cada uma.

    Retorna:
        DataFrame com colunas ['data', 'evento']
    """
    doc = nlp(texto)
    padrao_data = r'\b(\d{1,2}\s+de\s+\w+\s+de\s+\d{4}|\bem\s+\d{4})'

    eventos = []

    for sent in doc.sents:
        frase = sent.text.strip()
        datas = re.findall(padrao_data, frase, flags=re.IGNORECASE)
        for data in datas:
            eventos.append({'data': data.strip(), 'evento': frase})

    return pd.DataFrame(eventos)
