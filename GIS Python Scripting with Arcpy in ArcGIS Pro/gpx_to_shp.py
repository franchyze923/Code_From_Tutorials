import os
import arcpy


gpx_directory_path = r"C:\Users\Fran\Downloads\export_22552451\activities"

gpx_list = os.listdir(gpx_directory_path)


for gpx_file in gpx_list:
    if gpx_file.endswith(".gpx"):
        full_gpx_path = os.path.join(gpx_directory_path, gpx_file)
        print(f"Converting {full_gpx_path} to shapefile")
        output_shapefile = os.path.splitext(full_gpx_path)[0] + ".shp"
        try:
            arcpy.GPXtoFeatures_conversion(full_gpx_path, output_shapefile)
            print(f"Finished Converting {full_gpx_path} to shapefile \n")
        except Exception as e:
            print("failed to convert")
            print(e)

print("Finished converting all gpx to shp")
