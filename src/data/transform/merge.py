import pandas as pd

def merge_data(left_dataframe: pd.DataFrame, right_dataframe: pd.DataFrame, how="inner"):
    return pd.merge(
        left_dataframe,
        right_dataframe,
        how=how
    )
