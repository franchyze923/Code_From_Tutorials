import arcpy

arcpy.env.overwriteOutput = True

points = r"E:\Files\GIS\_Tutorial\Data\ne_10m_populated_places.shp"
countries = r"E:\Files\GIS\_Tutorial\Data\ne_10m_admin_0_countries.shp"
outpath = r"E:\Files\GIS\_Tutorial\outputs"

with arcpy.da.SearchCursor(points, ['Name', 'POP_MAX', 'TIMEZONE']) as cities_cursor:
    for x in cities_cursor:
        print x[0]
        print x[1]
        print x[2] + '\n'
        print x