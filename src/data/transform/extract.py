import pandas as pd
from typing import List


def extract_columns(df: pd.DataFrame, column_list: List[str]):
    """
    
    """
    if all([column in df.columns for column in column_list]):
        return df[column_list]
    else:
        return Exception("Could not extract columns from dataset")
    