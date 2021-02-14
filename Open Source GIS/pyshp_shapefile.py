import csv
import shapefile

with open(r"C:\Fran_Temp_Working_Files\obs_vids_temp\B21C0631.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    with shapefile.Writer(r"C:\Fran_Temp_Working_Files\garmin_fit\pyshp_demo\new_file") as w:
        w.field('HeartRate', 'C')

        for row in csv_reader:
            if row[1] == '7' and row[0] == 'Data':
                heart_rate = row[22]
                position_lat_semi_circles = row[7]
                position_long_semi_circles = row[10]

                position_lat_degrees = float(position_lat_semi_circles) * (180 / 2**31)
                position_long_degrees = float(position_long_semi_circles) * (180 / 2 ** 31)
                print(f"position_lat_degrees: {position_lat_degrees}")
                print(f"position_long_degrees: {position_long_degrees}\n")
                w.point(position_long_degrees, position_lat_degrees)
                w.record(heart_rate)


with open(r"C:\Fran_Temp_Working_Files\garmin_fit\pyshp_demo\new_file.prj", "w") as text_file:
    epsg = 'GEOGCS["WGS 84",'
    epsg += 'DATUM["WGS_1984",'
    epsg += 'SPHEROID["WGS 84",6378137,298.257223563]]'
    epsg += ',PRIMEM["Greenwich",0],'
    epsg += 'UNIT["degree",0.0174532925199433]]'

    print(epsg, file=text_file)
