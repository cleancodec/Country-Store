import json
import boto3
import botocore

def lambda_handler(event, context):
    connectionId = event["requestContext"]["connectionId"]
    dynamo = boto3.resource("dynamodb").Table("OnlineConnection")
    dynamo.delete_item(Key={"token":connectionId})
