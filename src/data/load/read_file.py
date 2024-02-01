from .read_csv import import_csv_file
from .read_json import import_json_file

def import_file(file_path: str):
    """
    
    """
    if (file_path.endswith(".csv")):
        return import_csv_file(file_path)
    elif (file_path.endswith(".json")):
        return import_json_file(file_path)
    else:
        return Exception("Couldn't import file: format not supported")