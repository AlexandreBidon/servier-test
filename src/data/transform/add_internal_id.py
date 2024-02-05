import pandas as pd
import uuid


def add_internal_id(df: pd.DataFrame, column_name = "internal_id"):
    df[column_name] = [str(uuid.uuid4()) for _ in range(len(df.index))]
    return df
