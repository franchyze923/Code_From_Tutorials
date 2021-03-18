import arcpy

arcpy.env.overwriteOutput = True

points = r"E:\Files\GIS\_Tutorial\Data\ne_10m_populated_places.shp"
countries = r"E:\Files\GIS\_Tutorial\Data\ne_10m_admin_0_countries.shp"
outpath = r"E:\Files\GIS\_Tutorial\outputs"

arcpy.MakeFeatureLayer_management(points, 'points_layer')

with arcpy.da.SearchCursor(countries, ['FID', 'SOVEREIGNT']) as country_cursor:
    for x in country_cursor:
        print x[1]
        arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "FID" = {} """.format(x[0]))
        arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
        # 2021 Update - had to replace '-' and also encode into utf-8
        formatted_output_name = x[1].replace('(', '_').replace(')', '_').replace('-', '_').encode('utf-8')
        arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpath, 'cities_in_{}_{}'.format(formatted_output_name, x[0]))
        print 'Successfully Converted {} \n'.format(formatted_output_name)

print 'Finished'
