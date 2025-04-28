import sys
import spacy
import os

sys.path.append(os.path.abspath(".."))

from src.coleta import coletar_conteudo
from src.visualizacao import criar_linha_do_tempo
from src.extracao import extrair_eventos_com_spacy

conteudo = coletar_conteudo("segunda guerra mundial")

print(conteudo[:2000])  # Mostra os primeiros 1000 caracteres

# Extrai eventos com datas
df_eventos = extrair_eventos_com_spacy(conteudo)

# Mostra os primeiros eventos encontrados
df_eventos.head()


# Cria a visualização
criar_linha_do_tempo(df_eventos)

#%%

try:
    import spacy
    print("spaCy está instalado!")
except ImportError:
    print("spaCy NÃO está instalado.")

# %%
