from data.load import read_file
from data.transform import add_internal_id, add_type_column, rename, concat, extract, unique, merge, remove
from data.clean import convert_date, merge_duplicate, remove_artefact
from processing import create_output, get_drug_reference, get_journal_mentions


def process_data_main(
        drugs_path = "./data/01_raw/drugs.csv",
        clinical_trials_path = "./data/01_raw/clinical_trials.csv",
        pubmed_path_list = [
            "./data/01_raw/pubmed.csv",
            "./data/01_raw/pubmed.json"
        ]
    ):
    """
    Process les données d'entrées du datalake et les transforme. Retourne le JSON de sortie.
    """
    drugs = read_file.import_file(drugs_path)
    drugs = merge_duplicate.merge_duplicate(drugs, "drug")

    drugs = add_internal_id.add_internal_id(drugs)

    # Process clinical trials

    clinical_trials = read_file.import_file(clinical_trials_path)
    clinical_trials = merge_duplicate.merge_duplicate(clinical_trials, "scientific_title")
    clinical_trials = remove_artefact.remove_artefact(
        clinical_trials, 
        ["scientific_title", "journal"])
    clinical_trials = convert_date.convert_date(clinical_trials)
    clinical_trials = add_type_column.add_type_column(clinical_trials, "type", "clinical_trial")
    clinical_trials = rename.rename_column(clinical_trials, "scientific_title", "title")
    clinical_trials = add_internal_id.add_internal_id(clinical_trials)

    # Process Pubmed

    # TODO: retravailler cette partie du code pour permettre d'importer plus de deux fichiers pubmed
    pubmed1 = read_file.import_file(pubmed_path_list[0])
    pubmed1 = merge_duplicate.merge_duplicate(pubmed1, "title")
    pubmed1 = convert_date.convert_date(pubmed1)

    pubmed2 = read_file.import_file(pubmed_path_list[1])
    pubmed2 = merge_duplicate.merge_duplicate(pubmed2, "title")
    pubmed2 = convert_date.convert_date(pubmed2)

    pubmed = concat.concat_data(pubmed1, pubmed2)

    pubmed = add_type_column.add_type_column(pubmed, "type", "pubmed")

    pubmed = add_internal_id.add_internal_id(pubmed)


    # Merge all articles (pubmed and clinical trials)

    articles = concat.concat_data(clinical_trials, pubmed)

    # Extract all journal names

    all_journal = extract.extract_columns(articles, ["journal"])

    all_journal = unique.remove_duplicate(all_journal, ["journal"])

    # Add a unique ID for each journal
    all_journal = add_internal_id.add_internal_id(all_journal)

    ## Get article mentions of journal

    article_mentions = merge.merge_data(articles, all_journal, "left", "journal")
    article_mentions = rename.rename_column(
        article_mentions,
        "internal_id_x", 
        "internal_id_article")
    article_mentions = rename.rename_column(
        article_mentions, 
        "internal_id_y", 
        "internal_id_journal")
    article_mentions = remove.remove_columns(article_mentions, ["title", "id","journal"])

    ## Get drug reference in article

    drug_reference = get_drug_reference.get_drug_reference(drugs, articles)

    ## Finally, we can get the journal mentions of drug by merging the two dataset

    journal_mentions = get_journal_mentions.get_journal_mentions(drug_reference, article_mentions)

    create_output.create_output(
        name ="test",
        journals=all_journal,
        drugs=drugs,
        articles=articles,
        article_mentions=article_mentions,
        drug_reference=drug_reference,
        journal_mentions=journal_mentions
    )
