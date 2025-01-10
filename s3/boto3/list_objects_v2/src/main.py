from collections.abc import Iterator

import boto3

from s3_local_server import S3Objects
from s3_local_server import S3Server


bucket = "bucket-test"
path = "/tmp/"


class S3Client:
    def __init__(self):
        self.s3_client = boto3.client("s3")

    def get_maximum_response(self) -> dict:
        return self.s3_client.list_objects_v2(Bucket=bucket, Prefix=path, MaxKeys=1000)

    def get_with_start_listing_from(self, delimiter=None)-> Iterator[dict]:
        max_keys = 2
        last_key = ""
        delimiter = "" if delimiter is None else delimiter
        while True:
            response = self.s3_client.list_objects_v2(
                Bucket=bucket,
                Prefix=path,
                MaxKeys=max_keys,
                StartAfter=last_key,
                Delimiter=delimiter,
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
        self._s3_client = S3Client()

    def get_folders_in_the_path(self, bucket: str, query_prefix: str) -> list[str]:
        # https://stackoverflow.com/questions/71577584/python-boto3-s3-list-only-current-directory-file-ignoring-subdirectory-files
        response = self._s3_client.s3_client.list_objects_v2(
            Bucket=bucket, Prefix=query_prefix, Delimiter="/"
        )
        return self._get_folders_in_response_list_objects_v2(response)

    def _get_folders_in_response_list_objects_v2(self, response: dict) -> list[str]:
        if "CommonPrefixes" not in response:
            return []
        return [common_prefix["Prefix"] for common_prefix in response["CommonPrefixes"]]

    def get_folders_in_the_path_with_pagination(self) -> list[dict]:
        """
        https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_objects_v2.html
        """
        # The following code does not returns values to detect subdirectories.
        # To detect directory I should analyze each prefix.
        # Insetad of paginator, I've to use list_objects_v2.
        # operation_parameters = {"Bucket": bucket, "Prefix": query_prefix}
        # paginator = self._s3_client.get_paginator("list_objects_v2")
        # page_iterator = paginator.paginate(**operation_parameters)
        # for page in page_iterator:
        #    if page["KeyCount"] == 0:
        #        return []
        #    print(page)
        result = []
        for response in self._s3_client.get_with_start_listing_from(delimiter="/"):
            result += self._get_folders_in_response_list_objects_v2(response)
        return result


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
    assert ["/tmp/folder-1/"] == s3_folders_analyzer.get_folders_in_the_path(
        bucket, path
    )
    assert s3_client.get_maximum_response()["KeyCount"] == 4
    for response in s3_client.get_with_start_listing_from():
        assert response["KeyCount"] == 2
        # S3Printer().show_contents(response)
    assert [
        "/tmp/folder-1/"
    ] == s3_folders_analyzer.get_folders_in_the_path_with_pagination()
    S3Server().stop()


if __name__ == "__main__":
    run()
