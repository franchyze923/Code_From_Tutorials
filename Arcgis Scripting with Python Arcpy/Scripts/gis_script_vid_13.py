import arcpy

points = r"E:\Files\GIS\_Tutorial\Data\ne_10m_populated_places.shp"

with arcpy.da.UpdateCursor(points, ['NAMEPAR']) as city_cursor:
    for x in city_cursor:
        print x[0]
        x[0]= 'WE_JUST_UPDATED_THIS'
        city_cursor.updateRow(x)
        print 'We updated this value to {}'.format(x[0])