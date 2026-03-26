# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5
import shapely
from shapely import MultiPolygon, Polygon, LineString, MultiLineString
import numpy as np


def setup():
    global poly_pts, hatch
    py5.size(600, 600)
    py5.stroke_cap(py5.ROUND)
    poly_pts = polys_from_text('A', ('Open Sans Bold', 600)).geoms[0].geoms[0]
    hatch = py5.convert_shape(generate_hatch(
        poly_pts,
        angle=py5.PI /  4
    ))
    for i, s in enumerate(hatch.get_children()):
        s.set_stroke_weight((1 + i) / 10)
        s.set_stroke(py5.color(i * 4, 0, 0 ))

    py5.background(220, 220, 180)
    py5.translate(50, 550)
    py5.shape(hatch)
    py5.stroke_weight(6)
    for ax, ay, bx, by in edges(poly_pts.exterior.coords):
            dashed_line(ax, ay, bx, by, d=10)    
    for hole in poly_pts.interiors:
        for ax, ay, bx, by in edges(hole.coords):
            dashed_line(ax, ay, bx, by, d=10)

def edges(poly_points):
    poly_points = np.asarray(poly_points)
    rolled = np.roll(poly_points, -1, axis=0)
    return np.column_stack((poly_points, rolled))

def dashed_line(*args, d=20):
    global dashes
    dim = len(args)//2  # 4 args is 2d, 6 args is 3d 
    a = args[:dim]
    b = args[dim:]
    a = np.array(a)
    b = np.array(b)
    c = py5.dist(*a, *b)
    n = int(c / d)
    t = np.linspace((0, 0), (1, 1), n)
    coords = py5.lerp(a, b, t)
    dashes = edges(coords)[:-1:2]
    py5.lines(dashes)

def dotted_line(*args, d=20):
    dim = len(args)//2  # 4 args is 2d, 6 args is 3d 
    a = args[:dim]
    b = args[dim:]
    a = np.array(a)
    b = np.array(b)
    c = py5.dist(*a, *b)
    n = int(c / d)
    t = np.linspace((0, 0), (1, 1), n)
    coords = py5.lerp(a, b, t)
    py5.points(coords)

def fill_points(poly_pts, d=10):
    poly_pts = np.asarray(poly_pts)
    poly = shapely.Polygon(poly_pts)
    # shapely.prepare(poly)
    minx, miny, maxx, maxy = poly.bounds
    x = np.arange(minx, maxx + d, d)
    y = np.arange(miny, maxy + d, d)
    xx, yy = np.meshgrid(x, y)
    grid = np.column_stack([xx.ravel(), yy.ravel()])
    # mask = np.array([poly.contains(shapely.Point(pt)) for pt in grid])
    # py5.points(grid[mask])
    pts = shapely.MultiPoint(grid).intersection(poly)
    py5.shape(pts) 
 


def generate_hatch(poly, angle=0, spacing=10, holes=[]):
    if not isinstance(poly, (Polygon, MultiPolygon)):
        poly = Polygon(poly, holes)
    if poly.area == 0:
        return MultiLineString()
    diagonal = py5.dist(*poly.bounds)  # diagonal length
    #print(poly.bounds, diagonal, poly.area)
    num = int(diagonal / spacing)
    V = py5.Py5Vector
    centroid = V(poly.envelope.centroid.x, poly.envelope.centroid.y)
    a = V(-diagonal / 2, -diagonal / 2).rotate(angle) + centroid
    b = V(-diagonal / 2, +diagonal / 2).rotate(angle) + centroid
    c = V(+diagonal / 2, -diagonal / 2).rotate(angle) + centroid
    d = V(+diagonal / 2, +diagonal / 2).rotate(angle) + centroid
    lines = [LineString((V.lerp(a, b, i / num), V.lerp(c, d, i / num)))
             for i in range(num + 1)]
    return MultiLineString(lines).intersection(poly)
 
def polys_from_text(
    words: str,
    font: py5.Py5Font | tuple(str, float),
    leading: float = None, 
    alternate_spacing=False
    
    ) -> shapely.GeometryCollection:
    """
    Produce from a string a shapely GeometryCollection containing
    MultiPolygons for each glyph. The MultiPolygon.geoms contains
    one or more shapely.Polygon objects (which can have holes).
    New-line chars will try to move text to a new line.
    
    The alternate_spacing option will pick the glyph
    spacing from py5.text_width() for each glyph, it can be
    too spaced, but good for monospaced font alignment.
    """
    if isinstance(font, tuple):
        name, size = font
        font = py5.create_font(name, size)
    # Use the font size as leading value if none is provided.
    leading = leading or font.get_size()
    py5.text_font(font)
    space_width = py5.text_width(' ')
    results = []
    x_offset = y_offset = 0
    for c in words:
        if c == '\n':
            y_offset += leading
            x_offset = 0  # this assumes left aligned text...
            continue
        glyph_pt_lists = [[]] # starts with an empty list inside
        # font.get_shape(c, 1) will trigger a "Need to call beginShape() first"
        # Processing warning you can safely ignore.
        c_shp = font.get_shape(c, 1)  
        vs3d = [c_shp.get_vertex(i)
                for i in range(c_shp.get_vertex_count())]
        vs = set()
        for vx, vy, _ in vs3d:
            x = vx + x_offset
            y = vy + y_offset
            glyph_pt_lists[-1].append((x, y))
            if (x, y) not in vs:
                vs.add((x, y))
            else:
                glyph_pt_lists.append([]) # note this leaves trailling empty list
        if alternate_spacing:
            w = py5.text_width(c)
        else:
            w = c_shp.get_width() if vs3d else space_width
        x_offset += w
        # filter out elements with less than 3 points 
        # and stop one item before the trailling empty list
        glyph_polys = [shapely.Polygon(p)
                       for p in glyph_pt_lists[:-1] if len(p) > 2]
        if glyph_polys:  # there are still empty glyphs at this point
            glyph_shapes = process_glyphs(glyph_polys)
            results.append(glyph_shapes)
    return shapely.GeometryCollection(results)

def process_glyphs(polys: list[shapely.Polygon]) -> shapely.MultiPolygon:
    """
    Try to subtract the shapely Polygons from glyph contours
    in order to produce appropriate looking glyphs with holes.
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
    return shapely.MultiPolygon(results)
 
def key_pressed():
    py5.save_frame('out.png')

py5.run_sketch(block=False)


