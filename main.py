#importar bibliotecas
#pip install yfinance
import streamlit as st
import pandas as pd 
import yfinance as yf
#funções de carregamento dos dados
#BTG, Itaú
@st.cache_data #atribui funcionalidade (decorator) // armazenamento em cache // boa prática
def carregar_dados(empresas):
    tickers = " ".join(empresas)
    # Formatação para "BPAC11.SA ITUB4.SA XPBR31.SA BPAN4.SA"

    dados_acao = yf.TickerS(empresa)
    cotacoes_acao = dados_acao.history(period="1d", start="2014-01-01", end="2024-08-01") #histórico de cotações
    print(cotacoes_acao)
    cotacoes_acao = cotacoes_acao[["Close"]] #printa como uma tabela do pandas até fechamento da ação
    return cotacoes_acao

acoes = ["BPAC11.SA", "ITUB4.SA", "XPBR31.SA", "BPAN4.SA"]
carregar_dados("BPAC11.SA")
print(dados)

#visualizações 
dados = carregar_dados(acoes)

#criar interface streamlit
st.write("""
# Precificação de ações
O gráfico representa a volução do preço das ações do BTG (BPAC11) ao longo dos anos
""") #markdown com ####

#gráfico
st.line_chart(dados)
