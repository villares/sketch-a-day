import py5

import osmnx as ox
from shapely import affinity

import matplotlib.pyplot as plt

# fig, ax = plt.subplots(figsize=(10, 10))
# city_boundary.plot(ax=ax, color='lightgrey', edgecolor='black') 
# plt.show()

def setup():
    global shp, polygon
    py5.size(800, 800)
    py5.stroke_join(py5.ROUND)
    py5.translate(400, 400)
    city_boundary = ox.geocode_to_gdf("São Paulo, Brazil")
    polygon = city_boundary.geometry[0]
    polygon = affinity.translate(polygon, 46, 23)
    polygon_s = affinity.scale(polygon,
                               xfact=500,
                               yfact=-500,
                               origin='center'
                               )
    polygon2 = affinity.scale(polygon,
                              xfact=500,
                              yfact=-500,
                              origin='centroid'
                              )

    py5.fill(100)
    with py5.begin_closed_shape():
        py5.vertices(polygon_s.exterior.coords)

    py5.fill(0, 0, 100)
    with py5.begin_closed_shape():
        py5.vertices(polygon2.exterior.coords)
        
    py5.fill(255, 0, 0, 100)
    py5.no_stroke()
    shp = py5.convert_shape(polygon, flip_y_axis=True)
    shp.disable_style()
    shp.scale(500)
    py5.shape_mode(py5.CENTER)
    py5.shape(shp, 0, 0) #,0, 0, 1000, 1000)
    py5.save('out.png')

py5.run_sketch(block=False)