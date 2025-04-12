import os

import leafmap.maplibregl as leafmap # pip install leafmap[maplibre] --upgrade
#import leafmap.foliumap as leafmap  

#from villares.token_helpers import get_token
# MAPTILER_KEY = get_token('maptiler', 'MAPTILER_KEY')

m = leafmap.Map(center=[-46.6333, -23.5505], zoom=15,  pitch=45, style='liberty')
m.add_globe_control()
m.to_html('index.html')

# # And down below, mostly failed stuff I tried, commented out!
# m.add_basemap("Esri.WorldImagery", visible=False)
# source = {
#     "url": f"https://api.maptiler.com/tiles/v3/tiles.json?key={MAPTILER_KEY}",
#     "type": "vector",
# }
#m.add_source("openmaptiles", source)

# layer = {
#     "id": "3d-buildings",
#     "source": "openmaptiles",
#     "source-layer": "building",
#     "type": "fill-extrusion",
#     "min-zoom": 15,
#     "paint": {
#         "fill-extrusion-color": [
#             "interpolate",
#             ["linear"],
#             ["get", "render_height"],
#             0,
#             "lightgray",
#             200,
#             "royalblue",
#             400,
#             "lightblue",
#         ],
#         "fill-extrusion-height": [
#             "interpolate",
#             ["linear"],
#             ["zoom"],
#             15,
#             0,
#             16,
#             ["get", "render_height"],
#         ],
#         "fill-extrusion-base": [
#             "case",
#             [">=", ["get", "zoom"], 16],
#             ["get", "render_min_height"],
#             0,
#         ],
#     },
# }
# m.add_layer(layer)
# m.add_layer_control(layer.keys())
# url = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
# m.add_tile_layer(
#     url, name="OpenStreetMap", attribution="OpenStreetMap", opacity=1.0, visible=False
# )
