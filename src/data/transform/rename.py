import pandas as pd


def rename_column(df: pd.DataFrame, old_name: str, new_name :str):
    if old_name in df.columns:
        if new_name not in df.columns:
            df = df.rename(columns={old_name: new_name})

            return df