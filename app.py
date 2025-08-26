import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('Spotify Youtube Dataset.csv')

st.header('Spotify e YouTube Analise de Dados')

#Agora, vamos criar o conteúdo do aplicativo baseado em Streamlit.

st.write('Selecione as visualizações que você gostaria de ver:')

build_histogram = st.checkbox('Criar um histograma de contagem de Streams')
build_scatter = st.checkbox('Criar um gráfico de dispersão de Danceability vs Energy')

if build_histogram:
    st.write('Criando um histograma para a contagem de Streams')
    fig_hist = px.histogram(df, x="Stream")
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:
    st.write('Criando um gráfico de dispersão de Danceability vs Energy')
    fig_scatter = px.scatter(df, x="Danceability", y="Energy")
    st.plotly_chart(fig_scatter, use_container_width=True)