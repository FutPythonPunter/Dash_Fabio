import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta

st.set_page_config(
    page_title='Dash do Fábio',
)

def pagina_01():
    st.title("Bases de Dados")

    st.sidebar.header("Leagues")
    selected_league = st.sidebar.selectbox('League',['England','Germany'])

    st.sidebar.header("Season")
    selected_season = st.sidebar.selectbox('Season',['2022/2023','2021/2022'])
    
    # Webscraping Football Data
    def load_data(league, season):
        if (selected_league == 'England') & (selected_season == '2022/2023'):
            data = pd.read_csv("https://www.football-data.co.uk/mmz4281/2223/E0.csv")
        if (selected_league == 'England') & (selected_season == '2021/2022'):
            data = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/E0.csv")
        if (selected_league == 'Germany') & (selected_season == '2022/2023'):
            data = pd.read_csv("https://www.football-data.co.uk/mmz4281/2223/D1.csv")
        if (selected_league == 'Germany') & (selected_season == '2021/2022'):
            data = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/D1.csv")
        return data
    df = load_data(selected_league, selected_season)
    df = df[['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','B365H','B365D','B365A']]
    df.columns = ['Date','Home','Away','Goals_H','Goals_A','Result','Odd_H','Odd_D','Odd_A']
    df = df.reset_index(drop=True)
    df.index += 1
    st.dataframe(df)

def pagina_02():
    st.title("Jogos do Dia")

    dia = st.date_input(
        "Data de Análise",
        date.today()
    )

    def load_jogos():

        url = f"https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_FlashScore/{dia}_Jogos_do_Dia_FlashScore.xlsx?raw=true"

        data = pd.read_excel(url)

        return data
    
    jogos_do_dia = load_jogos()
    
    jogos_do_dia = jogos_do_dia[['Time','League','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A']]
    jogos_do_dia.dropna(inplace=True)
    jogos_do_dia = jogos_do_dia.reset_index(drop=True)
    jogos_do_dia.index += 1
    st.dataframe(jogos_do_dia)







paginas = ['Football Data', 'Jogos do Dia']
escolha = st.sidebar.radio('',paginas)

if escolha == 'Football Data':
    pagina_01()
if escolha == 'Jogos do Dia':
    pagina_02()
