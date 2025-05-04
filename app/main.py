# app/main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import matplotlib.pyplot as plt
from src.coleta import coletar_conteudo
from src.extracao import extrair_eventos_com_spacy
from src.nuvem import gerar_nuvem_de_palavras
from src.entidades import extrair_personagens_relevantes
from src.sentimento import analisar_sentimentos
from src.processamento import extrair_ano_historico


# Configuração do app
st.set_page_config(page_title="Linha do Tempo Histórica", layout="centered")

st.title("\U0001F4DC Linha do Tempo Histórica com Wikipedia")

# Entrada do usuário
termo = st.text_input("\U0001F50D Digite um termo (ex: Segunda Guerra Mundial)", value="Imperio romano")

if st.button("Analisar Artigo"):
    with st.spinner("Coletando conteúdo da Wikipedia..."):
        conteudo = coletar_conteudo(termo)

    if conteudo:
        with st.spinner("Extraindo eventos com datas..."):
            df_eventos = extrair_eventos_com_spacy(conteudo)

        if df_eventos.empty:
            st.warning("Nenhuma data encontrada no artigo. Tente outro termo.")
        else:
            st.success(f"{len(df_eventos)} eventos extraídos com sucesso!")

            # Nuvem de palavras
            st.markdown("### ☁️ Nuvem de Palavras dos Eventos Históricos")
            texto_eventos = " ".join(df_eventos["evento"])
            nuvem = gerar_nuvem_de_palavras(texto_eventos)

            fig, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(nuvem, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig)

            # Tabela de entidades reconhecidas
            st.markdown("### 🏛️ Personagens Históricos Mais Citados")
            df_personagens = extrair_personagens_relevantes(conteudo)
            df_eventos["ano"] = df_eventos["data"].apply(extrair_ano_historico)
            df_eventos = df_eventos.dropna(subset=["ano"])
            df_eventos = df_eventos.sort_values("ano")
            st.dataframe(df_personagens, use_container_width=True)

            # Adiciona coluna de sentimento ao dataframe de eventos
            df_eventos = analisar_sentimentos(df_eventos)

            # Tabela interativa com sentimentos
            st.markdown("### 📋 Tabela de Eventos Históricos")
            st.dataframe(df_eventos[["ano", "evento", "sentimento"]].sort_values("ano"), use_container_width=True)

    else:
        st.error("Erro ao buscar conteúdo da Wikipedia.")