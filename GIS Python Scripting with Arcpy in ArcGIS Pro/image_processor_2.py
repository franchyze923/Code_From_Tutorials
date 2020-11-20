import arcpy
import boto3
from botocore.handlers import disable_signing
import os

s3 = boto3.resource('s3')
s3.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
bucket = 'njogis-imagery'


mosaic_dataset = r"E:\Youtube_Videos\New File Geodatabase.gdb\youtube_test_mosaic_dataset"

my_bucket = s3.Bucket(bucket)

prefix = "2015/cog/"

counter = 0
images_to_add =[]

for file in my_bucket.objects.filter(Prefix=prefix):

    counter+=1
    vsis3_image_path = os.path.join("/vsis3/", bucket, file.key).replace("\\", "/")
    print("Adding {} to list".format(vsis3_image_path))
    print("counter = {}".format(counter))
    images_to_add.append(vsis3_image_path)

    if counter > 20:
        break

print("This is the image list, to be used as input for AddRasters {}".format(images_to_add))

arcpy.AddRastersToMosaicDataset_management(mosaic_dataset, "Raster Dataset", images_to_add)
print(arcpy.GetMessages())
print("Program finished")