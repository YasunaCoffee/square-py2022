import json
import os
from square.client import Client
import requests

def lambda_handler(event, context):
    client = Client(
    access_token=os.environ['SQUARE_ACCESS_TOKEN'],
    environment='sandbox')

    result = client.customers.create_customer(
        body = {
            "idempotency_key": "59973bb6-75ae-497a-a006-b2490example",
            "given_name": "Ya",
            "family_name": "Mi",
            "company_name": "ACME Inc.",
            "nickname": "Junior",
            "email_address": "a@acme.com",
            "phone_number": "+1 (206) 222-3456"
        }
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)


    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
                # "location": ip.text.replace("\n", "")
            }
        ),
    }
