import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# Adiciona a pasta raiz ao caminho de importação
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from visualizer import plot_data

def test_plot_data_extended():
    # DataFrame com valores de exemplo
    df = pd.DataFrame({
        "DataHora": pd.date_range("2025-01-01", periods=5, freq="H"),
        "Temperatura": [20, 22, 24, 23, 25],
        "UmidadeRelativa": [60, 62, 64, 63, 65],
        "VelocidadeVento": [5, 7, 6, 8, 9]
    })

    # Executa a função
    plot_data(df)

    # Verifica se pelo menos uma figura foi criada
    assert plt.get_fignums() != []
