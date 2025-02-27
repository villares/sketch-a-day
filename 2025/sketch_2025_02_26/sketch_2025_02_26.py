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
    global main_shp
    py5.size(1000, 1000)
    py5.no_stroke()
    data_path = Path('osmnx.data')
    ox.settings.log_console = True
    
    if data_path.is_file():
        with open(data_path, 'rb') as f:
            city_boundary, parks_and_squares, rivers, buildings = (
                pickle.load(f))
    else:
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
        with open(data_path, 'wb') as f:
            pickle.dump((city_boundary,
                         parks_and_squares,
                         rivers,
                         buildings
                         ), f)

    x_min, y_min, x_max, y_max = city_boundary.total_bounds
    map_w, map_h = (x_max - x_min), (y_max - y_min)
    x_scale = y_scale = py5.height / map_h
    main_shp = py5.create_shape(py5.GROUP)
    for gdf, fill_color in ((city_boundary, 'white'),
                            (rivers, 'blue'),
                            (parks_and_squares, py5.color(0, 128, 0, 128)),
                            (buildings, 100),
                            ):
        translate_and_scale_gdf(gdf, -x_min, -y_min, x_scale, -y_scale)
        py5.fill(fill_color)
        shps = shapely.GeometryCollection(tuple(gdf.geometry))
        main_shp.add_child(py5.convert_shape(shps))

def draw():
    py5.background(200)
    with py5.push_matrix():
        py5.scale(zoom)
        py5.shape(main_shp, x_off, py5.height + y_off)

    py5.fill(200, 0, 200)
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

#import matplotlib.pyplot as plt
#     fig, ax = plt.subplots(figsize=(10, 10))
#     city_boundary.plot(ax=ax, color='lightgrey', edgecolor='black') 
#     parks_and_squares.plot(ax=ax, color='green') 
#     plt.show()