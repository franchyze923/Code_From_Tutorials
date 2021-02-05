## in order to use python from qgis in pycharm need to set interpreter to "C:\OSGeo4W64\bin\python-qgis.bat"
## https://pcjericks.github.io/py-gdalogr-cookbook/vector_layers.html#create-a-new-shapefile-and-add-data
## https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry

import csv
import osgeo.ogr as ogr
import osgeo.osr as osr

driver = ogr.GetDriverByName("ESRI Shapefile")
data_source = driver.CreateDataSource(r"E:\garmin_points.shp")
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)

# create the layer
layer = data_source.CreateLayer("garmin_points", srs, ogr.wkbPoint)

# Add the fields we're interested in
field_name = ogr.FieldDefn("Heartrate", ogr.OFTString)
field_name.SetWidth(24)
layer.CreateField(field_name)
layer.CreateField(ogr.FieldDefn("Latitude", ogr.OFTReal))
layer.CreateField(ogr.FieldDefn("Longitude", ogr.OFTReal))

# Save and close the data source

with open(r"C:\Fran_Temp_Working_Files\obs_vids_temp\B21C0631.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        if row[1] == '7' and row[0] == 'Data':
            heart_rate = row[22]
            position_lat_semi_circles = row[7]
            position_long_semi_circles = row[10]

            position_lat_degrees = float(position_lat_semi_circles) * (180 / 2**31)
            position_long_degrees = float(position_long_semi_circles) * (180 / 2 ** 31)
            print(f"position_lat_degrees: {position_lat_degrees}")
            print(f"position_long_degrees: {position_long_degrees}\n")

            # create the feature
            feature = ogr.Feature(layer.GetLayerDefn())
            # Set the attributes using the values from the delimited text file
            feature.SetField("Heartrate", heart_rate)
            feature.SetField("Latitude", position_lat_degrees)
            feature.SetField("Longitude", position_long_degrees)

            # create the WKT for the feature using Python string formatting
            wkt = f"POINT({position_long_degrees} {position_lat_degrees})"
            print("wkt: {}".format(wkt))

            # Create the point from the Well Known Txt
            point = ogr.CreateGeometryFromWkt(wkt)
            feature.SetGeometry(point)
            layer.CreateFeature(feature)

            feature = None
    data_source = None


