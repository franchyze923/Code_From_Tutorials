import os
from PIL import Image, ExifTags

img_folder = r"D:\Files\GIS\_Tutorial\Data\imgs"
img_contents = os.listdir(img_folder)

for image in img_contents:

    full_path = os.path.join(img_folder, image)
    pil_img = Image.open(full_path)

    exif = {ExifTags.TAGS[k]: v for k, v in pil_img._getexif().items() if k in ExifTags.TAGS}

    gps_all = {}

    try:
        for key in exif['GPSInfo'].keys():

            decoded_value = ExifTags.GPSTAGS.get(key)
            gps_all[decoded_value] = exif['GPSInfo'][key]

        long_ref = gps_all.get('GPSLongitudeRef')
        lat_ref = gps_all.get('GPSLatitudeRef')

        long = gps_all.get('GPSLongitude')
        lat = gps_all.get('GPSLatitude')

        print(long_ref)
        print(lat_ref)

        print(long)
        print(lat)

    except:
        print("This image has no GPS info in it")
        print(full_path)