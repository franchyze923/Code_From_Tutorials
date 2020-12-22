import arcpy

working_directory = r"E:\Youtube_Videos\fgdb"
input_csv_file = r"E:\Youtube_Videos\arcpy\weather_stations.csv"

file_gdb_path = arcpy.management.CreateFileGDB(working_directory, f"fgdb_1", "CURRENT")
print(file_gdb_path)
new_feature_class = arcpy.management.XYTableToPoint(input_csv_file, fr"{file_gdb_path}\new_feature_class", "longitude", "Latitude", None, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision")

print(new_feature_class)

arcpy.AddField_management(new_feature_class, "temperature__F", "DOUBLE")
print("added new field")

arcpy.management.CalculateField(new_feature_class, "temperature__F", "(!temperature__C! * 9/5) + 32", "PYTHON3", '', "TEXT")

print("finished everything")
