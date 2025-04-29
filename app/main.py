import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from src.coleta import coletar_conteudo
from src.extracao import extrair_eventos_com_spacy
from src.visualizacao import criar_linha_do_tempo
from src.nuvem import gerar_nuvem_de_palavras
import matplotlib.pyplot as plt
import plotly.express as px

# Configuração do app
st.set_page_config(page_title="Linha do Tempo Histórica", layout="centered")

st.title("📜 Linha do Tempo Histórica com Wikipedia")

# Entrada do usuário
termo = st.text_input("🔍 Digite um termo (ex: Segunda Guerra Mundial)", value="Segunda Guerra Mundial")

if st.button("Gerar Linha do Tempo"):
    with st.spinner("Coletando conteúdo da Wikipedia..."):
        conteudo = coletar_conteudo(termo)

    if conteudo:
        with st.spinner("Extraindo eventos com datas..."):
            df_eventos = extrair_eventos_com_spacy(conteudo)

        if df_eventos.empty:
            st.warning("Nenhuma data encontrada no artigo. Tente outro termo.")
        else:
            st.success(f"{len(df_eventos)} eventos extraídos com sucesso!")
            fig = criar_linha_do_tempo(df_eventos, retornar_figura=True)
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Erro ao buscar conteúdo da Wikipedia.")
    if not df_eventos.empty:
        st.success(f"{len(df_eventos)} eventos extraídos com sucesso!")
    
   # Mostrar nuvem de palavras
    st.markdown("### ☁️ Nuvem de Palavras dos Eventos Históricos")

    texto_eventos = " ".join(df_eventos["evento"])
    nuvem = gerar_nuvem_de_palavras(texto_eventos)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(nuvem, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

    # Tabela interativa
    st.markdown("### 📋 Tabela de Eventos Históricos")
    st.dataframe(df_eventos.sort_values("data_convertida"), use_container_width=True)
    
