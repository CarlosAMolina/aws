import os
from pathlib import Path
from botocore.exceptions import ClientError

import boto3
from moto import mock_aws


class _S3Server:
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


class _NoBucket:
    def __init__(self):
        self._s3_server = _S3Server()

    def run(self):
        self._s3_server.start()
        error_code = None
        try:
            self._run_s3_request()
        except ClientError as exception:
            error_code = exception.response["Error"]["Code"]
        self._s3_server.stop()
        _assert_error_code_has_expected_value(error_code, "NoSuchBucket")

    def _run_s3_request(self):
        session = boto3.Session()
        s3_client = session.client("s3")
        s3_client.list_objects_v2(Bucket="foo", Prefix="bar", Delimiter="/")


def _assert_error_code_has_expected_value(error_code: str | None, expected_value: str):
    if error_code != expected_value:
        raise ValueError(f"Current value: {error_code}. Expected value: {expected_value}")

if __name__ == "__main__":
    _NoBucket().run()
