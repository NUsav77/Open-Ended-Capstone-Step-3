# Access S3 NEXRAD Bucket real-time

import boto3
from botocore import UNSIGNED
from botocore.client import Config


s3 = boto3.resource("s3", config=Config(signature_version=UNSIGNED))
bucket = s3.Bucket("unidata-nexrad-level2-chunks")


# Print first 10 objects in S3 bucket
for obj in bucket.objects.limit(10):
    print(obj)

# Prints all objects in the bucket
# for obj in bucket.objects.filter(key='FOP1/178/20210618-091135-001'):
#     print(obj)