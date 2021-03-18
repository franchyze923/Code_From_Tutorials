import arcpy

points = r"E:\Files\GIS\_Tutorial\Data\ne_10m_populated_places.shp"
countries = r"E:\Files\GIS\_Tutorial\Data\ne_10m_admin_0_countries.shp"
outpath = r"E:\Files\GIS\_Tutorial\outputs"

arcpy.MakeFeatureLayer_management(points, 'points_layer')
# In  2021, the United States "Name" value has changed from 'United States' to 'United States of America'
arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME" = 'United States of America' """)

arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpath, 'cities_in_us')

