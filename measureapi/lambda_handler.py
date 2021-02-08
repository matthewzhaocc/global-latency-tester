import requests

def lambda_handler(event, context):
    return {
        "latency": requests.get(event["url"]).elapsed.total_seconds()
    }

if __name__ == "__main__":
    event = {
        "url":"https://google.com"
    }
    print(lambda_handler(event, ""))