import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

dfData = st.session_state["data"]

clubes = dfData["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

dfFiltered = dfData[(dfData["Club"] == club)].set_index("Name")

st.image(dfFiltered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns = ["Age","Photo","Flag","Overall", 'Value(£)', 'Wage(£)','Joined',
           'Height(cm.)','Weight(lbs.)', 'Contract Valid Until', 'Release Clause(£)']

st.dataframe(dfFiltered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f",
                                                 min_value=0, max_value=dfFiltered["Wage(£)"].max()),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country"),
             })