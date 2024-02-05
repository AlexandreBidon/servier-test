import pandas as pd
import logging


def add_type_column(df: pd.DataFrame, column_name="type", value=""):
    if column_name not in df.columns:
        logging.debug("Adding new column named {} with value {}".format(column_name, value))
        df[column_name] = value
        return df