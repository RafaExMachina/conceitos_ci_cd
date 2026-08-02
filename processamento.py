import pandas as pd
import os #Import não utilizado
import sys

def limpa_dados(df):
    #espaçamento errado, variaveis não utilizadas
    x=10
    df_limpo = df.dropna() #Remove linhas com valores nulos
    return df_limpo