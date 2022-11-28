import json
import boto3
from boto3.dynamodb.conditions import Key, And
from functools import reduce

def lambda_handler(event, context):

    items = []
    available = []
    notAvailable = []
    filters = dict() # used for searching item
    
    items = event[7:].split(",")
    
    dynamodb = boto3.resource('dynamodb')
    tableName = "inventoryitemDDB"
    table = dynamodb.Table(tableName)
    
    for i in items:
        filters['itemName'] = str(i)
        response = table.scan(FilterExpression=reduce(And, ([Key(k).eq(v) for k, v in filters.items()])))
        if(response["Count"] != 0) :
            available.append(i)
            print(f"{i} is available")
        else:
            notAvailable.append(i)
            print(f"{i} is not available")
            
   
    availableS = ','.join(available)
    notAvailableS = ','.join(notAvailable)
    combine = availableS+"-"+notAvailableS
    return {
        'statusCode': 200,
        'body': json.dumps({"list":combine})
    }
