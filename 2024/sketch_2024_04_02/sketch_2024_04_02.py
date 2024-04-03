from itertools import product
from random import sample

from shapely import Polygon, GeometryCollection


grid = list(product(range(100,701,300),
                    repeat=2))

pts = [(100, 700), (400, 700),
       (700, 100), (100, 100),
       (100, 400), (400, 400)]

def setup():
    size(800, 800)
    no_loop()
    
def draw():
    background(0, 100, 100)
    stroke_weight(3)
    no_fill()
    #pts[:] = sample(grid, 6)
    print(pts)
    polys = []
    for i in range(20):
        poly = Polygon(pts).buffer(-i * 9)
        polys.append(poly)

    shp = convert_shape(GeometryCollection(polys))
    shape(shp, 0, 0)


def key_pressed():
    save(__file__[:-2] + 'png')