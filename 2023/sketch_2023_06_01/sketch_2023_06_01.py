from itertools import product
from random import sample, seed
from villares.line_geometry import line_intersect, is_poly_self_intersecting
from shapely import Polygon

def setup():
    global grid
    size(650, 650)
    stroke_join(ROUND)
    no_loop()
    grid = list(product(range(125, width - 99, 200), repeat=2))

def key_pressed():
    redraw()

def draw():
    background(230)
    stroke_weight(10)
    stroke(255)
    for x, y in grid:
        point(x, y)
    path = arrow = None
    #seed(43)
    while not path or not is_poly_self_intersecting(path):
        path = sample(grid, 6)
    path.pop()
    #path.append((mouse_x, mouse_y))
    arrow = offset_path(path, 40)
    fill(255, 100)
    stroke_weight(5)
    stroke(0)
#     with begin_closed_shape():
#         for x, y in arrow:
#             vertex(x, y)
    p = Polygon(arrow).buffer(0)
    draw_shapely(p)
            

def offset_path(path, offset):
    a = calc_offset(path, offset, True)
    b = calc_offset(path[::-1], offset)
    return a + b


def calc_offset(path, offset, inside=False):
    first_seg = path[:2]  # first segment
    first_angle = PI + seg_angle(first_seg) if inside else seg_angle(first_seg)
    first_point = point_offset(first_seg[0], offset, first_angle)
    first_offset = seg_offset(first_seg, offset)
    #draw_seg(first_offset)
    new_path = [first_point, first_offset[0]]
    for p in path[2:]:
        stroke(120, 120, 200)
        #draw_seg(first_offset)
        second_seg = (first_seg[1], p)
        second_offset = seg_offset(second_seg, offset)
        stroke(120, 200, 200)
        #draw_seg(second_offset)
        half_angle = (seg_angle(first_seg) +
                      seg_angle(second_seg)) / 2 - HALF_PI
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


def draw_seg(seg):
    (xa, ya), (xb, yb) = seg
    line(xa, ya, xb, yb)


def seg_offset(seg, offset):
    angle = seg_angle(seg) + HALF_PI  # angle perpendiculat to seg
    return point_offset(
        seg[0], offset, angle), point_offset(
        seg[1], offset, angle)


def point_offset(p, offset, angle):
    return p[0] + offset * cos(angle), p[1] + offset * sin(angle)


def seg_angle(seg):
    (xa, ya), (xb, yb) = seg
    return atan2(yb - ya, xb - xa) + PI

def draw_shapely(shp):
    from shapely import Polygon, MultiPolygon
    from shapely import LineString, MultiLineString
    from shapely import Point, MultiPoint
    from py5 import begin_shape, vertex, begin_contour, end_shape
    from py5 import push_style, no_fill, point
    if isinstance(shp, MultiPolygon):
        for p in shp.geoms:
            draw_shp(p)
    elif isinstance(shp, Polygon):
        begin_shape()
        for x, y in shp.exterior.coords:
            vertex(x, y)
        for hole in shp.interiors:
            begin_contour()
            for x, y in hole.coords:
                vertex(x, y)
            end_contour()
        end_shape(CLOSE)
    elif isinstance(shp, LineString):
        with push_style():
            no_fill()
            begin_shape()
            for x, y in shp.coords:
                vertex(x, y)
            end_shape()
    else:
        print(f"Unable to draw: {shp}")