import wikipedia

# Define o idioma para português
wikipedia.set_lang("pt")

def coletar_conteudo(titulo):
    """
    Busca e retorna o conteúdo de uma página da Wikipedia.
    """
    try:
        conteudo = wikipedia.page(titulo).content
        print(f"[✓] Página '{titulo}' encontrada.")
        return conteudo
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"[!] Título ambíguo. Escolha uma das opções: {e.options}")
    except wikipedia.exceptions.PageError:
        print(f"[!] Página '{titulo}' não encontrada.")
    return None
