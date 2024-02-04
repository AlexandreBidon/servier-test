import pandas as pd

def merge_duplicate(df: pd.DataFrame, column_name: str):
    """

    """
    return df.groupby(column_name, as_index=False).first()
