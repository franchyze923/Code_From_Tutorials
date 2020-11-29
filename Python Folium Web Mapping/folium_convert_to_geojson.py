from osgeo import gdal
import folium
import os


def shapefile2geojson(infile, outfile):

    options = gdal.VectorTranslateOptions(format="GeoJSON", dstSRS="EPSG:4326")
    gdal.VectorTranslate(outfile, infile, options=options)


infile = input("Copy/Paste the location of your shapefile: ").strip('"')
output_geojson = os.path.splitext(infile)[0] + ".geojson"

shapefile2geojson(infile, output_geojson)


m = folium.Map(location=[37, 0],
           zoom_start=2.5,
           tiles='https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}',
           attr='My Data Attribution')


g = folium.GeoJson(
    output_geojson,
    name='geojson'
).add_to(m)

folium.GeoJsonTooltip(fields=["NAME"]).add_to(g)


m.save("E:\pythonProject\index_2.html")