import pandas as pd
import json5

def import_json_file(file_path: str):
    """
    Import a JSON File and returns a dataframe.

    Parameters
    ----------
    file_path : string 
        The path of the file to import

    Returns
    -------
    Dataframe
        The dataframe of the data imported
    """ 
    if (file_path.endswith(".json")):
        data_dict = import_json_file_to_dict(file_path)
        return pd.DataFrame(data_dict)
    else:
        return Exception("The file is not a JSON")

def import_json_file_to_dict(file_path: str):
    """
    Import a JSON file as a Python object (array and dict)
    This function also removes trailing commas

    Parameters
    ----------
    file_path : string 
        The path of the file to import

    Returns
    -------
    dict
        The data imported as a python dict
    """ 
    with open(file_path) as file:
        file_data = file.read()
        return json5.loads(file_data)
