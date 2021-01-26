import arcpy

coords = [('VIRGINIA', (-78.144527, 38.582526)), ('CALIFORNIA', (-121.747833, 38.410558)), ('SOUTH AMERICA', (-59.825562, -7.710992)), ('India', (72.023570, 22.755921))]

new_shape_file = arcpy.CreateFeatureclass_management(r"C:\Fran_Temp_Working_Files\arc", "TEST_143.shp", "POINT", spatial_reference=4326)
print(new_shape_file)
arcpy.AddField_management(new_shape_file, "NAME", "TEXT")

with arcpy.da.InsertCursor(new_shape_file, ['NAME', 'SHAPE@XY']) as insert_cursor:
    for coord in coords:
        print("Inserted {} into {}".format(coord, new_shape_file))
        insert_cursor.insertRow(coord)