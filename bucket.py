from minio import Minio
from minio.error import ResponseError, BucketNotEmpty
import os
import json
import boto3
from datetime import datetime, timedelta

s3_access_key = os.environ.get("S3_ACCESS_KEY")
s3_secret_key = os.environ.get("S3_SECRET_KEY")


client = Minio('s3.goyal.club',
               access_key=s3_access_key,
               secret_key=s3_secret_key, secure=True)

try:
    print(client.presigned_get_object('static', 'mongodb/01/001.mp4', expires=timedelta(minutes=2)))

except ResponseError as err:
    print(err)
