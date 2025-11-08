CT = "Poly data (c) OpenStreetMap contributors \nhttps://www.openstreetmap.org/copyright"

import pickle
from pathlib import Path

from math  import isnan

import py5
import osmnx as ox
import shapely


zpt = {'x': 0, 'y': 1000, 'scale': 1, 'amount': 0}  # zoom & pan transformation values
black = py5.color(0)
DIST = 1500


def setup():
    global main_shp, geodata, graph, parks
    py5.size(1000, 1000)
    py5.stroke_join(py5.ROUND)
    py5.color_mode(py5.HSB)
    data_path = Path('osmnx.data')
    ox.settings.log_console = True
    ox.settings.requests_timeout = 10000
    se = ox.geocode("Praça da República, São Paulo, SP, Brasil")  
    if data_path.is_file():
        print(f'loading GDFs from {data_path}')
                
        with open(data_path, 'rb') as f:
            geodata = pickle.load(f)
            
        building = ox.features_from_place(
            "São Paulo, Brazil", tags={
                'amenity': True,
                'building': True,
                })
        geodata['buildings'] = buildings
        with open(data_path, 'wb') as f:
            pickle.dump(geodata, f)
    else:
        print(f'downloading GDFs with OSMnx.=')
        city_boundary = ox.geocode_to_gdf("São Paulo, Brazil")
        parks = ox.features_from_polygon(
            city_boundary.geometry[0],
            tags={
                'leisure': 'park',
                'landuse': 'grass'
                }
            )
        graph = ox.graph_from_polygon(
             city_boundary.geometry[0], network_type='walk',
             )
        gdf_nodes, gdf_edges = ox.graph_to_gdfs(
            graph,
            nodes=True, edges=True,
            node_geometry=True,
            fill_edge_geometry=False
        )
        
        rivers = ox.features_from_place(
            "São Paulo, Brazil", tags={
                'water': True,
                })
        building = ox.features_from_place(
            "São Paulo, Brazil", tags={
                'amenity': True,
                'building': True,
                })
        
        geodata = {
            'boundary': city_boundary,
            'parks': parks,
            'graph': graph,
            'edges': gdf_edges,
            'rivers': rivers,
            'buildings': buildings,
            }  
        with open(data_path, 'wb') as f:
            pickle.dump(geodata, f)

    x_min, y_min, x_max, y_max = geodata['boundary'].total_bounds
    map_w, map_h = (x_max - x_min), (y_max - y_min)
    x_scale = y_scale = py5.height / map_h
    main_shp = py5.create_shape(py5.GROUP)
    boundary = geodata['boundary']
    translate_and_scale_gdf(boundary, -x_min, -y_min, x_scale, -y_scale)
    shps = shapely.GeometryCollection(tuple(boundary.geometry))
    main_shp.add_child(py5.convert_shape(shps))
    
    py5.color_mode(py5.RGB)
    py5.stroke_weight(0.01)

    # parks
    parks = geodata['parks']
    translate_and_scale_gdf(parks, -x_min, -y_min, x_scale, -y_scale)    
    for g, lu in zip(parks.geometry, parks.landuse):
        if lu in ('recreation_ground' , 'grass'):
            py5.fill(0, 100, 0)
        else:
            py5.fill(100)
            py5.stroke(0)
        main_shp.add_child(py5.convert_shape(g))   
    # water
    rivers = geodata['rivers']
    translate_and_scale_gdf(rivers, -x_min, -y_min, x_scale, -y_scale)    
    for g in rivers.geometry:
        py5.fill(0, 0, 100)
        py5.no_stroke()
        main_shp.add_child(py5.convert_shape(g))
        
    # b
    buildings = geodata['buildings']
    translate_and_scale_gdf(buildings, -x_min, -y_min, x_scale, -y_scale)    
    for g in rivers.geometry:
        py5.fill(200)
        py5.no_stroke()
        main_shp.add_child(py5.convert_shape(g))
    # Walk
    edges = geodata['edges']
    translate_and_scale_gdf(edges, -x_min, -y_min, x_scale, -y_scale)
    shps = shapely.GeometryCollection(tuple(edges.geometry))
    py5.stroke(0)
    main_shp.add_child(py5.convert_shape(shps))

def draw():
    py5.background(150)
    with py5.push_matrix():
        py5.translate(zpt['x'], zpt['y'])
        py5.scale(zpt['scale'])
        main_shp.set_stroke_weight(1 / zpt['scale'])
        py5.shape(main_shp)
    py5.fill(255)
    py5.text(CT, 400, py5.height-30)


def key_pressed():
    py5.save('map.png')

def translate_and_scale_gdf(gdf, x, y, x_scale, y_scale):
    gdf['geometry'] = gdf.geometry.translate(x, y)
    gdf['geometry'] = gdf.geometry.scale(
        xfact=x_scale, yfact=y_scale, origin=(0, 0))

def mouse_wheel(e):
    xrd = (py5.mouse_x - zpt['x']) / zpt['scale']
    yrd = (py5.mouse_y - zpt['y']) / zpt['scale']
    zpt['amount'] -= e.get_count()
    zpt['scale'] = 1.1 ** zpt['amount']
    zpt['x'] = int(py5.mouse_x - xrd * zpt['scale'])
    zpt['y'] = int(py5.mouse_y - yrd * zpt['scale'])

def mouse_dragged():
    zpt['x'] += py5.mouse_x - py5.pmouse_x
    zpt['y'] += py5.mouse_y - py5.pmouse_y

py5.run_sketch(block=False)
