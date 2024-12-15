# Voronoy play
from itertools import product

import py5
from shapely import Polygon
from scipy.spatial import Voronoi

num_points = 200

def setup():
    py5.size(600, 600)
    py5.color_mode(py5.HSB)
    new_points()
    
def new_points():
    global seed_points, shapely_regions
    
    seed_points = []
    for i in range(2):
        seed_points.extend((x + (i - 1) * py5.random(-10, 10),
                            y + i * py5.random(-10, 10)) for x, y
                           in product(range(0, py5.width + 60, 60),
                                      range(0, py5.height+ 60, 60)))
    shapely_regions = generate_regions(seed_points, py5.width, py5.height)
    py5.stroke(255)

def generate_regions(seed_points, w, h):
    # add 4 points far from the visible region
    extended_points = seed_points.copy()
    extended_points.extend([
         (-w/2, -h/2),
         (w * 1.5, -h/2),
         (w * 1.5, h * 1.5),
         (-w/2, h * 1.5)
         ])
    voronoi = Voronoi(extended_points)
    shapely_regions = []
    for vs in voronoi.regions:
        if vs and -1 not in vs:
            shapely_regions.append(
                Polygon(voronoi.vertices[index] for index in vs if index != -1)
            )
    return shapely_regions
           
def draw():
    #py5.translate(100, 100)
    #py5.scale(400 / 600)
    for p in shapely_regions:
        #py5.no_stroke()
        #print(p.area)
        #py5.fill(py5.remap(p.area, 250, 2500, 0, 255), 200, 200)
        py5.fill(16 * len(p.exterior.coords), 200, 200)
        py5.shape(py5.convert_cached_shape(p))
    if py5.is_key_pressed:
        py5.fill(255)
        py5.no_stroke()
        for x, y in seed_points:
            py5.circle(x, y, 4)
    
def key_pressed():
    if py5.key == ' ':
        new_points()
    elif py5.key == 's':
        py5.save_frame('out###.png')
    
            
py5.run_sketch(block=False)
