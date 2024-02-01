import pandas as pd

def import_csv_file(file_path: str):
    """
    
    """
    if (file_path.endswith(".csv")):
        return pd.read_csv(file_path)
    else:
        return Exception("The file is not a CSV")