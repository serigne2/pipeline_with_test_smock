import pandas as pd
from sqlalchemy import create_engine

def load_data(df: pd.DataFrame, db_name: str, table_name: str):

    engine = create_engine(f'mysql+mysqlconnector://username:password@localhost/{db_name}')

    # Charger les données dans la base de données
    try:
        df.to_sql(table_name, con=engine, if_exists='replace', index=False, method='multi')
        print(f"Data successfully loaded into {db_name}.{table_name}")
    except Exception as e:
        print(f"Error loading data: {e}")
