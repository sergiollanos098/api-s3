import json
import boto3
import base64

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    body = json.loads(event["body"])

    bucket = body["bucket"]
    key = body["key"]          # "carpeta1/archivo.txt"
    contenido = base64.b64decode(body["archivo"])

    s3.put_object(Bucket=bucket, Key=key, Body=contenido)

    return {
        "statusCode": 200,
        "body": json.dumps({"msg": f"Archivo {key} subido a {bucket}"})
    }
