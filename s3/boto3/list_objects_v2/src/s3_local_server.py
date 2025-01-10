import os
import random
import string

import boto3
from moto import mock_aws


class S3Server:
    def __init__(self):
        """http://docs.getmoto.org/en/latest/docs/getting_started.html"""
        self._set_aws_credentials()
        self._mock_aws = mock_aws()

    def start(self):
        self._mock_aws.start()

    def stop(self):
        self._mock_aws.stop()

    def _set_aws_credentials(self):
        """ "
        http://docs.getmoto.org/en/latest/docs/getting_started.html#how-do-i-avoid-tests-from-mutating-my-real-infrastructure
        """
        os.environ["AWS_ACCESS_KEY_ID"] = "testing"
        os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
        os.environ["AWS_SECURITY_TOKEN"] = "testing"
        os.environ["AWS_SESSION_TOKEN"] = "testing"
        os.environ["AWS_DEFAULT_REGION"] = "us-east-1"


class S3Objects:
    def __init__(self, bucket_name: str):
        self._bucket_name = bucket_name
        self._s3_resource = boto3.resource("s3")
        self._s3_client = boto3.client("s3")

    def create_bucket(self):
        bucket = self._s3_resource.Bucket(self._bucket_name)
        bucket.create()

    def upload_files(self):
        number_of_files = 3
        for index in range(number_of_files):
            content = self._get_random_string()
            file_name = f"foo-{index}.html"
            prefix = "/tmp/"
            key = f"{prefix}{file_name}"
            self._s3_client.put_object(
                Body=content, Bucket=self._bucket_name, Key=key, ContentType="text/html"
            )

    @staticmethod
    def _get_random_string() -> str:
        length = random.randint(5, 20)
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
