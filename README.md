# 🕰️ Linha do Tempo Histórica com Wikipedia

Este projeto utiliza **Processamento de Linguagem Natural (PLN)** para extrair automaticamente eventos históricos de artigos da Wikipedia, visualizá-los e analisá-los com diferentes abordagens interativas.

## 🔍 Objetivo

Fornecer uma forma dinâmica e automatizada de visualizar a linha do tempo de eventos históricos, destacando os personagens principais e sentimentos associados às descrições dos eventos.

---

## 🚀 Funcionalidades

- 🔎 Busca por tema histórico direto da Wikipedia
- 📅 Extração automática de eventos com datas usando **spaCy**
- ☁️ Nuvem de palavras com **remoção de stopwords contextuais**
- 🧠 Reconhecimento de **personagens históricos mais citados** com `NER`
- 😊 Análise de **sentimento dos eventos** com `VADER` do NLTK
- 📊 Tabela interativa dos eventos com classificação de sentimentos

---

## 🛠️ Tecnologias e Bibliotecas

- [Python 3.11+](https://www.python.org/)
- [spaCy](https://spacy.io/) (`pt_core_news_lg`)
- [NLTK + VADER](https://www.nltk.org/)
- [Wikipedia e Wikipedia-API](https://pypi.org/project/wikipedia/)
- [Streamlit](https://streamlit.io/)
- [WordCloud](https://amueller.github.io/word_cloud/)
- [Plotly](https://plotly.com/python/)
- [Altair](https://altair-viz.github.io/) (para possíveis visualizações futuras)

---

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/linha-do-tempo-wikipedia.git
   cd linha-do-tempo-wikipedia
2. Crie e ative um ambiente virtual
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    .\venv\Scripts\activate    # Windows
3. Instale as dependências:
   pip install -r requirements.txt  
   python -m spacy download pt_core_news_lg   
   python -m nltk.downloader vader_lexicon

4. Execute:
    streamlit run app/main.py



📁 Estrutura do Projeto

linha-do-tempo-wikipedia/
│
├── app/                  # Aplicação principal Streamlit
│   └── main.py
├── src/                  # Módulos de extração e análise
│   ├── coleta.py
│   ├── extracao.py
│   ├── visualizacao.py
│   ├── nuvem.py
│   ├── entidades.py
│   └── sentimento.py
├── notebooks/            # Análises exploratórias
├── requirements.txt      # Dependências do projeto
└── README.md



