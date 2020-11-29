import folium

m = folium.Map(location=[37, 0],
           zoom_start=2.5,
           tiles='https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}',
           attr='My Data Attribution')


geojson = r"E:\pythonProject\gz_2010_us_040_00_500k\gz_2010_us_040_00_500k\gz_2010_us_040_00_500k.geojson"

g = folium.GeoJson(
    geojson,
    name='geojson'
).add_to(m)

folium.GeoJsonTooltip(fields=["NAME"]).add_to(g)


m.save("E:\pythonProject\index.html")