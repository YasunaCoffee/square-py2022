import json
import os
from square.client import Client
import requests

def lambda_handler(event, context):

    { 
      'statusCode': 200,
      'headers': {
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Origin": '*',
        "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
      },
      'body': json.dumps('Hello from Lambda!')
    }

    client = Client(
    access_token=os.environ['SQUARE_ACCESS_TOKEN'],
    environment='sandbox')

    result = client.customers.create_customer(
        body = {
      "family_name": event['family_name'],
      "given_name": event['given_name'],
      "email_address": event['email_address'],
      "address": {
        "locality": event['locality'],
        "administrative_district_level_1": event['administrative_district_level_1'],
        "postal_code": event['postal_code'],
      },
      "phone_number": event['phone_number'],
        }
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

