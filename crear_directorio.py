import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    body = json.loads(event["body"])

    bucket = body["bucket"]
    directorio = body["directorio"]  # ej: "carpeta1/"

    if not directorio.endswith('/'):
        directorio += '/'

    s3.put_object(Bucket=bucket, Key=directorio)

    return {
        "statusCode": 200,
        "body": json.dumps({"msg": f"Directorio {directorio} creado en {bucket}"})
    }
