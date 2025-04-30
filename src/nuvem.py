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

    stopwords = nlp.Defaults.stop_words
    if stopwords_extras:
        stopwords = stopwords.union(stopwords_extras)

    palavras_filtradas = [token.text for token in doc if token.is_alpha and token.text not in stopwords]
    texto_filtrado = " ".join(palavras_filtradas)

    wc = WordCloud(
        width=800,
        height=400,
        background_color='white',
        stopwords=stopwords
    ).generate(texto_filtrado)

    return wc
