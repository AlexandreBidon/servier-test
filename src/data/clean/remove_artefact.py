"""
Removes the artefact appearing because of string conversion.
"""
import re
import logging
from typing import List
import pandas as pd

def remove_artefact(df: pd.DataFrame, column_list: List[str]):
    """
    Removes the artefact appearing because of string conversion.
    """
    for column in column_list:
        # Checks if the column is in the dataframe
        if column in df.columns:
            df[column] = df[column].apply(lambda x: re.sub(r'\\x[0-9a-fA-F]+',r'', x))
            logging.debug("Successfully removed artefact from column %s", column)
        else:
            # Log to warn the user about the problem
            # Another solution would be to return an error
            logging.warning("Could not find column %s while removing artefact.", column)
    return df
