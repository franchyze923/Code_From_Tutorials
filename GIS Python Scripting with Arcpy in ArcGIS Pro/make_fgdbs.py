import arcpy
import os
import time

start_time = time.time()
# where you want the fgdbs to go
working_directory = r"E:\Youtube_Videos\fgdb"

for fgdb in range(5):
    fgdb_full_path = os.path.join(working_directory, f"fgdb_{fgdb}.gdb")

    print(f"Creating {fgdb_full_path}")
    arcpy.management.CreateFileGDB(working_directory, f"fgdb_{fgdb}", "CURRENT")

    print(f"Creating feature class in {fgdb_full_path}")
    arcpy.management.CreateFeatureclass(fgdb_full_path, "fc_1", "POINT", None, "DISABLED", "DISABLED", None, '', 0, 0, 0, '')

    print(f"Importing cities shapefile in {fgdb_full_path}\n")
    arcpy.FeatureClassToFeatureClass_conversion(r"C:\Users\Fran\Downloads\ne_10m_populated_places (2)\ne_10m_populated_places.shp", fgdb_full_path, "world_cities")

print(f"Process Complete. Took --- {time.time() - start_time} seconds ---")
