"""
    EXTRACT
    Através de uma URL de download obtemos o arquivo e salvamos em formato csv
"""
import logging
import time
from datetime import datetime
import awswrangler as wr
import pandas as pd
import os

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def lambda_handler(event, context):
    analise_covid_extract()
    return {'statusCode': 200}


def analise_covid_extract():
    start = time.time()

    bucket_name = os.getenv('BUCKETNAME', 'analisecovid')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    execution_day = datetime.now().strftime("%Y-%m-%d")
    name_dataset = f'owid_covid19_{timestamp}.csv'
    source_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

    LOGGER.info('Extraction started.')

    df = pd.read_csv(source_url)

    s3_path = f"s3://{bucket_name}/owid/{execution_day}/{name_dataset}"

    wr.s3.to_csv(df, s3_path, index=False)

    LOGGER.info('Extraction finish.')
    end = time.time()
    LOGGER.info(f'Time elapsed {end-start}s.')