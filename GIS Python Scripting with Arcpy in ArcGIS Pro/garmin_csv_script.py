import csv
import arcpy

new_shape_file = arcpy.CreateFeatureclass_management(r"C:\Fran_Temp_Working_Files\garmin_fit", "garmin_shapefile_1.shp", "POINT", spatial_reference=4326)
arcpy.AddField_management(new_shape_file, "HEARTRATE", "TEXT")

with open(r"C:\Fran_Temp_Working_Files\garmin_fit\B21D3144.csv") as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')

    coords_list = []

    for row in csv_reader:
        if row[1] == '7' and row[0] == 'Data':
            heart_rate = row[22]
            position_lat_semi_circles = row[7]
            position_long_semi_circles = row[10]

            position_lat_degrees = float(position_lat_semi_circles) * (180 / 2**31)
            position_long_degrees = float(position_long_semi_circles) * (180 / 2 ** 31)
            print(f"position_lat_degrees: {position_lat_degrees}")
            print(f"position_long_degrees: {position_long_degrees}\n")
            coords_list.append((heart_rate, (position_long_degrees, position_lat_degrees))       )

print(coords_list)

with arcpy.da.InsertCursor(new_shape_file, ["HEARTRATE", 'SHAPE@XY']) as insert_cursor:
    for coord in coords_list:
        print("Inserted {} into {}".format(coord, new_shape_file))
        insert_cursor.insertRow(coord)

arcpy.management.AddXY(new_shape_file)