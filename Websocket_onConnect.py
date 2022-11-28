import json
import boto3
import botocore

def lambda_handler(event, context):
    
    connectionId = event["requestContext"]["connectionId"]
    userId = event["queryStringParameters"]["userId"]
    dynamo = boto3.resource('dynamodb').Table("OnlineConnection")
    jsonobj = {
        "UserID":userId,
        "token":connectionId
    }
    dynamo.put_item(Item = jsonobj)
    
    
    
    # code for retrive onlineunser details
    # users = []
    # response = dynamo.scan()
    # for i in response[UserID]:
    #     users.append(i)
    
    
    return {
        "isBase64Encoded": False,
        "statusCode":200,
        "headers":{"status":"success"},
        "body":"success"
    }
