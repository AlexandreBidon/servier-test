import pandas as pd

def merge_duplicate(df: pd.DataFrame, column_name: str):
    """

    """
    if column_name in df.columns:
        return df.groupby(column_name, as_index=False).first()
    else:
        return Exception("Column doesn't exist")
