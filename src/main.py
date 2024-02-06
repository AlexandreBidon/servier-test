import argparse
import logging

from processing_ad_hoc import *
from pipeline.process_data_main import process_data_main


# Logging to debug the pipeline
logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)



parser = argparse.ArgumentParser(
    description="Script de traitement des données.")
parser.add_argument(
    "--pipeline", type=str, default="process_json"
    )

args = parser.parse_args()

pipeline_value = args.pipeline

if pipeline_value == "process_json":
    process_data_main()
elif pipeline_value == "get_mentions":
    print(get_journal_most_mention.get_journal_most_mentions())
else:
    print("Error, pipeline named not found")
