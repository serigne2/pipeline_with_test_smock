import pandas as pd
import requests

def extract_csv(file_path: str) -> pd.DataFrame:

    return pd.read_csv(file_path,index_col=False)

def extract_weather(api_url: str, city: str, api_key: str) -> dict:

    url = f"{api_url}?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch weather data for {city}")
    return response.json()
