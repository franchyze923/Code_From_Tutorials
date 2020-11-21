import arcpy
import boto3
from botocore.handlers import disable_signing
import os

s3 = boto3.resource('s3')
s3.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
bucket = 'landsat-pds'

my_bucket = s3.Bucket(bucket)

path = "150"
row = "045"

download_folder = r"E:\Youtube_Videos\Landsat Data"
prefix = "c1/L8/{}/{}/".format(path, row)

landsat_bands = []

how_many_times_to_run = 5
counter = 0

for file in my_bucket.objects.filter(Prefix=prefix):

    if counter == how_many_times_to_run:
        break
    vsis3_image_path = os.path.join("/vsis3/", bucket, file.key).replace("\\", "/")
    if vsis3_image_path.endswith(".TIF"):
        vsis3_list = vsis3_image_path.split("/")

        if vsis3_image_path[-6:-4] == 'B2' or vsis3_image_path[-6:-4] == 'B3' or vsis3_image_path[-6:-4] == 'B4':
            print("Downloading {}".format(vsis3_image_path))
            my_bucket.download_file(file.key, os.path.join(download_folder, vsis3_list[8]))
            print("Adding: {} to list".format(os.path.join(download_folder, vsis3_list[8])))
            landsat_bands.append(os.path.join(download_folder, vsis3_list[8]))

            if len(landsat_bands) == 3:
                print("Running composite bands with these values {}".format(list(reversed(landsat_bands))))

                arcpy.CompositeBands_management(list(reversed(landsat_bands)), os.path.join(download_folder, "landsat_composite_{}.tif".format(counter)))
                print(arcpy.GetMessages())
                counter += 1
                landsat_bands = []
                print("set landsat bands back to 0")

print("Finished Processing {} Landsats".format(how_many_times_to_run))