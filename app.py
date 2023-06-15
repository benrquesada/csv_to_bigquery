from google.cloud import bigquery
from google.oauth2 import service_account
from google.api_core.exceptions import NotFound
import configparser

# Read the config file
config = configparser.ConfigParser()
config.read('config.ini')

# Path to your service account key file
service_account_path = config['APP']['SERVICE_ACCOUNT_PATH']

# Define your BigQuery details
project_id = config['BIGQUERY']['PROJECT_ID']
dataset_id = config['BIGQUERY']['DATASET_ID']
table_id = config['BIGQUERY']['TABLE_ID']

# Define the path to your local CSV file
csv_path = config['APP']['CSV_PATH']

# Create a client instance
credentials = service_account.Credentials.from_service_account_file(service_account_path)
client = bigquery.Client(credentials=credentials, project=project_id)

# Construct a full BigQuery table identifier
table_ref = client.dataset(dataset_id).table(table_id)

try:
    client.get_table(table_ref)
    print("Table already exists. Appending data...")
    job_config = bigquery.LoadJobConfig(autodetect=True, write_disposition="WRITE_APPEND")
except NotFound:
    print("Table does not exist. Creating new table...")
    job_config = bigquery.LoadJobConfig(autodetect=True, write_disposition="WRITE_TRUNCATE")


with open(csv_path, "rb") as source_file:
    job = client.load_table_from_file(
        source_file,
        table_ref,
        location="US",  # Must match the destination dataset location.
        job_config=job_config,
    )

job.result()  # Waits for table load to complete

print("Loaded {} rows into {}:{}.".format(job.output_rows, dataset_id, table_id))
