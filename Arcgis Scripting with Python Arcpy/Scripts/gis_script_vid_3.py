import arcpy

arcpy.env.workspace = r"E:\Files\GIS\_Tutorial\Data"

feature_list = arcpy.ListFeatureClasses()

print feature_list