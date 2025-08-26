import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('Spotify Youtube Dataset.csv')

st.header('Spotify e YouTube Analise de Dados')