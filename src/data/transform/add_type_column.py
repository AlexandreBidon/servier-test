import logging
import pandas as pd


def add_type_column(df: pd.DataFrame, column_name="type", value=""):
    """
    Add a new column filled with the same value.
    """
    if column_name not in df.columns:
        logging.debug("Adding new column named %s with value %s", column_name, value)
        df[column_name] = value
        return df
