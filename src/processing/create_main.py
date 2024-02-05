import os
from data.load import *
from data.transform import *
from data.clean import *

import logging

# Logging to debug the pipeline
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

def test():
    drugs = read_file.import_file("./data/01_raw/drugs.csv")
    drugs = merge_duplicate.merge_duplicate(drugs, "drug")

    drugs = add_internal_id.add_internal_id(drugs)
    
    print(drugs)


    clinical_trials = read_file.import_file("./data/01_raw/clinical_trials.csv")
    clinical_trials = merge_duplicate.merge_duplicate(clinical_trials, "scientific_title")
    clinical_trials = remove_artefact.remove_artefact(clinical_trials, ["scientific_title", "journal"])
    clinical_trials = convert_date.convert_date(clinical_trials)
    print(clinical_trials)

    pubmed1 = read_file.import_file("./data/01_raw/pubmed.csv")
    pubmed1 = merge_duplicate.merge_duplicate(pubmed1, "title")
    pubmed1 = convert_date.convert_date(pubmed1)

    pubmed2 = read_file.import_file("./data/01_raw/pubmed.json")
    pubmed2 = merge_duplicate.merge_duplicate(pubmed2, "title")
    pubmed2 = convert_date.convert_date(pubmed2)

    pubmed = concat.concat_data(pubmed1, pubmed2)

    # Extract all journal names

    journals_pubmed = extract.extract_columns(pubmed, ["journal"])

    journal_clinical_trial = extract.extract_columns(clinical_trials, ["journal"])

    all_journal = concat.concat_data(journals_pubmed, journal_clinical_trial)

    all_journal = unique.remove_duplicate(all_journal, ["journal"])

    # Add a unique ID for each journal
    all_journal = add_internal_id.add_internal_id(all_journal)

    print(all_journal)