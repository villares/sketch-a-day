# Draws ways and buildings from data © OpenStreetMap contributors

from shapely.affinity import affine_transform
#import matplotlib.pyplot as plt
import py5

import osmnx as ox
ox.settings.log_console=True
ox.settings.use_cache=True

bgcolor = '#343434'
edge_color = '#CCCCCC'
bldg_color = '#008888'
point = ox.geocode('Avenida Paulista, São Paulo, Brasil')
dist = 2000

bbox = ox.utils_geo.bbox_from_point(point, dist=dist)
fp = ox.features_from_point(point, tags={'building':True}, dist=dist)
G = ox.graph_from_point(point, network_type='drive', dist=dist, truncate_by_edge=True, retain_all=True)
nodes, edges = ox.graph_to_gdfs(G)
m_edges = edges.to_crs(epsg=3857)
paulista = m_edges[m_edges['name'] == 'Avenida Paulista']
#selected_edges_gdf = gdf_meters[gdf_meters['edge_id'].isin(selected_edges)]
paulista_length = paulista.geometry.length.sum()
print(paulista_lengt)
# fig, ax = ox.plot_graph(G, bgcolor=bgcolor, node_size=0, edge_color=edge_color, show=False)
# fig, ax = ox.plot_footprints(fp, ax=ax, bbox=bbox, color=bldg_color, show=False) #, save=True)
# paulista.plot(ax=ax, color='red')
# plt.show()

def setup():
    py5.size(500, 650)
    minx, miny, maxx, maxy = m_edges.bounds
    scale_x = py5.width / (maxx - minx)
    scale_y = py5.height / (maxy - miny)
    translate_x = -minx * scale_x
    translate_y = -miny * scale_y
    # trying scale_y * -1 ...
    matrix = [scale_x, 0, 0, -scale_y, translate_x, translate_y]
    m_edges['geometry'] = m_edges['geometry'].affine_transform(matrix)

