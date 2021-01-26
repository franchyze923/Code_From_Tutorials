import arcpy

coords = [(-78.144527, 38.582526), (-121.747833, 38.410558),  (-59.825562, -7.710992), (72.023570, 22.755921)]

new_shape_file = arcpy.CreateFeatureclass_management(r"C:\Fran_Temp_Working_Files\arc", "TEST_142.shp", "POINT", spatial_reference=4326)
print(new_shape_file)

with arcpy.da.InsertCursor(new_shape_file, ['SHAPE@XY']) as insert_cursor:
    for coord in coords:
        print("Inserted {} into {}".format(coord, new_shape_file))
        insert_cursor.insertRow([coord])