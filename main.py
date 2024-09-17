#importar bibliotecas
#pip install yfinance
import streamlit as st
import pandas as pd 
import yfinance as yf
#funções de carregamento dos dados
@st.cache_data #atribui funcionalidade (decorator) // armazenamento em cache // boa prática
def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacoes_acao = dados_acao.history(period="1d", start="2010-01-01", end="2024-08-01") #histórico de cotações
    return cotacoes_acao

carregar_dados("BPAC11.SA")
print(dados)

#prepara visualizações

#criar interface streamlit

st.write("""
# Precificação de ações
O gráfico representa a volução do preço das ações do BTG (BPAC11) ao longo dos anos
""") #markdown com ####
