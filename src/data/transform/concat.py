import pandas as pd

def concat_data(dataframe_1: pd.DataFrame, dataframe_2: pd.DataFrame):
    return pd.concat(
        [dataframe_1,
        dataframe_2]
    )
