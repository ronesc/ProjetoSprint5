import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('Spotify Youtube Dataset.csv')

st.header('Spotify and YouTube Data Analysis Dashboard')

st.write('Selecione as visualizações que você gostaria de ver:')

build_histogram = st.checkbox('Criar um histograma de contagem de Streams')
build_scatter = st.checkbox('Criar um gráfico de dispersão de Views vs Stream')

if build_histogram:
    st.write('Criando um histograma para a contagem de Streams')
    fig_hist = px.histogram(df, x="Stream")
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:
    st.write('Criando um gráfico de dispersão de Views vs Stream')
    fig_scatter = px.scatter(df, x="Views", y="Stream")
    st.plotly_chart(fig_scatter, use_container_width=True)

st.header('Artista com Mais Streams no Spotify')

# Calcular o artista com mais streams
artist_streams = df.groupby('Artist')['Stream'].sum().reset_index()
most_streamed_artist = artist_streams.loc[artist_streams['Stream'].idxmax()]

st.write(f"O artista com mais streams no Spotify neste conjunto de dados é **{most_streamed_artist['Artist']}** com um total de **{most_streamed_artist['Stream']:.2f}** streams.")

