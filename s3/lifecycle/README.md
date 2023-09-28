## Theory

### Expiration date

To retrieve the expiration date see the `How to find when objects will expire` section in this [link](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-expire-general-considerations.html). You can use the [get](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) or [head](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html) AWS actions. For example, [using the aws cli](https://docs.aws.amazon.com/cli/latest/reference/s3api/get-object.html):

```bash
aws s3api get-object --bucket BUCKET_NAME --key FILE_S3_URI DOWNLOADED_FILE
```

Example:

```bash
# aws s3api get-object --bucket weather --key 20230928/january.csv january.csv
{
    "AcceptRanges": "bytes",
    "Expiration": "expiry-date=\"Sun, 01 Oct 2023 00:00:00 GMT\", rule-id=\"two-days\"",
    "LastModified": "Thu, 28 Sep 2023 10:24:55 GMT",
    "ContentLength": 14,
    "ETag": \"ffddc...",
    "ContentType": "text/plain",
    "ServerSideEncryption": "AES256",
    "Metadata": {}
}
```
