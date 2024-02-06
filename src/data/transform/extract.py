from typing import List
import pandas as pd


def extract_columns(df: pd.DataFrame, column_list: List[str]):
    """
    
    """
    if all([column in df.columns for column in column_list]):
        return df[column_list]
    return Exception("Could not extract columns from dataset")
