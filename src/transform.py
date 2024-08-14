import pandas as pd
import config

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    print(df.head())
    df.rename(columns={"date_of_sale": "date"},inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    # Suppression du caractère '$' et conversion de la colonne price en float
    df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
    print(df.head())
    return df



def merge_weather_data(df: pd.DataFrame, weather_data: dict) -> pd.DataFrame:
    """Add weather data to the DataFrame."""
    df['weather'] = weather_data['weather'][0]['description']
    return df
