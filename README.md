# InsightForge 🔍📊

Um pipeline de análise de dados meteorológicos que coleta informações da API **Open-Meteo**, gera estatísticas e cria visualizações gráficas.  
Projeto desenvolvido em Python com foco em **análise exploratória** e **visualização de dados**.

---

## 🚀 Funcionalidades
- Coleta de dados via API (`data_fetcher.py`)
- Análise estatística básica (`analyzer.py`)
- Visualização com gráficos (`visualizer.py`)
- Execução centralizada (`main.py`)
- Testes unitários com `pytest` (`tests/`)
- Relatórios de cobertura com `pytest-cov`

---

## 🛠️ Tecnologias utilizadas
- Python 3.14
- Pandas
- Matplotlib
- Seaborn
- Requests
- Pytest
- Pytest-cov

---

## 📦 Instalação
Clone o repositório e instale as dependências:

```bash
git clone https://github.com/jacqdev/InsightForge-v1.git
cd InsightForge-v1
pip install -r requirements.txt

    - name: 📤 Enviar cobertura para Codecov
      uses: codecov/codecov-action@v4
      with:
        token: ${{ secrets.CODECOV_TOKEN }}
