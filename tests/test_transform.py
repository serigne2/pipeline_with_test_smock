import pandas as pd
from src.transform import transform_data

def test_transform_data():
    data = {'date': ['2021-01-01'], 'price': ['$100']}
    df = pd.DataFrame(data)
    df = transform_data(df)
    assert df['price'].iloc[0] == 100.0
    assert pd.api.types.is_datetime64_any_dtype(df['date'])
