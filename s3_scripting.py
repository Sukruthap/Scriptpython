import boto3
#####################Creating s3 bucket####################################################
s3 = boto3.resource('s3')
bucket_name = "Bucketpython"
try:
    response=s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint':'us-east-2'})
    print response

except Exception as error:
    print error