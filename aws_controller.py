''' Util functions to interface with Dynamodb databases '''

import boto3
from boto3.dynamodb.conditions import Key


dynamo_client = boto3.client('dynamodb', region_name='us-west-2')

def get_data(items=["pm1", "pm25", "pm10"]):
    cols_to_extract = f"device_id, #time_taken"
    for item in items:
        cols_to_extract += f", payload.{item}"
    #cols_to_extract = f"device_id, #time_taken, payload.{item}"
    response = dynamo_client.query(
        ProjectionExpression=cols_to_extract,
        ExpressionAttributeNames={"#time_taken": "time"},
        KeyConditionExpression="device_id = :enviro",
        ExpressionAttributeValues={":enviro" : {"S" : "enviro"}},
        TableName='iot_table')
    return response['Items']

