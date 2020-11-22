import folium
import requests

m = folium.Map(location=[37, 0], zoom_start=2.5, tiles='Stamen Terrain')


response = requests.get('https://restcountries.eu/rest/v2/all').json()
#print(response)

for country_data in response:
    #print(country_data)
    # print(country_data['name'])

    if country_data['latlng']:
        lat = country_data['latlng'][0]
        long = country_data['latlng'][1]
        print(country_data)
        folium.Marker([lat, long], popup='<i>{}</i><br><i>{}</i> '.format(country_data['name'], country_data['population']), icon=folium.Icon(icon='cloud', color='green')).add_to(m)
    else:
        continue
#
m.save("E:\pythonProject\index.html")