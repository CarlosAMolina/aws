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
        s3_client = session.client("s3", endpoint_url=os.getenv("AWS_ENDPOINT"))
        s3_client.list_objects_v2(Bucket="foo", Prefix="bar", Delimiter="/")


if __name__ == "__main__":
    _NoAwsCredentials().run()
