import os
import pandas

def import_file(file_path: str):
    if (file_path.endswith(".csv")):
        return pandas.read_csv(file_path)
    elif (file_path.endswith(".json")):
        return pandas.read_json(file_path)
    else:
        return Exception("Couldn't import file: format not supported")