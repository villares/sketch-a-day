from itertools import product
from random import sample, seed

import py5
from shapely import Polygon

from villares.line_geometry import line_intersect, is_poly_self_intersecting
from villares.shapely_helpers import draw_shapely

def setup():
    global grid
    py5.size(800, 800, py5.P3D)
    py5.color_mode(py5.HSB)
    py5.stroke_join(py5.ROUND)
    grid = list(product(range(200, py5.width - 199, 200), repeat=2))
    py5.no_loop()

def key_pressed():
    py5.redraw()

def draw():
    py5.background(250)
    #py5.ortho()
    py5.translate(py5.width / 2, py5.height / 2)
    py5.scale(0.9)
    py5.rotate_x(py5.radians(45))
    py5.rotate_z(py5.radians(45))
    py5.translate(-py5.width / 2, -py5.height / 2)
    arrows = []
    for _ in range(10):
        path = None
        while not path or is_poly_self_intersecting(path):
            path = sample(grid, 6)
        arrow = Polygon(offset_path(path, 30))
        arrows.append(arrow.buffer(10)) # .buffer(0) cleans up Polygon
    py5.fill(255, 100)
    py5.stroke_weight(5)
    py5.stroke(0)
    py5.translate(0, 0, -150)
    for i, p in enumerate(arrows):
        py5.fill(32 + i * 24, 200, 200, 100)
        draw_shapely(p)
        py5.translate(0, 0, 40)

    py5.save_frame('###.png')

def offset_path(path, offset):
    a = calc_offset(path, offset, True)
    b = calc_offset(path[::-1], offset)
    return a + b

def calc_offset(path, offset, inside=False):
    first_seg = path[:2]  # first segment
    first_angle = py5.PI + \
        seg_angle(first_seg) if inside else seg_angle(first_seg)
    first_point = point_offset(first_seg[0], offset, first_angle)
    first_offset = seg_offset(first_seg, offset)
    # draw_seg(first_offset)
    new_path = [first_point, first_offset[0]]
    for p in path[2:]:
        #stroke(120, 120, 200)
        # draw_seg(first_offset)
        second_seg = (first_seg[1], p)
        second_offset = seg_offset(second_seg, offset)
        #stroke(120, 200, 200)
        # draw_seg(second_offset)
        half_angle = (seg_angle(first_seg) +
                      seg_angle(second_seg)) / 2 - py5.HALF_PI
        ip = line_intersect(first_offset, second_offset, in_segment=True)
        if not ip:
            ip = line_intersect(first_offset, second_offset, in_segment=False)
            new_path.append(first_offset[1])
            new_path.append(second_offset[0])
        else:
            new_path.append(ip)
        # prepare for next loop
        first_seg = second_seg
        first_offset = second_offset
    new_path.append(second_offset[1])  # final offset point
    return new_path

# def draw_seg(seg):
#     """For debugging"""
#     (xa, ya), (xb, yb) = seg
#     line(xa, ya, xb, yb)

def seg_offset(seg, offset):
    angle = seg_angle(seg) + py5.HALF_PI  # angle perpendiculat to seg
    return point_offset(
        seg[0], offset, angle), point_offset(
        seg[1], offset, angle)

def point_offset(p, offset, angle):
    return p[0] + offset * py5.cos(angle), p[1] + offset * py5.sin(angle)

def seg_angle(seg):
    (xa, ya), (xb, yb) = seg
    return py5.atan2(yb - ya, xb - xa) + py5.PI

py5.run_sketch()
