# Exemplo do tutorial

import py5
import shapely
from shapely import Point, Polygon
import trimesh

import facets # https://github.com/py5coding/python-brasil-2025/blob/main/prototypes/facets.py

def setup():
    global resultado
    py5.size(500, 500, py5.P3D)
 
    poly = Polygon((
        (-200, -200),
        (200, -200),
        (150, 150),
        (0, 50),
        (-200, 200),
    ))
    poly = poly - poly.buffer(-20)
    malha = trimesh.creation.extrude_polygon(poly, 200)
    resultado = py5.convert_shape(malha,
                                  min_angle=py5.radians(30))

def draw():
    py5.background('#6440C5')
    py5.translate(py5.width / 2, py5.height / 2)
    py5.scale(0.7)
    py5.rotate_y(py5.radians(py5.mouse_x))
    py5.shape(resultado)

py5.run_sketch(block=False)

