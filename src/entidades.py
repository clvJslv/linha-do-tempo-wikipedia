# src/entidades.py
import spacy
import pandas as pd
from collections import Counter

# Carrega modelo do spaCy
nlp = spacy.load("pt_core_news_lg")

def normalizar_nome(nome):
    """Retorna o último token como chave de agrupamento (geralmente o sobrenome)."""
    doc = nlp(nome)
    tokens = [token.text.lower() for token in doc if token.is_alpha]
    return tokens[-1] if tokens else nome.lower()

def extrair_personagens_relevantes(texto, top_n=10):
    doc = nlp(texto)
    pessoas = [ent.text.strip() for ent in doc.ents if ent.label_ == "PER"]

    agrupado = {}
    nomes_completos = {}

    for nome in pessoas:
        chave = normalizar_nome(nome)
        agrupado[chave] = agrupado.get(chave, 0) + 1

        # manter o nome mais longo como representante
        if chave not in nomes_completos or len(nome) > len(nomes_completos[chave]):
            nomes_completos[chave] = nome

    # Monta o DataFrame
    dados = [(nomes_completos[k], v) for k, v in agrupado.items()]
    dados.sort(key=lambda x: x[1], reverse=True)
    df = pd.DataFrame(dados[:top_n], columns=["personagem", "citações"])
    df.index = df.index + 1
    df.reset_index(inplace=True)
    df.rename(columns={"index": "relevância"}, inplace=True)
    
    return df