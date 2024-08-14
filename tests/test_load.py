import pytest
from unittest.mock import patch
import pandas as pd
from src.load import load_data

@patch('pandas.DataFrame.to_sql')
@patch('src.load.create_engine')
def test_load_data_success(mock_create_engine, mock_to_sql):
    mock_engine = mock_create_engine.return_value

    data = {'date': ['2021-01-01'], 'price': [100.0]}
    df = pd.DataFrame(data)

    load_data(df, 'test_db', 'test_table')

    mock_to_sql.assert_called_once_with('test_table', con=mock_engine, if_exists='replace', index=False, method='multi')

    print("Test passed successfully!")
