import pandas as pd
from datetime import datetime
import json
import logging

def create_output(
        name: str, 
        journals: pd.DataFrame,
        drugs: pd.DataFrame,
        articles: pd.DataFrame,
        article_mentions: pd.DataFrame,
        drug_reference: pd.DataFrame,
        journal_mentions: pd.DataFrame
        ):

    journals_list = {
        row["internal_id"]:{
            "name": row["journal"],
            "ref": [
                {
                    "id": row["internal_id_drug"],
                    "date": row["date"]
                } for index, row in journal_mentions[journal_mentions["internal_id_journal"] == row["internal_id"]].iterrows()
            ]
        } for index, row in journals.iterrows()
    }

    drugs_list = {
        row["internal_id"]:{
            "name": row["drug"].lower(),
            "atccode": row["atccode"],
            "ref": [
                {
                    "id": row["internal_id_article"],
                } for index, row in drug_reference[drug_reference["internal_id_drug"] == row["internal_id"]].iterrows()
            ]
        } for index, row in drugs.iterrows()
    }

    articles_list = {
        row["internal_id"]:{
            "name": row["title"].lower(),
            "type": row["type"],
            "ref": [
                {
                    "id": row["internal_id_journal"],
                    "date": row["date"]
                } for index, row in article_mentions[article_mentions["internal_id_article"] == row["internal_id"]].iterrows()
            ]
        } for index, row in articles.iterrows()
    }

    output = {
        "name": name,
        "date": datetime.today().strftime('%Y-%m-%d'),
        "journals": journals_list,
        "drugs": drugs_list,
        "articles": articles_list
    }

    print(output)
    with open("./data/03_result/result.json", 'w', encoding='utf8') as outfile:
        try:
            json.dump(
                output,
                outfile,
                indent=2,
                sort_keys=False,
                ensure_ascii=False
            )

        except Exception as exc:
            raise exc
