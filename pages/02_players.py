import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

dfData = st.session_state["data"]

clubes = dfData["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

dfPlayers = dfData[(dfData["Club"] == club)]
players = dfPlayers["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

player_stats = dfData[dfData["Name"] == player].iloc[0] # Este iloc é para pegar somente a primeira aparição do jogador caso ele apreça mais vezes

st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}") # Aqui é importante lembrar que o python se confundi se você abriu com " " dentro dela usar aspas simples ''
st.markdown(f"**Posi:** {player_stats['Club']}")

#Criando 4 colunas para ficar 
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}") # A altura está em centimetros vamos dividir por 100 para ter em metros
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}") # O peso esta em libras, para converter para gramas multiplicamos por 0.453. o ":.2f" e para formatar e aparecer apenas duas casas decimais

st.divider() #Cria uma linha de separação 

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"])) # Cria uma linha de pogresso que vai de 0 a 100

col1, col2, col3 = st.columns(3)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")