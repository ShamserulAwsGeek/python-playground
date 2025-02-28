import boto3

client = boto3.client('s3')


# response = client.create_bucket(  
#     Bucket='sham-s3-boto3-lab',
    
# )

response = client.get_bucket_acl(
    Bucket='shamserul-s3-boto3-lab',
    
)

print(response)

