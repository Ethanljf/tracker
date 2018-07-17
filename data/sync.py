import os
import boto3


def upload_s3(bucket: str, results_path: str, date: str) -> None:
    s3 = boto3.resource("s3") # pylint: disable=invalid-name

    for root, _, files in os.walk(results_path):
        for file in files:
            path = os.path.join(root, file)
            s3.meta.client.upload_file(path, bucket, os.path.join(date, path))
