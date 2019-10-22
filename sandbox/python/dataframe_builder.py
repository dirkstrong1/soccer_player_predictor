from sqlalchemy import create_engine
import pandas as pd 
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


    


def df_builder(key_value: str, value2: str, value3: str, value4: str, value5: str, value6: str) -> pd.DataFrame:
    """This function takes in a SQL query aggregate function and multiple
    values and returns a pandas dataframe"""
    assert isinstance(key_value, str), 'Selector needs to be a string.'
    assert isinstance(value2, str), 'parameter needs to be a string.'
    assert isinstance(value3, str), 'league_name needs to be a string.'
    assert isinstance(value4, str), 'Selector needs to be a string.'
    assert isinstance(value5, str), 'parameter needs to be a string.'
    assert isinstance(value6, str), 'league_name needs to be a string.'

    query = f'''SELECT "Player Name", {key_value}, {value2}, {value3},
                         {value4}, {value5}, {value6}
                         FROM fifa_19 
                         ORDER BY {key_value} DESC
                         Limit 20;'''

    engine = create_engine('postgresql:///soccer')

    df = pd.read_sql_query(query, engine)

    return df 

    