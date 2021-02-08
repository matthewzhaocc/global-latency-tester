import requests

def lambda_handler(event, context):
    return {
        "latency": requests.get(event["url"]).elapsed.total_seconds()
    }
