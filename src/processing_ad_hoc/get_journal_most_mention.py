import json
import pandas as pd


def get_journal_most_mentions(file_path="./data/03_result/result.json"):
    """
    Get the journal that mentions the most of different drugs

    Parameters
    ----------
    file_path : string 
        The path of the file to import the data

    Returns
    -------
    Dataframe
        A dataframe with all journals ordered by the number of different drugs mentionned
    """

    result_dict = {}

    with open(file_path, encoding='utf8') as outfile:
        data = json.load(outfile)

        for journal in data["journals"]:
            result_dict[data["journals"][journal]["name"]] = len(set([d['id'] for d in data["journals"][journal]["ref"]]))

    result_df = pd.DataFrame.from_dict(result_dict, orient='index')

    return result_df.sort_values(by=[0], ascending=False)
