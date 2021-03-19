import os
from PIL import Image, ExifTags
import arcpy

img_folder = r"D:\Files\GIS\_Tutorial\Data\imgs"
img_contents = os.listdir(img_folder)
out_shapefile = r"D:\Files\GIS\_Tutorial\outputs\out_shape.shp"
shp_list = []
spatial_ref = arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)


def shape_creator():

    pt = arcpy.Point()
    ptGeoms = []

    for p in shp_list:

        pt.X = p[0]
        pt.Y = p[1]

        ptGeoms.append(arcpy.PointGeometry(pt, spatial_ref))

    arcpy.CopyFeatures_management(ptGeoms, out_shapefile)


def convert_to_degrees(value):

    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)

    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)


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

        if long_ref == "W":
            long_in_degrees = -abs(convert_to_degrees(long))
        else:
            long_in_degrees = convert_to_degrees(long)

        if lat_ref == "S":
            lat_in_degrees = -abs(convert_to_degrees(lat))
        else:
            lat_in_degrees = convert_to_degrees(lat)

        shp_list.append([long_in_degrees, lat_in_degrees])

    except:
        print("This image has no GPS info in it")
        print(full_path)
        pass

print(shp_list)
shape_creator()