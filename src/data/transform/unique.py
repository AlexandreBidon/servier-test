import pandas as pd
from typing import List


def remove_duplicate(df: pd.DataFrame, column_list: List[str]):
    return df.drop_duplicates(subset=column_list, ignore_index=True)