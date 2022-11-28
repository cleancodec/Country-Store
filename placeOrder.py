import json
import boto3
from datetime import datetime


def lambda_handler(event, context):
    
    paymentyStatus = False
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    
    dynamodb = boto3.resource('dynamodb')
    tableOrder = dynamodb.Table('orderitemDDB')
    tableItem = dynamodb.Table('oderItemsDB')
    
    oderID = event['Orders'][0]['orderID']
    itemID = event['Orders'][0]['itemID']
    address = event['Orders'][0]['address']
    
    #  code for payment processing
    paymentyStatus = True
    if(paymentyStatus):
        
        # code for insert item to orderitemDDB
      tableOrder.put_item(
      Item={
            'orderID': oderID,
            'itemID': itemID,
            'address': address,
            'dateAndTime': dt_string,
            }
        ) 
    return {
        'statusCode': 200,
        'body': event
    }
