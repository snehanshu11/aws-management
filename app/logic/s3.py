import boto3
from datetime import datetime
from .log import logging


def list_buckets():
    client = boto3.client('s3')
    buckets= client.list_buckets()['Buckets']
    return buckets

def list_bucket_objects(bucket_name:str):
    try:
        client = boto3.resource('s3')
        bucket = client.Bucket(bucket_name)
        my_map =[]
        for obj in bucket.objects.all():
            my_map.append(obj.key)
    except Exception:
        logging.error(f"[{datetime.utcnow()}]: Exception occured while getting bucket details:{bucket_name} not found.")
    return my_map


