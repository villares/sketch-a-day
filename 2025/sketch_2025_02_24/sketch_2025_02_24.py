CT = "Poly data (c) OpenStreetMap contributors \nhttps://www.openstreetmap.org/copyright"

import py5
import osmnx as ox
import shapely

def setup():
    global city_boundary, parks_and_squares, polygon, map_h, x_min
    py5.size(1000, 1000)
    py5.translate(0, py5.height)
    py5.scale(1, -1)
    py5.stroke_join(py5.ROUND)

    city_boundary = ox.geocode_to_gdf("São Paulo, Brazil")
    polygon = city_boundary.geometry[0]
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
    x_min, y_min, x_max, y_max = city_boundary.total_bounds
    map_w, map_h = (x_max - x_min), (y_max - y_min)
    x_scale = y_scale = py5.height / map_h   
    for gdf in (city_boundary,
                parks_and_squares,
                rivers):
        translate_and_scale_gdf(gdf, -x_min, -y_min, x_scale, y_scale)

    py5.no_stroke()
    py5.fill(240)
    with py5.begin_closed_shape():
        py5.vertices(city_boundary.geometry[0].exterior.coords)

    py5.fill(0, 0, 200)
    blues = shapely.GeometryCollection(tuple(rivers.geometry))
    py5.shape(py5.convert_shape(blues))

    py5.fill(0, 128, 0, 128)
    greens = shapely.GeometryCollection(tuple(parks_and_squares.geometry))
    py5.shape(py5.convert_shape(greens))

    py5.scale(1, -1)
    py5.fill(0)
    py5.text(CT, 400, -30)

    py5.save('map.png')

def translate_and_scale_gdf(gdf, x, y, x_scale, y_scale):
    gdf['geometry'] = gdf.geometry.translate(x, y)
    gdf['geometry'] = gdf.geometry.scale(
        xfact=x_scale, yfact=y_scale, origin=(0, 0))

py5.run_sketch(block=False)

#import matplotlib.pyplot as plt
#     fig, ax = plt.subplots(figsize=(10, 10))
#     city_boundary.plot(ax=ax, color='lightgrey', edgecolor='black') 
#     parks_and_squares.plot(ax=ax, color='green') 
#     plt.show()