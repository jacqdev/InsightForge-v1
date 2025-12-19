import requests
import pandas as pd

def fetch_weather_data(lat=-22.8, lon=-43.3):
    """
    Coleta dados meteorológicos usando a API Open-Meteo.
    Retorna um DataFrame com temperatura, umidade e velocidade do vento.
    """
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    )
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Erro ao coletar dados da API Open-Meteo")

    data = response.json()

    # Cria DataFrame com as variáveis meteorológicas
    df = pd.DataFrame({
        "DataHora": data["hourly"]["time"],
        "Temperatura": data["hourly"]["temperature_2m"],
        "UmidadeRelativa": data["hourly"]["relativehumidity_2m"],
        "VelocidadeVento": data["hourly"]["windspeed_10m"]
    })

    return df

if __name__ == "__main__":
    df = fetch_weather_data()
    print("Primeiros dados coletados:")
    print(df.head())
