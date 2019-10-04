from minio import Minio
from minio.error import ResponseError, BucketNotEmpty

client = Minio('s3.goyal.club',
               access_key='ayush',
               secret_key='ayushg1214')


try:
    # Get current policy of bucket 'my-bucketname'.
    print(client.get_bucket_policy('sample'))
except ResponseError as err:
    print(err)
