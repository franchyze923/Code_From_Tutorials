import boto3

s3 = boto3.resource('s3')
my_bucket = s3.Bucket("fran-lambda-bucket")

text_file_location = r"E:\Youtube_Videos\boto3_project\boto3_list.txt"

with open(text_file_location, 'a') as text_file:

    for file in my_bucket.objects.all():

        if file.key.endswith(".lrc"):
            print(file.key)
            text_file.write(file.key + '\n')




