import requests
import pandas as pd

def fetch_weather_data(lat=-22.8, lon=-43.3):
    """
    Coleta dados de temperatura usando a API Open-Meteo.
    Retorna um DataFrame com as temperaturas.
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()

    # Cria DataFrame com as temperaturas e os horários
    df = pd.DataFrame({
        "DataHora": data["hourly"]["time"],
        "Temperatura": data["hourly"]["temperature_2m"]
    })

    return df

if __name__ == "__main__":
    df = fetch_weather_data()
    print("Primeiros dados coletados:")
    print(df.head())
