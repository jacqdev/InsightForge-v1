import sys
import os
import pandas as pd

# Adiciona a pasta raiz (InsightForge) ao caminho de importação
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analyzer import analyze_data

def test_analyze_data_runs(capsys):
    df = pd.DataFrame({"Temperatura": [20, 25, 30]})
    analyze_data(df)
    captured = capsys.readouterr()
    assert "Média: 25.0" in captured.out
    assert "Máxima: 30" in captured.out
    assert "Mínima: 20" in captured.out
