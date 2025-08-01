import os
import boto3
from dotenv import load_dotenv
from airflow.exceptions import AirflowException

load_dotenv()

class AwsS3Hook:
    def __init__(self, region_name=None):
        self.region_name = region_name or os.getenv("AWS_REGION", "us-east-1")
        self.aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
        self.aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        if not self.aws_access_key or not self.aws_secret_key:
            raise AirflowException("Missing AWS credentials in environment")

    def upload_fileobj(self, file_obj, bucket_name, key):
        session = boto3.Session(
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_key,
            region_name=self.region_name
        )
        s3_client = session.client("s3")
        s3_client.upload_fileobj(file_obj, bucket_name, key)


