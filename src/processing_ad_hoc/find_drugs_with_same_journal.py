import pandas as pd
import json


def find_drugs_with_same_journal(drug_name: str, file_path="./data/03_result/result.json"):
    """
    Retourne l’ensemble des médicaments mentionnés par les mêmes
    journaux référencés par les publications scientifiques (PubMed)
    mais non les tests cliniques (Clinical Trials)

    Parameters
    ----------
    drug_name: string
        The name of the drug to compare against
    file_path : string 
        The path of the file to import the data

    Returns
    -------
    List
        A list of a all the drugs mentionned in the same journal by a pubmed
    """

    #TODO
    return