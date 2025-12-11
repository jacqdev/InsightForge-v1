import pandas as pd

def analyze_data(df: pd.DataFrame):
    """
    Recebe um DataFrame e imprime estatísticas básicas.
    """
    print("📊 Análise dos Dados")
    print("Média:", df["Temperatura"].mean())
    print("Máxima:", df["Temperatura"].max())
    print("Mínima:", df["Temperatura"].min())
