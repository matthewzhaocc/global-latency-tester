import requests

def lambda_handler(event, context):
    sum = 0
    for _ in range(100):
        sum += requests.get(event["url"]).elapsed.total_seconds()
    return {
        "latency": sum/100
    }
