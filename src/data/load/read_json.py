import pandas as pd

def import_json_file(file_path: str):
    """
    
    """
    if (file_path.endswith(".json")):
        return pd.read_json(file_path)
    else:
        return Exception("The file is not a JSON")