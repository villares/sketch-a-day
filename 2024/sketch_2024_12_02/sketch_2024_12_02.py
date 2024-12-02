# Voronoy play

import py5
from shapely import Polygon
from scipy.spatial import Voronoi

num_points = 20

def setup():
    global seed_points, shapely_regions
    py5.size(600, 600)
    py5.color_mode(py5.HSB)
    seed_points = [(py5.random_int(py5.width), py5.random_int(py5.height))
                   for i in range(num_points)]
    shapely_regions = generate_regions(seed_points, py5.width, py5.height)
    py5.no_loop()

def generate_regions(seed_points, w, h):
    # add 4 points far from the visible region
    extended_points = seed_points.copy()
    extended_points.extend([
         (-w * 4, -h * 4),
         (-w * 4,  h * 4),
         ( w * 4, -h * 4),
         ( w * 4,  h * 4)
         ])
    voronoi = Voronoi(extended_points)
    shapely_regions = []
    for vs in voronoi.regions:
        shapely_regions.append(
            Polygon(voronoi.vertices[index] for index in vs if -1 not in vs)
            )
    return shapely_regions
           
def draw():
    for p in shapely_regions:
        py5.fill(p.area / 500 % 255, 200, 200)
        py5.shape(py5.convert_cached_shape(p))
    py5.fill(0)
    for x, y in seed_points:
        py5.circle(x, y, 5)
    
def key_pressed():
    py5.save('out.png')
    
            
py5.run_sketch()
