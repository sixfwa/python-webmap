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

fg = folium.FeatureGroup(name = "My Map")

for lat, lon, elev in zip(latitude, longitude, elevation):
    fg.add_child(folium.CircleMarker(location = [lat, lon], radius = 6,
    popup = str(elev) + " m", fill_color = colour_producer(elev), color = 'grey', fill_opacity = 0.7,
    fill = True))
    
my_map.add_child(fg)

my_map.save("my_map.html")