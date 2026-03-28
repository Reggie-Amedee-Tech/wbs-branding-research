import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


def get_competitor_data(client):

    live_db = os.getenv("BIG_QUERY_DB")

    sqlquery = f"SELECT * FROM `{live_db}`"
    
    # Run query and return as a DataFrame
    df = client.query(sqlquery).to_dataframe()
    return df