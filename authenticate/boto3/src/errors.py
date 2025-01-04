import os

import boto3
from botocore.exceptions import ClientError


class _NoAwsCredentials:
    def run(self):
        self._drop_aws_environ_values()
        try: 
            self._run_s3_request()
        except ClientError as exception:
            assert exception.response["Error"]["Code"] == "AccessDenied"

    def _drop_aws_environ_values(self):
        for environ_key in ("AWS_SECRET_ACCESS_KEY", "AWS_SECURITY_TOKEN", "AWS_SESSION_TOKEN", "AWS_DEFAULT_REGION"):
            os.environ.pop(environ_key, None)

    def _run_s3_request(self):
        session = boto3.Session()
        s3_client = session.client("s3")
        s3_client.list_objects_v2(Bucket="foo", Prefix="bar", Delimiter="/")


class _IncorrectAwsCredentials:
    def run(self):
        self._set_aws_credentials()
        try:
            self._run_s3_request()
        except ClientError as exception:
            assert exception.response["Error"]["Code"] == "InvalidAccessKeyId"

    def _set_aws_credentials(self):
        """ "
        http://docs.getmoto.org/en/latest/docs/getting_started.html#how-do-i-avoid-tests-from-mutating-my-real-infrastructure
        """
        os.environ["AWS_ACCESS_KEY_ID"] = "foo"
        os.environ["AWS_SECRET_ACCESS_KEY"] = "foo"
        os.environ["AWS_SECURITY_TOKEN"] = "foo"
        os.environ["AWS_SESSION_TOKEN"] = "foo"
        os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

    def _run_s3_request(self):
        session = boto3.Session()
        s3_client = session.client("s3")
        s3_client.list_objects_v2(Bucket="foo", Prefix="bar", Delimiter="/")


if __name__ == "__main__":
    _NoAwsCredentials().run()
    _IncorrectAwsCredentials().run()
