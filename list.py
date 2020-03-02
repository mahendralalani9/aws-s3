import json
import boto3
import botocore
import os

conn = boto3.client('s3') 
for key in s3.list_objects(Bucket='smashistaging',Prefix='fbtest2/')['Contents']:
    print("Hii")
    print(key['Key'])
