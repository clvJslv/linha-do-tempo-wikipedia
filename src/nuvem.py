# src/nuvem.py
import spacy
from wordcloud import WordCloud

# Carrega modelo do spaCy
nlp = spacy.load("pt_core_news_lg")

def gerar_nuvem_de_palavras(texto, stopwords_extras=None):
    """
    Gera e retorna uma nuvem de palavras a partir do texto, removendo stopwords via spaCy.
    """
    doc = nlp(texto.lower())

    # Stopwords adicionais específicas para contexto histórico
    stopwords_personalizadas = {
        "sendo", "apesar", "durante", "sido", "seguem", "paz", "ano", "vez",
        "data", "parte", "passou", "apesar", "produto", "milhões", "direito",
        "início","dia"
    }

    stopwords = nlp.Defaults.stop_words.union(stopwords_personalizadas)
    if stopwords_extras:
        stopwords = stopwords.union(stopwords_extras)

    palavras_filtradas = [
        token.lemma_ for token in doc
        if token.is_alpha and token.lemma_ not in stopwords and token.pos_ in {"NOUN", "PROPN"}
    ]

    texto_filtrado = " ".join(palavras_filtradas)

    wc = WordCloud(
        width=800,
        height=400,
        background_color='black',
        colormap='tab10',
        stopwords=stopwords
    ).generate(texto_filtrado)

    return wc

