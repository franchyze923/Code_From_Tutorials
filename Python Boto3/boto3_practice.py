import boto3
import os

s3 = boto3.resource('s3')

# list all buckets and all objects
# for bucket in s3.buckets.all():
#     my_bucket = s3.Bucket(bucket.name)
#
#     for file in my_bucket.objects.all():
#         print(f"Bucket: {bucket.name} Key: {file.key}")

my_bucket = s3.Bucket("fran-lambda-bucket")

# List starting from a certain object

working_directory = r"E:\Youtube_Videos\boto3_project"

#Download objects

# for file in my_bucket.objects.filter(Prefix="fran_testing/LAMBDA_GDAL/"):
#
#     if file.key.endswith(".lrc"):
#
#         local_file_name = os.path.join(working_directory, file.key.split("/")[2])
#
#         print(f"Downloading {file.key} to {local_file_name}")
#         my_bucket.download_file(file.key, local_file_name)
#         print(f"Finished downloading {local_file_name}\n")

# upload objects

local_upload_directory = r"Z:\Frans_Files\Drone Files\20201010"

for image in os.listdir(local_upload_directory):
    full_upload_path = os.path.join(local_upload_directory, image)
    print(f"uploading {full_upload_path} to youtube_examples/{image}")
    my_bucket.upload_file(full_upload_path, f"youtube_examples/{image}")
    print(f"done uploading {full_upload_path} to youtube_examples/{image}\n")








