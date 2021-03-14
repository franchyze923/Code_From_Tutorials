import csv
import fiona
from fiona.crs import from_epsg
from shapely.geometry import Point, mapping

with open(r"C:\Fran_Temp_Working_Files\obs_vids_temp\B21C0631.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    yourschema = {'geometry': 'Point', 'properties': {'name': 'str', 'heart_rate': 'int'}}

    with fiona.open(r"C:\Fran_Temp_Working_Files\obs_vids_temp\fiona_shapely.shp", 'w', crs=from_epsg(4326), driver='ESRI Shapefile', schema=yourschema) as output:
        for row in csv_reader:
            if row[1] == '7' and row[0] == 'Data':
                heart_rate = row[22]
                position_lat_semi_circles = row[7]
                position_long_semi_circles = row[10]

                position_lat_degrees = float(position_lat_semi_circles) * (180 / 2**31)
                position_long_degrees = float(position_long_semi_circles) * (180 / 2 ** 31)
                print(f"position_lat_degrees: {position_lat_degrees}")
                print(f"position_long_degrees: {position_long_degrees}\n")

                the_point = Point(float(position_long_degrees), float(position_lat_degrees))
                prop = {'name': "this is the name value", 'heart_rate': int(heart_rate)}
                output.write({'geometry': mapping(the_point), 'properties': prop})





