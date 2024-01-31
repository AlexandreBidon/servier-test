import os
from data.read_file import *


def test():
    result = import_file("./data/01_raw/drugs.csv")
    print(result)

    result2 = import_file("./data/01_raw/clinical_trials.csv")
    print(result2)

    result3 = import_file("./data/01_raw/pubmed.csv")
    print(result3)

    result4 = import_file("./data/01_raw/pubmed.json")
    print(result4)