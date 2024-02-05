import pandas as pd
from data.transform import *


def get_journal_mentions(drug_reference: pd.DataFrame, article_mentions: pd.DataFrame):
    """

    """
    journal_mentions = merge.merge_data(drug_reference, article_mentions, "left", "internal_id_article")
    
    journal_mentions = journal_mentions[["internal_id_drug", "internal_id_journal", "date"]]

    return journal_mentions