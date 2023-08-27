# Draws ways and buildings from data © OpenStreetMap contributors

import networkx as nx
import matplotlib.pyplot as plt

import osmnx as ox
# ox.config(log_console=True, use_cache=True) # deprecated
ox.settings.log_console=True
ox.settings.use_cache=True


bgcolor = '#343434'
edge_color = '#CCCCCC'
bldg_color = '#008888'
point = ox.geocode('Avenida Paulista, São Paulo, Brasil')
dist = 2000

bbox = ox.utils_geo.bbox_from_point(point, dist=dist)
fp = ox.features_from_point(point, tags={'building':True}, dist=dist)
G = ox.graph_from_point(point, network_type='walk', dist=dist, truncate_by_edge=True, retain_all=True)

fig, ax = ox.plot_graph(G, bgcolor=bgcolor, node_size=0, edge_color=edge_color, show=False)
fig, ax = ox.plot_footprints(fp, ax=ax, bbox=bbox, color=bldg_color) #, save=True)