from itertools import chain

import py5
from py5 import sin, cos, TAU, sqrt
import trimesh

from shapely import Polygon, Point, unary_union

def setup():
    global mesh
    py5.size(400, 400, py5.P3D)
    xc, yc = 0, 0
    n = 6
    radius = 160
    stroke_width = 10
    depth =  10
    side = sqrt(3) / 2 * radius
    hex_points = poly_points(xc, yc, radius, n)
    hex_shp = Polygon(hex_points)
    base = trimesh.creation.extrude_polygon(hex_shp, depth)
    arcs = []
    for arc_center in hex_points:
        ring_shp = (Point(arc_center).buffer(radius  / 2 + stroke_width / 2)
                    - Point(arc_center).buffer(radius  / 2 - stroke_width / 2))
        arc_shp = hex_shp.intersection(ring_shp)
        arcs.append(arc_shp)
    arcs_union = unary_union(arcs)
    figure = trimesh.creation.extrude_polygon(arcs_union, depth)
    figure.apply_translation((0,0, depth))
    #mesh = base.union(figure, engine='blender', check_volume=False)
    mesh = trimesh.util.concatenate((figure, base))
    
def draw():
    py5.shape(py5.convert_shape(mesh))
    py5.directional_light(255, 255, 255, 0.5, 0.5, 0)
    py5.background(150)
    py5.no_fill()
    py5.stroke(255, 32)
    py5.fill(200, 200, 240)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_x(py5.mouse_y / TAU) #TAU / 6)
    py5.shape(py5.convert_cached_shape(mesh))
    
def key_pressed():
    mesh.export('teste.stl')

def poly_points(xc, yc, ra, n):
    ang = TAU / n
    return [
        (xc + ra * cos(i * ang),
         yc + ra * sin(i * ang))
        for i in range(n)]
 

py5.run_sketch(block=False)
