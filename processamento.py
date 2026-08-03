def limpa_dados(df):
    df_limpo = df.dropna() #Remove linhas com valores nulos
    return df_limpo