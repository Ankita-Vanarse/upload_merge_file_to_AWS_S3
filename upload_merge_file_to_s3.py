import boto3
import os
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
AWS_S3_BUCKET_NAME = "upload-csvfileto-awss3"
AWS_REGION = "ap-south-1"



# Initialize the S3 client
s3_client = boto3.client(
    service_name="s3",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

# Required variables
first_bucket_name = "firstbucket5299"
second_bucket_name = "secondbucket5299"
upload_merge_bucket_name = "mergebucket5299"

def get_last_modified(obj):
    return obj['LastModified']

def download_csv_s3(bucket_name):
    objs = s3_client.list_objects_v2(Bucket=bucket_name)['Contents']
    last_added = sorted(objs, key=get_last_modified, reverse=True)[0]
    file_name = last_added['Key']
    s3_client.download_file(bucket_name, file_name, file_name)
    print(f"{file_name} csv file downloaded from S3 bucket {bucket_name}")
    return file_name

def merge_both_files(file_name1, file_name2):
    file_name1_csv = pd.read_csv(file_name1)
    file_name2_csv = pd.read_csv(file_name2)

    # Assuming 'merge_key' is the common column for merging
    merged_df = pd.merge(file_name1_csv, file_name2_csv, on='DepartmentID', how='inner')

    merge_file_name = 'merged_upload.csv'
    merged_df.to_csv(merge_file_name, index=False)

    print(f"Merge successful. {merge_file_name} csv file created.")
    return merge_file_name

def upload_merge_file(merge_file_name):
    s3_client.upload_file(merge_file_name, upload_merge_bucket_name, merge_file_name)
    print(f"{merge_file_name} file uploaded successfully to {upload_merge_bucket_name}")

def main():
    first_file_name = download_csv_s3(first_bucket_name)
    second_file_name = download_csv_s3(second_bucket_name)
    merge_file_name = merge_both_files(first_file_name, second_file_name)
    upload_merge_file(merge_file_name)

if __name__ == "__main__":
    main()
