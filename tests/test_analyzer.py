import sys
import os
import pandas as pd

# Adiciona a pasta raiz ao caminho de importação
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analyzer import analyze_data

def test_analyze_data_extended(capsys):
    # DataFrame com valores de exemplo
    df = pd.DataFrame({
        "Temperatura": [20, 25, 30],
        "UmidadeRelativa": [60, 65, 70],
        "VelocidadeVento": [5, 10, 15]
    })

    # Executa a função
    analyze_data(df)
    captured = capsys.readouterr()

    # Verifica se as estatísticas foram impressas corretamente
    assert "Média: 25.0" in captured.out
    assert "Máxima: 30" in captured.out
    assert "Mínima: 20" in captured.out

    assert "Média: 65.0" in captured.out
    assert "Máxima: 70" in captured.out
    assert "Mínima: 60" in captured.out

    assert "Média: 10.0" in captured.out
    assert "Máxima: 15" in captured.out
    assert "Mínima: 5" in captured.out
