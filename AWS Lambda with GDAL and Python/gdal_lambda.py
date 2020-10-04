import json
import urllib.parse
from osgeo import gdal

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    s3key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    print(bucket)
    print(s3key)
    print(event)
    
    gtif = gdal.Open("/vsis3/{0}/{1}".format(bucket, s3key))
    print (gtif.GetMetadata())