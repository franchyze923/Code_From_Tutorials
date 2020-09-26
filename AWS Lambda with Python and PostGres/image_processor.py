
import boto3
import urllib.parse
from PIL import Image, ExifTags
import psycopg2

from io import BytesIO

s3 = boto3.client('s3')


def convert_to_degress(value):

    d = float(value[0])
    m = float(value[1])
    s = float(value[2])

    return d + (m / 60.0) + (s / 3600.0)


def processor(event=None, context=None):
    bucket = event['Records'][0]['s3']['bucket']['name']
    s3key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    print(bucket)
    print(s3key)
    print(event)

    file_byte_string = s3.get_object(Bucket=bucket, Key=s3key)['Body'].read()
    pil_img = Image.open(BytesIO(file_byte_string))

    #pil_img = Image.open(r"local image")
    exif = {ExifTags.TAGS[k]: v for k, v in pil_img._getexif().items() if k in ExifTags.TAGS}

    gps_all = {}

    img_time = (exif['DateTime'])

    for key in exif['GPSInfo'].keys():

        decoded_value = ExifTags.GPSTAGS.get(key)
        gps_all[decoded_value] = exif['GPSInfo'][key]

    long_ref = gps_all.get('GPSLongitudeRef')
    lat_ref = gps_all.get('GPSLatitudeRef')
    long = gps_all.get('GPSLongitude')
    lat = gps_all.get('GPSLatitude')

    if long_ref == "W":
        long_in_degrees = -abs(convert_to_degress(long))
    else:
        long_in_degrees = convert_to_degress(long)
    if lat_ref == "S":

        lat_in_degrees = -abs(convert_to_degress(lat))
    else:
        lat_in_degrees = convert_to_degress(lat)


    connection = psycopg2.connect(user="postgres", password="xxxx",
                                  host="xxx.xxx.xxx.rds.amazonaws.com", port="5432",
                                  database="drone-imagery2")

    cursor = connection.cursor()

    postgres_insert_query = "INSERT INTO youtube_demo (name,lat,long,image_date, geom) VALUES ('{0}','{1}','{2}','{3}',ST_GeomFromText('POINT({4} {5})', 4326))".format(s3key, round(lat_in_degrees, 6), round(long_in_degrees, 6), img_time,round(long_in_degrees, 4), round(lat_in_degrees, 4))
    #postgres_insert_query = "INSERT INTO youtube_demo (name,lat,long,image_date) VALUES ('{0}','{1}','{2}','{3}')".format("test", round(lat_in_degrees, 6), round(long_in_degrees, 6), img_time)

    cursor.execute(postgres_insert_query)
    connection.commit()
    count = cursor.rowcount
    print(postgres_insert_query)
    print(count, "Record inserted successfully")
