import folium
import pandas as pd

data = pd.read_csv("Volcanoes_USA.txt")

latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])

def colour_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

my_map = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles = "Mapbox Bright")

fgv = folium.FeatureGroup(name = "Volcanoes")

for lat, lon, elev in zip(latitude, longitude, elevation):
    fgv.add_child(folium.CircleMarker(location = [lat, lon], radius = 6,
    popup = str(elev) + " m", fill_color = colour_producer(elev), color = 'grey', fill_opacity = 0.7,
    fill = True))

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), 
            style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange'
            if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



my_map.add_child(fgv)
my_map.add_child(fgp)
my_map.add_child(folium.LayerControl())
my_map.save("my_map.html")