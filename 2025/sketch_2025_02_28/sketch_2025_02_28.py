CT = "Poly data (c) OpenStreetMap contributors \nhttps://www.openstreetmap.org/copyright"

import pickle
from pathlib import Path

import py5
import osmnx as ox
import shapely

x_off = 0
y_off = 0
zoom = 1

def setup():
    global main_shp, geodata, graph
    py5.size(1000, 1000)
    py5.stroke_join(py5.ROUND)
    data_path = Path('osmnx.data')
    ox.settings.log_console = True
    ox.settings.requests_timeout = 1000
    
    if data_path.is_file():
        print(f'loading GDFs from {data_path}')
        with open(data_path, 'rb') as f:
            geodata = pickle.load(f)
    else:
        print(f'downloading GDFs with OSMnx.=')
        city_boundary = ox.geocode_to_gdf("São Paulo, Brazil")
        se = ox.geocode("Praça da Sé, São Paulo, SP, Brasil")
        parks_and_squares = ox.features_from_place(
            "São Paulo, Brazil", tags={
                'leisure': 'park',
                'landuse': 'park',
                'amenity': 'square',
                })
        rivers = ox.features_from_place(
            "São Paulo, Brazil", tags={
                'water': True,
                })
        buildings = ox.features_from_point(
            se, dist=2000, tags={
                'building': True,
                })
        graph = ox.graph_from_place(
             "São Paulo, Brazil"
            )
                
        geodata = {
            'boundary': city_boundary,
            'parks': parks_and_squares,
            'rivers': rivers,
            'buildngs': buildings,
            'graph': graph,
            }  
                gdf_nodes, gdf_edges = ox.graph_to_gdfs(
            geodata['graph'],
            nodes=True, edges=True,
            node_geometry=True,
            fill_edge_geometry=False
        )
        geodata['edges'] = gdf_edges

        with open(data_path, 'wb') as f:
            pickle.dump(geodata, f)

    x_min, y_min, x_max, y_max = geodata['boundary'].total_bounds
    map_w, map_h = (x_max - x_min), (y_max - y_min)
    x_scale = y_scale = py5.height / map_h
    main_shp = py5.create_shape(py5.GROUP)
    for gdf, fill_color, stroke_color, in (
        (geodata['boundary'], 100, 'white'),
        (geodata['rivers'], 'blue', None),
        (geodata['parks'], py5.color(0, 100, 0, 128), None),
        (geodata['buildngs'], 200, 0),
        (geodata['edges'], None, 255),
        ):
        translate_and_scale_gdf(gdf, -x_min, -y_min, x_scale, -y_scale)
        if fill_color is None:
            py5.no_fill()
        else:
            py5.fill(fill_color)
        if stroke_color is None:
            py5.no_stroke()
        else:
            py5.stroke(stroke_color)
            py5.stroke_weight(0.001)
        shps = shapely.GeometryCollection(tuple(gdf.geometry))
        main_shp.add_child(py5.convert_shape(shps))

def draw():
    py5.background(200)
    with py5.push_matrix():
        py5.scale(zoom)
        
        py5.shape(main_shp, x_off, py5.height + y_off)

    py5.fill(255)
    py5.text(CT, 400, py5.height-30)

def key_pressed():
    py5.save('map.png')

def translate_and_scale_gdf(gdf, x, y, x_scale, y_scale):
    gdf['geometry'] = gdf.geometry.translate(x, y)
    gdf['geometry'] = gdf.geometry.scale(
        xfact=x_scale, yfact=y_scale, origin=(0, 0))

def mouse_dragged():
    global x_off, y_off
    x_off += py5.mouse_x - py5.pmouse_x
    y_off += py5.mouse_y - py5.pmouse_y

def mouse_wheel(e):
    global zoom
    zoom += e.get_count() / 10

py5.run_sketch(block=False)
