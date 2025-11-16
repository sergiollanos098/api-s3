import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    body = json.loads(event["body"])
    nombre = body["bucket"]

    s3.create_bucket(Bucket=nombre)
    
    return {
        "statusCode": 200,
        "body": json.dumps({"msg": f"Bucket {nombre} creado"})
    }
