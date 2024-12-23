import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

#carregar os dados
if "data" not in st.session_state:
	dfData = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
	dfData = dfData[dfData["Contract Valid Until"] >= datetime.today().year]
	dfData = dfData[dfData["Value(£)"] > 0]
	dfData = dfData.sort_values(by="Overall", ascending=False)
	st.session_state["data"] = dfData

st.markdown("# FIFA 23 OFFICIAL DATASET! ⚽")
st.sidebar.markdown("Desenvolvido por [Rafael](wwww.meusite.com.br)")

btn = st.button("Acesse os dados no Kaggle ")
if btn:
	webbrowser.open_new_tab("link do site")

st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)
