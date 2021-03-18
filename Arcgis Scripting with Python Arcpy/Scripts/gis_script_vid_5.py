import arcpy

arcpy.env.overwriteOutput = True

points = r"E:\Files\GIS\_Tutorial\Data\ne_10m_populated_places.shp"
countries = r"E:\Files\GIS\_Tutorial\Data\ne_10m_admin_0_countries.shp"
outpath = r"E:\Files\GIS\_Tutorial\outputs"

countries_of_interest = ['United States', 'Italy', 'Kenya', 'Jordan', 'Lebanon', 'Scotland', 'France']

arcpy.MakeFeatureLayer_management(points, 'points_layer')

for x in countries_of_interest:
    print x
    arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME" = '{}' """.format(x))
    arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
    arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpath, 'cities_in_{}'.format(x))
