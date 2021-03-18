import arcpy

arcpy.env.overwriteOutput = True

points = arcpy.GetParameterAsText(0)
countries = arcpy.GetParameterAsText(1)
outpath = arcpy.GetParameterAsText(2)
pop_number = arcpy.GetParameterAsText(3)

total_count = 0
created_count = 0

arcpy.MakeFeatureLayer_management(points, 'points_layer')

with arcpy.da.SearchCursor(countries, ['FID', 'SOVEREIGNT', 'POP_EST']) as country_cursor:
    for x in country_cursor:
        total_count += 1
        if x[2] > float(pop_number):

            created_count += 1
            print x[1]
            arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "FID" = {} """.format(x[0]) )
            arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
            # 2021 Update - had to replace '-' and also encode into utf-8
            formatted_output_name = x[1].replace('(', '_').replace(')', '_').replace('-', '_').encode('utf-8')
            arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpath, 'cities_in_{0}_{1}'.format(formatted_output_name, x[0]))
            print 'Successfully converted {} \n'.format(formatted_output_name)
            arcpy.AddMessage('Successfully converted {} \n'.format(formatted_output_name))

        else:
            # 2021 update - encode into utf-8
            print "{} didn't meet the criteria".format(x[1].encode('utf-8'))
            arcpy.AddMessage("{} didn't meet the criteria".format(x[1].encode('utf-8')))

print 'Finished'
arcpy.AddMessage('Finished!!!')
print '{0} met the criteria out of {1} countries'.format(created_count, total_count)
arcpy.AddMessage('{0} met the criteria out of {1} countries'.format(created_count, total_count))