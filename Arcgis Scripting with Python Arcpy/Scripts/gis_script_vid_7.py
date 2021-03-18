import arcpy

arcpy.env.overwriteOutput = True

points = r"E:\Files\GIS\_Tutorial\Data\ne_10m_populated_places.shp"
countries = r"E:\Files\GIS\_Tutorial\Data\ne_10m_admin_0_countries.shp"
outpath = r"E:\Files\GIS\_Tutorial\outputs"

arcpy.MakeFeatureLayer_management(points, 'points_layer')

with arcpy.da.SearchCursor(countries, ['FID', 'SOVEREIGNT']) as country_cursor:
    for x in country_cursor:
        print x[0]
        arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "FID" = {} """.format(x[0]))
        arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
        arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpath, 'cities_in_{}'.format(x[1]))
