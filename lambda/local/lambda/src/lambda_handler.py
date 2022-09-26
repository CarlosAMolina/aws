def lambda_handler(event: dict, context):
    response = {"result": event.get("file_path")}
    return response


if __name__ == "__main__":
    event = {"file_path": "/foo/bar"}
    response = lambda_handler(event, None)
    print(response)