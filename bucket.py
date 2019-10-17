from minio import Minio
from minio.error import ResponseError, BucketNotEmpty
import os
import json
from datetime import datetime, timedelta

s3_access_key = os.environ.get("S3_ACCESS_KEY")
s3_secret_key = os.environ.get("S3_SECRET_KEY")


client = Minio('s3.goyal.club',
               access_key=s3_access_key,
               secret_key=s3_secret_key, secure=True)
