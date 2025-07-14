import folium
import osmnx as ox
import webbrowser
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="mapeador")
addresses = [
    'Av. Angélica, São Paulo, Brazil',
    'Sesc Av. Paulista, São Paulo, Brazil',
    'Av. Ipiranga 200, São Paulo, Brazil',
]
geocoded_addresses = {}
for address in addresses:
    result = geolocator.geocode(address)
    if result:
        geocoded_addresses[address] = result.latitude, result.longitude
    else:
        print(f'Could not geocode: {address}')
if not geocoded_addresses:
    print('No valid addresses')
    exit()
    
center_point = list(geocoded_addresses.values())[0]
m = folium.Map(location=center_point, zoom_start=15)
# Add markers
for address, coords in geocoded_addresses.items():
    folium.Marker(location=coords, popup=address).add_to(m)
    
# Save the map as an HTML file
filename = "map.html"
m.save(filename)
webbrowser.open(filename)
