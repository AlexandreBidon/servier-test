import os
from data.load.read_file import *
from data.transform.merge import *
from data.transform.concat import *
from data.clean.convert_date import *
from data.clean.merge_duplicate import *
from data.clean.remove_artefact import *

import logging

# Logging to debug the pipeline
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

def test():
    result = import_file("./data/01_raw/drugs.csv")
    result = merge_duplicate(result, "drug")
    print(result)


    result2 = import_file("./data/01_raw/clinical_trials.csv")
    result2 = merge_duplicate(result2, "scientific_title")
    result2 = remove_artefact(result2, ["scientific_title", "journal"])
    result2 = convert_date(result2)
    print(result2)

    result3 = import_file("./data/01_raw/pubmed.csv")
    result3 = merge_duplicate(result3, "title")
    result3 = convert_date(result3)

    result4 = import_file("./data/01_raw/pubmed.json")
    result4 = merge_duplicate(result4, "title")
    result4 = convert_date(result4)

    test = concat_data(result3, result4)

    print(test)