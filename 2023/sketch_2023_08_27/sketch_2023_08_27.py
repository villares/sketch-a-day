# Draws ways and buildings from data © OpenStreetMap contributors
import py5

from shapely import Polygon, MultiPolygon
from shapely import LineString, MultiLineString, LinearRing
from shapely import Point, MultiPoint
from shapely import GeometryCollection
from shapely.ops import transform

import osmnx as ox
ox.settings.log_console=True
ox.settings.use_cache=True

from geopandas import GeoDataFrame

bgcolor = '#343434'
edge_color = '#CCCCCC'
bldg_color = '#008888'
point = ox.geocode('Avenida Paulista, São Paulo, Brasil')
dist = 2000

bbox = ox.utils_geo.bbox_from_point(point, dist=dist)
fp = ox.features_from_point(point, tags={'building':True}, dist=dist)
G = ox.graph_from_point(point, network_type='walk', dist=dist, truncate_by_edge=True, retain_all=True)
nodes, edges = ox.graph_to_gdfs(G)
m_edges = edges.to_crs(epsg=3857)
m_fp = fp.to_crs(epsg=3857)
#m_edges = edges.set_crs('EPSG:4326').to_crs('EPSG:3857')
paulista = m_edges[m_edges['name'] == 'Avenida Paulista']
#selected_edges_gdf = gdf_meters[gdf_meters['edge_id'].isin(selected_edges)]
paulista_length = paulista.geometry.length.sum()
print(paulista_length)  # value seems wrong!!!

def setup():
    py5.size(800, 800)
    py5.background(bgcolor)
    minx, miny, maxx, maxy = m_edges.total_bounds
    scale_x = py5.width / (maxx - minx)
    scale_y = py5.height / (maxy - miny)
    translate_x = -minx * scale_x
    translate_y = -miny * scale_y
    matrix = [scale_x, 0, 0, scale_y, translate_x, translate_y]
    screen_edges = m_edges['geometry'].affine_transform(matrix).apply(flip_y)
    screen_buildings = m_fp['geometry'].affine_transform(matrix).apply(flip_y)
    screen_paulista = paulista.affine_transform(matrix).apply(flip_y)
    py5.no_stroke()
    py5.fill(bldg_color)
    draw_shapely(b for b in screen_buildings if b.area)    
    py5.stroke(edge_color)
    draw_shapely(screen_edges)
    py5.stroke(255, 0, 0)
    draw_shapely(screen_paulista)
    py5.save(f'{__file__[:-3]}.png')

def flip_y(geom):
    return transform(lambda x, y: (x, -y + py5.height), geom)
 
def draw_shapely(shps, sketch: py5.Sketch=None):
    """
    Draw most shapely objects with py5.
    This will use the "current" py5 sketch as default.
    """
    s = sketch or py5.get_current_sketch()
    if isinstance(shps, (MultiPolygon, MultiLineString, GeometryCollection)):
        for shp in shps.geoms:
            draw_shapely(shp)
    elif isinstance(shps, Polygon):
        with s.begin_closed_shape():
            s.vertices(shps.exterior.coords)
            for hole in shps.interiors:
                with s.begin_contour():
                    s.vertices(hole.coords)
    elif isinstance(shps, (LineString, LinearRing)):
        # no need to uses begin_closed_shape() because LinearRing repeats the start/end coordinates
        with s.push_style():
            s.no_fill()
            with s.begin_shape():
                s.vertices(shps.coords)
    elif isinstance(shps, Point):
        s.point(tuple(shps.coords)[0]) # yeah shps.coords for a lone Point is a CoordinateSequence.
    elif isinstance(shps, MultiPoint):
        s.points(tuple(p.coords)[0] for p in shps.geoms)
    elif isinstance(shps, GeoDataFrame):
        for shp in shps.geometry:
                draw_shapely(shp)
    else:
        try:
            for shp in shps:
                draw_shapely(shp)
        except TypeError as e:
            print(f"Unable to draw: {shps}")
        
py5.run_sketch(block=False)
