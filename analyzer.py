import pandas as pd

def analyze_data(df: pd.DataFrame):
    """
    Recebe um DataFrame e imprime estatísticas básicas
    de Temperatura, Umidade e Velocidade do Vento.
    """
    print("📊 Análise dos Dados")

    # Temperatura
    print("\n🌡️ Temperatura")
    print("Média:", df["Temperatura"].mean())
    print("Máxima:", df["Temperatura"].max())
    print("Mínima:", df["Temperatura"].min())

    # Umidade
    print("\n💧 Umidade Relativa")
    print("Média:", df["UmidadeRelativa"].mean())
    print("Máxima:", df["UmidadeRelativa"].max())
    print("Mínima:", df["UmidadeRelativa"].min())

    # Vento
    print("\n🌬️ Velocidade do Vento")
    print("Média:", df["VelocidadeVento"].mean())
    print("Máxima:", df["VelocidadeVento"].max())
    print("Mínima:", df["VelocidadeVento"].min())
