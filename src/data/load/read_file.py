from .read_csv import import_csv_file
from .read_json import import_json_file

def import_file(file_path: str):
    """
        Import the file at the specified path and return a dataframe
    """
    if file_path.endswith(".csv"):
        return import_csv_file(file_path)
    if file_path.endswith(".json"):
        return import_json_file(file_path)
    return Exception("Couldn't import file: format not supported")
