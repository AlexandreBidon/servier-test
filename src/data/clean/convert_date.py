import pandas as pd


def convert_date(df: pd.DataFrame, column_name = "date"):
    """
    
    """
    # If the date column exists
    if column_name in df.columns:
        df[column_name] = pd.to_datetime(df[column_name], format='mixed')
        df[column_name] = df[column_name].dt.strftime('%Y-%d-%m')

    return df