def lambda_handler(event, context):
    body = ""
    with open("index.html") as f:
        body = f.read()
    return {
        'statusCode': 200, 
        'body': body
    }