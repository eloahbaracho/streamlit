#importar bibliotecas
#pip install yfinance
import streamlit as st
import pandas as pd 
import yfinance as yf
from datetime import timedelta
#funções de carregamento dos dados
#BTG, Itaú
@st.cache_data #atribui funcionalidade (decorator) // armazenamento em cache // boa prática
def carregar_dados(empresas):
    tickers = " ".join(empresas)
    # Formatação para "BPAC11.SA ITUB4.SA XPBR31.SA BPAN4.SA"
    dados_acao = yf.TickerS(tickers)
    cotacoes_acao = dados_acao.history(period="1d", start="2015-01-01", end="2024-08-01") #histórico de cotações
    cotacoes_acao = cotacoes_acao["Close"] #printa como uma tabela do pandas até fechamento da ação

    return cotacoes_acao

acoes = ["BPAC11.SA", "ITUB4.SA", "XPBR31.SA", "BPAN4.SA"]
dados = carregar_dados(acoes) 

#criar interface streamlit
st.write("""
# Precificação de ações
O gráfico representa a volução do preço das ações do BTG (BPAC11) ao longo dos anos
""") #markdown 

#filtros de visualizações - sidebar
st.sidebar.header("Filtragem")

#Filtro de visualizações das ações
lista_acoes = st.sidebar.multiselect("Escolha as ações para visualizar", dados.columns) #selecionar ações
#filtrar da tabela dados com lista de ações
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1: #criar compatibilidade para exibir uma única ação 
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})
#Filtro de datas -- data mais antiga para a mais recente
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_data = st.sidebar.slider("Selecione o período", 
                                   min_value=data_inicial,
                                   max_value=data_final,
                                   value=data_final, 
                                   
value=(data_inicial, data_final), step=timedelta(days=1)) #value representa valor de início mostrado num intervalo de datas
print(intervalo_data)
#gráfico
st.line_chart(dados)
