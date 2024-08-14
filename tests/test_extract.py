import pytest
from unittest.mock import patch
from src.extract import extract_weather

@patch('src.extract.requests.get')
def test_extract_weather_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "weather": [{"description": "clear sky"}],
        "main": {"temp": 280.32}
    }

    result = extract_weather("http://api.openweathermap.org/data/2.5/weather", "Paris", "fake_api_key")
    assert result['weather'][0]['description'] == "clear sky"

@patch('src.extract.requests.get')
def test_extract_weather_failure(mock_get):
    mock_get.return_value.status_code = 404

    with pytest.raises(ValueError, match="Failed to fetch weather data for Paris"):
        extract_weather("http://api.openweathermap.org/data/2.5/weather", "Paris", "fake_api_key")