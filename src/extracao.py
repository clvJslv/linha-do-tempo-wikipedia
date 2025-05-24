# src/extracao.py
import spacy
import pandas as pd
import re

nlp = spacy.load("pt_core_news_lg")

def limpar_texto(texto):
    """
    Remove títulos e cabeçalhos da Wikipedia no formato '== Título ==' e linhas em branco.
    """
    linhas = texto.splitlines()
    texto_limpo = [linha for linha in linhas if not re.match(r"^==+.*==+$", linha.strip()) and linha.strip()]
    return " ".join(texto_limpo)

def extrair_eventos_com_spacy(texto):
    """
    Usa spaCy para segmentar sentenças e regex para encontrar datas em cada uma.

    Retorna:
        DataFrame com colunas ['data', 'evento']
    """
    texto = limpar_texto(texto)
    doc = nlp(texto)

    padrao_data = r"""
        (\d{1,2}\s+de\s+\w+\s+de\s+\d{4})|            # 10 de maio de 1940
        (em\s+\d{4})|                                     # em 1945
        (\d{1,4}\s*a\.c\.)|                               # 27 a.C.
        (\d{1,4}\s*d\.c\.)|                               # 212 d.C.
        (século\s+[ivxlcdm]+\s*(?:a\.c\.|d\.c\.))         # século V a.C.
    """

    eventos = []

    for sent in doc.sents:
        frase = sent.text.strip()
        datas = re.findall(padrao_data, frase, flags=re.IGNORECASE | re.VERBOSE)
        datas_limpos = [d for grupo in datas for d in grupo if d]
        for data in datas_limpos:
            eventos.append({'data': data.strip(), 'evento': frase})

    return pd.DataFrame(eventos)
