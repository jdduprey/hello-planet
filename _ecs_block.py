import os
from prefect_aws import AwsCredentials, ECSTask, S3Bucket

aws_credentials = AwsCredentials.load('my-test-aws-creds')

ecs_task = ECSTask(
    image="jdduprey/hello-solar-system:latest",
    aws_credentials=aws_credentials,
    cluster='flapjack-octopus',
    #stream_output=True,
    #execution_role_arn='arn:aws:iam::779369213159:role/execution-role-ecs'

)
ecs_task.save("my-ecs-task", overwrite=True)

# S3 bucket
bucket_name = 'ooi-prefect-code-bucket'
s3_client = aws_credentials.get_s3_client()
# s3_client.create_bucket(ss
#     Bucket=bucket_name,
#     CreateBucketConfiguration={"LocationConstraint": aws_credentials.region_name}
# )
s3_bucket = S3Bucket(
    bucket_name=bucket_name,
    credentials=aws_credentials,
)
s3_bucket.save("my-s3-bucket", overwrite=True)
