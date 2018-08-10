import folium

my_map = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles = "Mapbox Bright")

fg = folium.FeatureGroup(name = "My Map")

for coordinates in [[38.2, -99.1], [39.2, -97.1]]:
    fg.add_child(folium.Marker(location = coordinates, popup= "Some Random Marker", icon = folium.Icon(color='green')))
    
my_map.add_child(fg)

my_map.save("my_map.html")