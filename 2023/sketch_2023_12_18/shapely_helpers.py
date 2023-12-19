# -*- coding: UTF-8 -*-
"""
From https://github.com/villares/villares/blob/main/shapely_helpers.py

Helpers to use shapely with py5

2023-07-31 Getting started with the drawing function.
2023-08-28 Testing for iterables last is less costly. Added GeoDataFrame case. Improved Point(s)
2023-10-09 Added polys_from_text() and its dependency process_glyphs
"""

from shapely import Polygon, MultiPolygon
from shapely import LineString, MultiLineString, LinearRing
from shapely import Point, MultiPoint
from shapely import GeometryCollection

try:
    from geopandas import GeoDataFrame
    geodataframe_imported = True
except ImportError:
    geodataframe_imported = False

import py5

def draw_shapely(shps, sketch: py5.Sketch=None):
    """
    Draw most shapely objects with py5.
    This will use the "current" py5 sketch as default.
    """
    s = sketch or py5.get_current_sketch()
    if isinstance(shps, (MultiPolygon, MultiLineString, GeometryCollection)):
        for shp in shps.geoms:
            draw_shapely(shp)
    elif isinstance(shps, Polygon):
        with s.begin_closed_shape():
            s.vertices(shps.exterior.coords)
            for hole in shps.interiors:
                with s.begin_contour():
                    s.vertices(hole.coords)
    elif isinstance(shps, (LineString, LinearRing)):
        # no need to uses begin_closed_shape() because LinearRing repeats the start/end coordinates
        with s.push_style():
            s.no_fill()
            with s.begin_shape():
                s.vertices(shps.coords)
    elif isinstance(shps, Point):
        s.point(shps.x, shps.y) 
    elif isinstance(shps, MultiPoint):
        s.points((p.x, p.y) for p in shps.geoms)
    elif geodataframe_imported and isinstance(shps, GeoDataFrame):
        for shp in shps.geometry:
                draw_shapely(shp)
    else:
        try:
            for shp in shps:
                draw_shapely(shp)
        except TypeError as e:
            print(f"Unable to draw: {shps}")
            
draw_shapely_objs = draw_shapely  # para retro-compatibilidade

def polys_from_text(words, font: py5.Py5Font, leading=None, alternate_spacing=False):
    """
    Produce a list of shapely Polygons (with holes!) from a string.
    New-line chars will try to move text to a new line.
    
    The alternate_spacing option will pick the glyph
    spacing from py5.text_width() for each glyph, it can be
    too spaced, but good for monospaced font alignment.
    """
    leading = leading or font.get_size()
    py5.text_font(font)
    space_width = py5.text_width(' ')
    results = []
    x_offset = y_offset = 0
    for c in words:
        if c == '\n':
            y_offset += leading
            x_offset = 0  # assuming left aligned text...
            continue
        glyph_pt_lists = [[]]
        c_shp = font.get_shape(c, 1)
        vs3 = [c_shp.get_vertex(i) for i in range(c_shp.get_vertex_count())]
        vs = set()
        for vx, vy, _ in vs3:
            x = vx + x_offset
            y = vy + y_offset
            glyph_pt_lists[-1].append((x, y))
            if (x, y) not in vs:
                vs.add((x, y))
            else:
                glyph_pt_lists.append([])  # will leave a trailling empty list
        
        if alternate_spacing:
            w = py5.text_width(c)
        else:
            w = c_shp.get_width() if vs3 else space_width
        x_offset += w
        # filter out elements with less than 3 points 
        # and stop before the trailling empty list
        glyph_polys = [Polygon(p) for p in glyph_pt_lists[:-1] if len(p) > 2]
        if glyph_polys:  # there are still empty glyphs at this point
            glyph_shapes = process_glyphs(glyph_polys)
            results.extend(glyph_shapes)
    return results


def process_glyphs(polys):
    """
    Try to subtract the shapely Polygons representing a glyph
    in order to produce appropriate looking glyphs!
    """
    polys = sorted(polys, key=lambda p: p.area, reverse=True)
    results = [polys[0]]
    for p in polys[1:]:
        # works on edge cases like â and ®
        for i, earlier in enumerate(results):
            if earlier.contains(p):
                results[i] = results[i].difference(p)
                break
        else:   # the for-loop's else only executes after unbroken loops
            results.append(p)
    return results

if __name__ == '__main__':
    def setup():
        py5.size(800, 800)
        py5.color_mode(py5.HSB)

        #py5.stroke_weight(10)
        #mp = MultiPoint([(200, 200), (100, 100), (200, 300)])
        #draw_shapely(mp)

        t = 'Oi B008!\né o gnumundo®...\n' \
            'viva a ciberlândia!\n' \
            '◍◴❂⦲జ్ఞ‌ా'
      
        d_font = py5.create_font('SansSerif', 60)
        i_font = py5.create_font('Open Sans', 60)

        shapes = polys_from_text(
            t, d_font, alternate_spacing=True)

        for i, shp in enumerate(shapes):
            py5.fill((i * 8) % 256, 255, 255, 100)
            draw_shapely(shp)

        shapes = polys_from_text(
            t, i_font, alternate_spacing=False)

        py5.translate(0, 400)

        for i, shp in enumerate(shapes):
            py5.fill((i * 8) % 256, 255, 255, 100)
            draw_shapely(shp)

        py5.translate(100, 100)

    py5.run_sketch(block=False)

'''
# Maybe I'll pick some ideas/functions from line_geometry.py and reimplement with shapely

def line_intersect(*args, **kwargs):
    """
    Adapted from Bernardo Fontes https://github.com/berinhard/sketches/
    2020-11-14 Does not assume Line objects anymore, and works with 4 points or 8 coords.
    2021_09_26 Adding intersection outside the segments. Also fixing bug when calling with 8 coords as arguments.
    2021_09_26 Removed line_a & line_b variables, rewrote ZeroDivision exception catching as a conditional check.
    """
    as_PVector = kwargs.get('as_PVector', False)
    in_segment = kwargs.get('in_segment', True)
    
    if len(args) == 2:  # expecting 2 Line objects or 2 tuples of 2 point tuples.
        (x1, y1), (x2, y2) = args[0]
        (x3, y3), (x4, y4) = args[1]
    elif len(args) == 4:
        (x1, y1), (x2, y2) = args[:2]
        (x3, y3), (x4, y4) = args[2:]
    elif len(args) == 8:
        x1, y1, x2, y2, x3, y3, x4, y4 = args
    else:
        raise ValueError("line_intersect requires 2 lines, 4 points or 8 coords.")
            
    divisor = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if divisor:
        uA = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / divisor
        uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / divisor
    else:
        return None
    if not in_segment or 0 <= uA <= 1 and 0 <= uB <= 1:
        x = x1 + uA * (x2 - x1)
        y = y1 + uA * (y2 - y1)
        return PVector(x, y) if as_PVector else (x, y)
    else:
        return None
    
def point_over_line(px, py, lax, lay, lbx, lby,
                    tolerance=0.1):
    """
    Check if point is over line using the sum of
    the distances from the point to the line ends
    (the result has to be near equal for True).
    """
    ab = dist(lax, lay, lbx, lby)
    pa = dist(lax, lay, px, py)
    pb = dist(px, py, lbx, lby)
    return (pa + pb) <= ab + tolerance

def points_are_colinear(ax, ay, bx, by, cx, cy,
                        tolerance=0.1):
    """
    Test for colinearity by calculating the area
    of a triangle formed by the 3 points.
    """
    area = triangle_area((ax, ay), (bx, by), (cx, cy))
    return abs(area) < tolerance



def draw_poly(points, holes=None, closed=True):
    """
    Aceita como pontos sequencias de tuplas, lista ou vetores com (x, y) ou (x, y, z).
    Note que `holes` espera uma sequencias de sequencias ou uma única sequencia de
    pontos. Por default faz um polígono fechado.
    """
    pass

poly = draw_poly

def edges_as_sets(poly_points, frozen=True):
    """
    Return a (frozen)set of poly edges as frozensets of 2 points.
    """
    if frozen:
        return frozenset(frozenset(edge) for edge in poly_edges(poly_points))
    else:
        return set(frozenset(edge) for edge in poly_edges(poly_points))

def poly_edges(poly_points):
    """
    Return a list of edges (tuples containing pairs of points)
    for a list of points that represent a closed polygon
    """
    return pairwise(poly_points) + [(poly_points[-1], poly_points[0])]

edges = poly_edges

def pairwise(iterable):
    from itertools import tee
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return list(zip(a, b))

def min_max(points):
    """
    Return two tuples with the most extreme coordinates,
    resulting in "bounding box" corners.
    """
    coords = tuple(zip(*points))
    return tuple(map(min, coords)), tuple(map(max, coords))

bounding_box = min_max

def triangle_area(a, b, c):
    area = (a[0] * (b[1] - c[1]) +
            b[0] * (c[1] - a[1]) +
            c[0] * (a[1] - b[1]))
    return area

def poly_area(points):
    points = list(points)
    area = 0.0
    for (ax, ay), (bx, by) in zip(points, points[1:] + [points[0]]):
        area += ax * by
        area -= bx * ay
    return abs(area) / 2.0
    
def rect_points(ox, oy, w, h, mode=CORNER, angle=None):
    if mode == CENTER:
        x, y = ox - w / 2.0, oy - h / 2.0
    else:
        x, y = ox, oy
    points = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    if angle is None:
        return points
    else:
        return [rotate_point((x, y), angle, (ox, oy))
                for x, y in points]

def rotate_point(*args):
    """
    point (tuple/PVector), angle
    x, y, angle (around 0, 0)
    point (tuple/PVector), angle, center (tuple/PVector)
    x, y, angle, x_center, y_center
    """
    if len(args) == 2:
        (xp, yp), angle = args
        x0, y0 = 0, 0
    elif len(args) == 3:
        try:
            (xp, yp), angle, (x0, y0) = args
        except TypeError:
            xp, yp, angle = args
            x0, y0 = 0, 0
    elif len(args) == 5:
        xp, yp, angle, x0, y0 = args
    x, y = xp - x0, yp - y0  # translate to origin
    xr = x * cos(angle) - y * sin(angle)
    yr = y * cos(angle) + x * sin(angle)
    return (xr + x0, yr + y0)

def point_in_screen(*args):
    if len(args) == 1:
        x, y = args[0][0], args[0][1]
    else:
        x, y = args[0], args[1]
    return 0 <= screenX(x, y) <= width and 0 <= screenY(x, y) <= height
    

def par_hatch(points, divisions, *sides):
    # points = [(p[0], p[1]) for p in points]
    lines = []
    if not sides:
        sides = [0]
    for s in sides:
        a, b = points[-1 + s], points[+0 + s]
        d, c = points[-2 + s], points[-3 + s]
        for i in range(1, divisions):
            s0 = lerp_tuple(a, b, i / float(divisions))
            s1 = lerp_tuple(d, c, i / float(divisions))
            lines.append(Line(s0, s1))
    return lines

def is_poly_self_intersecting(poly_points):
    edges = poly_edges(poly_points)
    for a, b in edges[::-1]:
        for c, d in edges[2::]:
            # test only non consecutive edges
            if (a != c) and (b != c) and (a != d):
                if simple_intersect(a, b, c, d):
                    return True
    return False

def point_inside_poly(*args):
    # ray-casting algorithm based on
    # https://wrf.ecse.rpi.edu/Research/Short_Notes/pnpoly.html
    if len(args) == 2:
        (x, y), poly = args
    else:
        x, y, poly = args
    inside = False
    for i, p in enumerate(poly):
        pp = poly[i - 1]
        xi, yi = p
        xj, yj = pp
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
    return inside

def centroid(pts):
    xs, ys = zip(*pts)
    return sum(xs) / len(xs), sum(ys) / len(ys)

def inter_lines(given_line, poly_points):
    """ 
    Line objects that indicate the complete overlap of a given line
    and a polygon (provided as a collection og points)
    """
    inter_pts = []
    for a, b in poly_edges(poly_points):
        inter_pt = line_intersect(Line(a, b), given_line)
        if inter_pt:
            inter_pts.append(inter_pt)
    if not inter_pts:
        return []
    inter_lines = []
    if len(inter_pts) > 1:
        fptx, fpty = inter_pts[0][0], inter_pts[0][1]
        first_pt_dist = lambda pt: ((pt[0] - fptx) ** 2 +
                                    (pt[1] - fpty) ** 2)
        inter_pts.sort(key=first_pt_dist)
        pairs = zip(inter_pts[::2], inter_pts[1::2])
        for a, b in pairs:
            if b:
                inter_lines.append(Line(a, b))
    return inter_lines

def ccw(*args):
    """Returns True if the points are arranged counter-clockwise in the plane"""
    if len(args) == 1:
        a, b, c = args[0]
    else:
        a, b, c = args
    return (b[0] - a[0]) * (c[1] - a[1]) > (b[1] - a[1]) * (c[0] - a[0])

def simple_intersect(*args):
    """Returns True if line segments intersect."""
    if len(args) == 2:    
        (a1, b1), (a2, b2) = args[0], args[1]
    else:
        a1, b1, a2, b2 = args
    return ccw(a1, b1, a2) != ccw(a1, b1, b2) and ccw(a2, b2, a1) != ccw(a2, b2, b1)

def is_poly_convex(poly_points):
    for i, a in enumerate(poly_points):
        b = poly_points[i - 1]
        c = poly_points[i - 2]
        if not ccw(a, b, c):
            return False
    return True

def corner_angle(corner, a, b):
    ac = atan2(a[1] - corner[1], a[0] - corner[0])
    bc = atan2(b[1] - corner[1], b[0] - corner[0])
    return abs(ac - bc)           
  
def hatch_poly(*args, **kwargs):
    if len(args) == 2:
        pts, angle = args
        bound = min_max(pts)
        diag = Line(bound)
        d = diag.dist()
        cx, cy, _ = diag.midpoint()
    else:
        x, y, w, h, angle = args
        pts = rect_points(x, y, w, h, kwargs.pop('mode', CORNER))
        d = dist(pts[0][0], pts[0][1], pts[2][0], pts[2][1])
        cx = (pts[0][0] + pts[1][0]) / 2.0
        cy = (pts[1][1] + pts[2][1]) / 2.0
    spacing = kwargs.get('spacing', 5)
    function = kwargs.pop('function', None)
    base = kwargs.pop('base', True)
    odd_function = kwargs.pop('odd_function', False)
    kwargs['ps'] = ps = (createShape(GROUP) if kwargs.get('ps', False)
                         else False)
    num = int(d / spacing)
    rr = [rotate_point(x, y, angle, cx, cy)
          for x, y in rect_points(cx, cy, d, d, mode=CENTER)]
    # stroke(255, 0, 0)   # debug mode
    ab = Line(rr[0], rr[1])  # ;ab.plot()  # debug mode
    cd = Line(rr[3], rr[2])  # ;cd.plot()  # debug mode
    for i in range(num + 1):
        if odd_function is not False and i % 2:
            kwargs['function'] = odd_function
        else:
            kwargs['function'] = function
        abp = ab.line_point(i / float(num))  # + EPSILON)
        cdp = cd.line_point(i / float(num))  # + EPSILON)
        if base == True:
            kwargs['base_line'] = Line(abp, cdp)
        inter_line_list = inter_lines(Line(abp, cdp), pts)
        for hli in inter_line_list:
            hli.plot(**kwargs)
    return ps

hatch_rect = hatch_poly

def lerp_tuple(a, b, t):   
    return tuple(lerp_tuple(ca, cb, t) if isinstance(ca, tuple)
                 else lerp(ca, cb, t)             
                 for ca, cb in zip(a, b))
    
def simplified_points(pts_list, min_dist):
        reference_point = pts_list[0]
        yield reference_point
        for x, y in pts_list[1:]:
            if dist(x, y, *reference_point) >= min_dist: 
                reference_point = x, y
                yield x, y
'''

