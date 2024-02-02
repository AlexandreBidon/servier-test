import pandas as pd


def convert_date(df: pd.DataFrame, column_name = "date"):
    """
    
    """
    df[column_name] = df[column_name].dt.strftime('%Y-%d-%m')

    return df