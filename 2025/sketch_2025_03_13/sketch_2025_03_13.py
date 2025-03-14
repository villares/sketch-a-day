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
    py5.color_mode(py5.HSB)
    data_path = Path('osmnx.data')
    ox.settings.log_console = True
    ox.settings.requests_timeout = 1000
    if data_path.is_file():
        print(f'loading GDFs from {data_path}')
        with open(data_path, 'rb') as f:
            geodata = pickle.load(f)
            
#         se = ox.geocode("Praça da Sé, São Paulo, SP, Brasil")            
#         graph = ox.graph_from_point(
#              se, dist=2000,
#            )
#         geodata['graph'] = graph

        gdf_nodes, gdf_edges = ox.graph_to_gdfs(
            geodata['graph'],
            nodes=True, edges=True,
            node_geometry=True,
            fill_edge_geometry=False
        )
        geodata['edges'] = gdf_edges
        
        with open(data_path, 'wb') as f:
            pickle.dump(geodata, f)            
    else:
        print(f'downloading GDFs with OSMnx.=')
        city_boundary = ox.geocode_to_gdf("São Paulo, Brazil")
        buildings = ox.features_from_point(
            se, dist=2000, tags={
                'building': True,
                })
        graph = ox.graph_from_point(
             se, dist=2000
             )
        gdf_nodes, gdf_edges = ox.graph_to_gdfs(
            graph,
            nodes=True, edges=True,
            node_geometry=True,
            fill_edge_geometry=False
        )        
        geodata = {
            'boundary': city_boundary,
            'buildings': buildings,
            'graph': graph,
            'edges': gdf_edges,
            }  
        with open(data_path, 'wb') as f:
            pickle.dump(geodata, f)

    x_min, y_min, x_max, y_max = geodata['buildings'].total_bounds
    map_w, map_h = (x_max - x_min), (y_max - y_min)
    x_scale = y_scale = py5.height / map_h
    main_shp = py5.create_shape(py5.GROUP)
    #boundary = geodata['boundary']
    #translate_and_scale_gdf(boundary, -x_min, -y_min, x_scale, -y_scale)
    #shps = shapely.GeometryCollection(tuple(boundary.geometry))
    #main_shp.add_child(py5.convert_shape(shps))
    # Walk
    edges = geodata['edges']
    translate_and_scale_gdf(edges, -x_min, -y_min, x_scale, -y_scale)
    shps = shapely.GeometryCollection(tuple(edges.geometry))
    py5.stroke(255)
    py5.stroke_weight(2 / x_scale)
    main_shp.add_child(py5.convert_shape(shps))
    # Buildings
    buildings = geodata['buildings']
    amenity_names = list(set(a for a in buildings.amenity if str(a) != 'nan'))
    am_color = {a: py5.color(i * (255 / len(amenity_names)), 200, 200)
                for i, a in enumerate(amenity_names)}
    translate_and_scale_gdf(buildings, -x_min, -y_min, x_scale, -y_scale)    
    py5.no_stroke()
    for g, a in zip(buildings.geometry, buildings.amenity):
        if c := am_color.get(a):
            py5.fill(c)
        else:
            py5.fill(200)
        main_shp.add_child(py5.convert_shape(g))
 
 
 
def draw():
    py5.background(100)
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
