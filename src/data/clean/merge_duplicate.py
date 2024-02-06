"""Merge duplicates lines inside a dataframe"""

import pandas as pd

def merge_duplicate(df: pd.DataFrame, column_name: str):
    """
    Merge duplicates lines inside a dataframe
    """
    if column_name in df.columns:
        return df.groupby(column_name, as_index=False).first()
    return Exception("Column doesn't exist")
