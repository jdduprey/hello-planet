import os 
from prefect_aws import AwsCredentials

aws_key = os.environ.get('AWS_KEY')
aws_secret = os.environ.get('AWS_SECRET')

AwsCredentials(
    aws_access_key_id=aws_key,
    aws_secret_access_key=aws_secret,
    aws_session_token=None,  # replace this with token if necessary
    region_name="us-west-2"
).save("my-test-aws-creds", overwrite=True)

# os.environ.get('OOI_EMAIL'