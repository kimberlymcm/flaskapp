''' Util functions to interface with Dynamodb databases '''
from datetime import datetime

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

