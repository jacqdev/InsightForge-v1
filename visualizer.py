import matplotlib.pyplot as plt
import pandas as pd

def plot_data(df: pd.DataFrame):
    """
    Gera gráficos simples a partir do DataFrame.
    """
    # Histograma das temperaturas
    df["Temperatura"].plot(kind="hist", bins=20, title="Distribuição das Temperaturas")
    plt.xlabel("Temperatura (°C)")
    plt.show()

    # Série temporal
    df.plot(y="Temperatura", title="Temperatura ao longo do tempo")
    plt.ylabel("Temperatura (°C)")
    plt.show()
