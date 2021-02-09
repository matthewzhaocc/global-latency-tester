import json
import base64
import boto3
from urllib.parse import unquote
regions = ["us-east-1",
        "us-east-2", 
        "us-west-1", 
        "us-west-2", 
        "ap-south-1", 
        "ap-northeast-2", 
        "ap-northeast-1", 
        "ap-southeast-2", 
        "ca-central-1",
        "eu-central-1", 
        "eu-west-2", 
        "eu-west-3", 
        "eu-north-1", 
        "sa-east-1"
        ]

def lambda_handler(event, context):
    res = ""
    url = unquote(base64.b64decode(event["body"]).decode("utf-8"))[4:]
    for region in regions:
        latency = json.loads(invoke_lambda(region, url)["Payload"].read().decode("utf-8"))["latency"]
        res = f"the latency measured in region: {region} for website {url} is {float(latency)*1000} milli seconds <br>"
    return {
        'statusCode': 200,
        'body': res
    }

def invoke_lambda(region, url):
    lambda_client = boto3.client("lambda", region_name = region)
    lambda_payload = json.dumps({"url": url})
    return lambda_client.invoke(FunctionName='apimeasure', 
                     InvocationType='RequestResponse',
                     Payload=lambda_payload)

