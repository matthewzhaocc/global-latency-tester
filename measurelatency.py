#!/usr/bin/python3
import sys
import json
import boto3

def invoke_lambda(region):
    lambda_client = boto3.client("lambda", region_name = region)
    lambda_payload = json.dumps({"url": sys.argv[1]})
    return lambda_client.invoke(FunctionName='apimeasure', 
                     InvocationType='RequestResponse',
                     Payload=lambda_payload)
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
for region in regions:
    latency = json.loads(invoke_lambda(region)["Payload"].read().decode("utf-8"))["latency"]
    print(f"the latency measured in region: {region} for website {sys.argv[1]} is {float(latency)*1000} milli seconds")
    
