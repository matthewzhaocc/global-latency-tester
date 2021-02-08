import requests

def lambda_handler(event, context):
    return {
        "latency": requests.get(context["url"]).elapsed.total_seconds()
    }
