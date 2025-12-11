from data_fetcher import fetch_weather_data
from analyzer import analyze_data
from visualizer import plot_data

def main():
    # 1. Coleta dados
    df = fetch_weather_data()

    # 2. Analisa dados
    analyze_data(df)

    # 3. Visualiza dados
    plot_data(df)

if __name__ == "__main__":
    main()
