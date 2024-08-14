from src.extract import extract_csv, extract_weather
from src.transform import transform_data, merge_weather_data
from src.load import load_data
from src.utils import log_message
import config
import pandas as pd
import mysql.connector


def main():
    log_message("ETL pipeline started.", "info")

    log_message("Extracting data from CSV.", "info")
    sales_data = extract_csv(config.CSV_FILE_PATH)

    log_message(f"Extracting weather data for {config.CITY}.", "info")
    weather_data = extract_weather(config.API_URL, config.CITY, config.API_KEY)

    log_message("Transforming data.", "info")
    transformed_data = transform_data(sales_data)

    log_message("Merging weather data.", "info")
    final_data = merge_weather_data(transformed_data, weather_data)

    log_message("Loading data into database.", "info")
    load_data(final_data, config.DB_NAME, config.TABLE_NAME)

    log_message("ETL pipeline finished.", "info")


if __name__ == "__main__":
    main()

