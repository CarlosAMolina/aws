import boto3
import sys

bucket = sys.argv[1]
path = "tmp"

s3_client = boto3.client("s3")

def get_and_show_maximum_response():
    print(f"Init get_and_show_maximum_response")
    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=path, MaxKeys=1000)
    show_response_and_contents(response)

def get_and_show_with_start_listing_from():
    print(f"Init get_and_show_with_start_listing_from")
    max_keys = 2
    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=path, MaxKeys=max_keys)
    # while response["IsTruncated"] is True: # Invalid to know if all objects were returned, using MaxKeys -> IsTruncated=True
    while has_s3_more_objects_to_retrieve(response):
        show_contents(response)
        last_key = response["Contents"][-1]["Key"]
        print(f"last_key={last_key}")
        response = s3_client.list_objects_v2(Bucket=bucket, Prefix=path, MaxKeys=max_keys, StartAfter=last_key)
    print("All data has been retrieved")

def has_s3_more_objects_to_retrieve(response: dict) -> bool:
    return response.get("Contents") is not None

def show_response_and_contents(response: dict):
    print(response)
    show_contents(response)

def show_contents(response: dict):
    contents = response["Contents"]
    #print(len(contents))
    #print(contents)
    for index, content in enumerate(contents):
        print(index, content)



if __name__ == "__main__":
    #get_and_show_maximum_response()
    get_and_show_with_start_listing_from()

