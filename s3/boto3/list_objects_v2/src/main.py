from collections.abc import Iterator

import boto3

from s3_local_server import S3Objects
from s3_local_server import S3Server


bucket = "bucket-test"
path = "/tmp/"


class S3Client:
    def __init__(self):
        self._s3_client = boto3.client("s3")

    def get_maximum_response(self) -> dict:
        return self._s3_client.list_objects_v2(Bucket=bucket, Prefix=path, MaxKeys=1000)

    def get_and_show_with_start_listing_from(self) -> Iterator[dict]:
        max_keys = 2
        last_key = ""
        while True:
            response = self._s3_client.list_objects_v2(
                Bucket=bucket, Prefix=path, MaxKeys=max_keys, StartAfter=last_key
            )
            if not self._has_s3_more_objects_to_retrieve(response):
                break
            yield response
            last_key = response["Contents"][-1]["Key"]
            # print(f"last_key={last_key}")

    def _has_s3_more_objects_to_retrieve(self, response: dict) -> bool:
        """
        `response["IsTruncated"] is True` is not valid to know if all objects were
        retrieved because when using `MaxKeys`, `IsTruncated` is True.
        """
        return response.get("Contents") is not None


class S3FoldersAnalyzer:
    def __init__(self):
        self._s3_client = boto3.client("s3")

    def get_folders_in_the_path(self, bucket: str, query_prefix: str) -> list[str]:
        # https://stackoverflow.com/questions/71577584/python-boto3-s3-list-only-current-directory-file-ignoring-subdirectory-files
        response = self._s3_client.list_objects_v2(Bucket=bucket, Prefix=query_prefix, Delimiter="/")
        if "CommonPrefixes" not in response:
            return []
        return [common_prefix["Prefix"] for common_prefix in response["CommonPrefixes"]]


class S3Printer:
    def show_response_and_contents(self, response: dict):
        print(response)
        self.show_contents(response)

    def show_contents(self, response: dict):
        contents = response["Contents"]
        # print(len(contents))
        # print(contents)
        for index, content in enumerate(contents):
            print(index, content)


def run():
    S3Server().start()
    s3_objects = S3Objects(bucket)
    s3_objects.create_bucket()
    s3_objects.upload_files()
    s3_client = S3Client()
    assert s3_client.get_maximum_response()["KeyCount"] == 3
    # S3Printer().show_response_and_contents(s3_client.get_maximum_response())
    s3_folders_analyzer = S3FoldersAnalyzer()
    assert [] == s3_folders_analyzer.get_folders_in_the_path(bucket, path)
    s3_objects.upload_folder()
    assert ['/tmp/folder-1/'] == s3_folders_analyzer.get_folders_in_the_path(bucket, path)
    assert s3_client.get_maximum_response()["KeyCount"] == 4
    for response in s3_client.get_and_show_with_start_listing_from():
        assert response["KeyCount"] == 2
        # S3Printer().show_contents(response)
    S3Server().stop()


if __name__ == "__main__":
    run()
