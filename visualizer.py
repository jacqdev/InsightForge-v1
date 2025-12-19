import matplotlib.pyplot as plt
import pandas as pd

def plot_data(df: pd.DataFrame):
    """
    Gera gráficos simples a partir do DataFrame:
    - Histograma da Temperatura
    - Série temporal da Temperatura, Umidade e Vento
    """

    # Histograma das temperaturas
    df["Temperatura"].plot(kind="hist", bins=20, title="Distribuição das Temperaturas")
    plt.xlabel("Temperatura (°C)")
    plt.savefig("images/grafico_histograma.png")  # <-- salva o gráfico
    plt.show()

    # Série temporal comparando variáveis
    df.plot(x="DataHora", y=["Temperatura", "UmidadeRelativa", "VelocidadeVento"], 
            title="Variáveis Meteorológicas ao longo do tempo")
    plt.ylabel("Valores")
    plt.savefig("images/grafico_temporal.png")  # <-- salva o gráfico
    plt.show()
