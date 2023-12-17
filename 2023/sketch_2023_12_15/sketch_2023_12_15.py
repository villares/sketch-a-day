# Draws ways and buildings from data © OpenStreetMap contributors
import py5

from shapely import Polygon, MultiPolygon
from shapely import LineString, MultiLineString, LinearRing
from shapely import Point, MultiPoint
from shapely import GeometryCollection
from shapely.ops import transform

import osmnx as ox
ox.settings.log_console=True
ox.settings.use_cache=False

from geopandas import GeoDataFrame

bgcolor = '#343434'
edge_color = '#CCCCCC'
bldg_color = '#008888'
highlight = '#FF0000'
point = ox.geocode('Biblioteca Monteiro Lobato, São Paulo, Brasil')
dist = 200

bbox = ox.utils_geo.bbox_from_point(point, dist=dist)
fp = ox.features_from_point(point, tags={'building':True}, dist=dist)
G = ox.graph_from_point(point, network_type='walk', dist=dist, truncate_by_edge=True, retain_all=True)
nodes, edges = ox.graph_to_gdfs(G)
m_edges = edges.to_crs(epsg=3857)
m_fp = fp.to_crs(epsg=3857)
minx, miny, maxx, maxy = m_edges.total_bounds
general = m_edges[m_edges['name'].str.contains('general', case=False, na=False)]
biblioteca = m_fp[m_fp['name'].str.contains('monteiro', case=False, na=False)]

#selected_edges_gdf = gdf_meters[gdf_meters['edge_id'].isin(selected_edges)]
#paulista_length = paulista.geometry.length.sum()
#print(paulista_length)  # value seems wrong!!!

drawing_elements = []

def setup():
    py5.size(900, 900)
    scale_x = py5.width / (maxx - minx) 
    scale_y = py5.height / (maxy - miny)
    translate_x = -minx * scale_x
    translate_y = -miny * scale_y
    matrix = [scale_x, 0, 0, scale_y, translate_x, translate_y]
    drawing_elements[:] = [
     (m_edges['geometry'].affine_transform(matrix),
          edge_color, None),
     ([b for b in m_fp['geometry'].affine_transform(matrix) if b.area],
          None, bldg_color),
     (biblioteca.affine_transform(matrix),
          None, highlight),
     (general.geometry.affine_transform(matrix),
          highlight, None),
     ]

def draw():
    py5.background(bgcolor)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.scale(1.3)
    py5.stroke_weight(0.5)
    py5.translate(-py5.width * 0.45, -py5.height / 2)
    for shps, sc, fc in drawing_elements:
        if sc is None:
            py5.no_stroke()
        else:
            py5.stroke(sc)
        if fc is None:
            py5.no_fill()
        else:
            py5.fill(fc)
        draw_shapely(shps, flipped_y=True)            


def draw_shapely(shps, flipped_y=False, sketch: py5.Sketch=None):
    """
    Draw most shapely objects with py5.
    This will use the "current" py5 sketch as default.
    """
    s = sketch or py5.get_current_sketch()
    if flipped_y:
        s.push_matrix()
        s.translate(0, py5.height)
        s.scale(1, -1)    
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
        s.point(shps.x, shps.y) 
    elif isinstance(shps, MultiPoint):
        s.points((p.x, p.y) for p in shps.geoms)
    elif isinstance(shps, GeoDataFrame):
        for shp in shps.geometry:
                draw_shapely(shp)
    else:
        try:
            for shp in shps:
                draw_shapely(shp)
        except TypeError as e:
            print(f"Unable to draw: {shps}")
    if flipped_y:
        s.pop_matrix()


py5.run_sketch(block=False)

