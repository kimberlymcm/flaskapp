''' Util functions to interface with Athena databases '''
import os

import boto3

AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_KEY = os.environ['AWS_SECRET_KEY']
SCHEMA_NAME = "iot_s3"
S3_STAGING_DIR = "s3://airquality-iot-firehose-longterm/athena_query_results"
AWS_REGION = "us-west-2"


athena_client = boto3.client(
    "athena",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION,
)

query_response = athena_client.start_query_execution(
    QueryString="SELECT * FROM airquality_test LIMIT 10",
    QueryExecutionContext={"Database": SCHEMA_NAME},
    ResultConfiguration={
        "OutputLocation": S3_STAGING_DIR,
        "EncryptionConfiguration": {"EncryptionOption": "SSE_S3"},
    },
)
while True:
    try:
        # This function only loads the first 1000 rows
        athena_client.get_query_results(
            QueryExecutionId=query_response["QueryExecutionId"]
        )
        break
    except Exception as err:
        if "not yet finished" in str(err):
            time.sleep(0.001)
        else:
            raise err

import pandas as pd
S3_BUCKET_NAME = "s3-results-bucket"
S3_OUTPUT_DIRECTORY = "output"
temp_file_location: str = "athena_query_results.csv"
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION,
)
s3_client.download_file(
    S3_BUCKET_NAME,
    f"{S3_OUTPUT_DIRECTORY}/{query_response['QueryExecutionId']}.csv",
    temp_file_location,
)
return pd.read_csv(temp_file_location)

"""from datetime import datetime

import boto3
from boto3.dynamodb.conditions import Key
import pandas as pd


# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('iot_table')

def get_data():
    done = False
    start_key = None
    allItems = []
    while not done:
        if start_key == None:
            response = table.query(
                KeyConditionExpression=Key('device_id').eq('enviro'))
        else:
            response = table.query(
                KeyConditionExpression=Key('device_id').eq('enviro'),
                ExclusiveStartKey=start_key
        )
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None
        allItems.append(response['Items'])
    new_df = pd.concat([pd.DataFrame(pd.json_normalize(x)) for x in allItems])

    return new_df

