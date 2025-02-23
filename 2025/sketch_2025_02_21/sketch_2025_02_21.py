import py5
import numpy as np
import osmnx as ox
import geopandas as gpd

from shapely.geometry import Point, LineString, GeometryCollection
from shapely.geometry import GeometryCollection
from shapely.affinity import scale, translate

from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

import matplotlib.pyplot as plt

# random points
points = [
    (-23.5505, -46.6333),  
    (-23.564, -46.654),    
    (-23.573, -46.641),   
    (-23.532, -46.635),   
    (-23.558, -46.675),     
    (-23.551, -46.654),  
    (-23.563, -46.6333),    
    (-23.574, -46.665),   
    (-23.532, -46.651),   
    (-23.558, -46.645) ,    
    (-23.557, -46.664),  
    (-23.531, -46.623),    
    (-23.563, -46.631),   
    (-23.550, -46.635),
]
geometry = [Point(lon, lat) for lat, lon in points]
gdf_points = gpd.GeoDataFrame(geometry=geometry, crs="EPSG:4326")
city_boundary = ox.geocode_to_gdf("São Paulo, Brazil")

coords = np.array(points)
dist_matrix = distance_matrix(coords, coords)
mst = minimum_spanning_tree(dist_matrix).toarray()

edges = []
for i in range(len(mst)):
    for j in range(len(mst)):
        if mst[i][j] > 0:
            edges.append((i, j))

edge_lines = []
for start, end in edges:
    line = LineString([Point(coords[start][1], coords[start][0]), Point(coords[end][1], coords[end][0])])
    edge_lines.append(line)

gdf_edges = gpd.GeoDataFrame(geometry=edge_lines, crs="EPSG:4326")

# Change CRS to a projected CRS (e.g., Web Mercator)
gdf_edges = gdf_edges.to_crs(epsg=3857)  # Web Mercator for meters
gdf_points = gdf_points.to_crs(epsg=3857)
city_boundary = city_boundary.to_crs(epsg=3857)

def get_parks_and_squares(points):
    min_lon, min_lat = np.min(points, axis=0)[1], np.min(points, axis=0)[0]
    max_lon, max_lat = np.max(points, axis=0)[1], np.max(points, axis=0)[0]
    bbox = (min_lon, min_lat, max_lon, max_lat)
    tags = {'leisure': 'park', 'landuse': 'park', 'amenity': 'square'}
    parks_squares = ox.features_from_bbox(bbox=bbox, tags=tags).to_crs(epsg=3857)    
    return parks_squares

parks_squares = get_parks_and_squares(points)

fig, ax = plt.subplots(figsize=(10, 10))
city_boundary.plot(ax=ax, color='lightgrey', edgecolor='black')
gdf_points.plot(ax=ax, color='red', markersize=100, label='Random Points')
gdf_edges.plot(ax=ax, color='black', linewidth=2, label='MST Edges')
parks_squares.plot(ax=ax, color='green', alpha=0.5)

plt.show()