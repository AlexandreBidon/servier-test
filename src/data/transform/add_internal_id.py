import uuid
import pandas as pd



def add_internal_id(df: pd.DataFrame, column_name = "internal_id"):
    """
    Add a new column filled with unique UUID.
    """
    df[column_name] = [str(uuid.uuid4()) for _ in range(len(df.index))]
    return df
