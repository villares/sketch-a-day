import math           # for math.isnan

import py5            # the main graphics & interaction framework
import pymunk as pm   # the 2D physics engine
from trimesh.creation import triangulate_polygon
import shapely
from shapely.affinity import translate as shapely_translate

MINIMUM_DIST = 20     # harder to draw, but more elegant objects

space = pm.Space()    # the pymunk simulation space
space.gravity = (0, 600)

current_poly = []     # (x, y) tuples while mouse dragging

def setup():
    global font, margin, text_x
    py5.size(800, 800)
    py5.color_mode(py5.HSB)
    
    #font = py5.create_font('Tomorrow Bold', 120)
    #font = py5.create_font('GaroaHackerClubeKnuthEdition', 120)
    font = py5.create_font('FreeSans Bold', 120)
    
    margin = 5
    text_x = margin * 2
    walls = (
        ((margin, py5.height - margin), (py5.width - margin, py5.height - margin)),
        ((margin, py5.height - margin), (margin, margin)),
        ((py5.width - margin, py5.height - margin), (py5.width - margin, margin)),
    )
    for pa, pb in walls:
        wall = DrawableSegment(space.static_body, pa, pb, 2)
        wall.friction = 0.4
        space.add(wall)

def draw():
    py5.background(200, 50, 100)
#     py5.stroke(255)           # white stroke
    py5.fill(255, 100)        # translucent white
    for shp in space.shapes:  # draws the objects
        shp.draw()

    if current_poly:   # draws poly preview while dragging mouse
        py5.fill(255, 0, 0, 100)
        with py5.begin_closed_shape():
            py5.vertices(current_poly)

    space.step(0.01)   # advance simulation

class DrawablePoly(pm.Poly):
    def draw(self):
        with py5.push():
            py5.no_stroke()
            py5.translate(self.body.position.x, self.body.position.y)
            py5.rotate(self.body.angle)
            pts = self.get_vertices()
            a = poly_area(pts) / 20
            py5.fill(100 + a % 100, 200, 200, 200)
            with py5.begin_closed_shape():
                py5.vertices(pts)

class DrawableSegment(pm.Segment):
    def draw(self):
        with py5.push():
            py5.stroke(255)    
            py5.stroke_weight(self.radius*2)
            py5.line(self.a.x, self.a.y, self.b.x, self.b.y)  

def min_max(pts):
    coords = tuple(zip(*pts))
    return tuple(map(min, coords)), tuple(map(max, coords))

def add_trianglulated_body(poly: shapely.Polygon):
    vs, faces = triangulate_polygon(poly)
    triangles = [(vs[a], vs[b], vs[c]) for a, b, c in faces]
    (xa, ya), (xb, yb) = min_max(vs)
    centroid = (xa + xb) / 2, (ya + yb) / 2
    cx, cy = centroid
    polys = []
    total_mass = total_moi = 0
    for tri in triangles:
        poly = [(x - cx, y - cy) for x, y in tri]
        mass = poly_area(poly) * 0.1
        total_mass += mass
        moi = pm.moment_for_poly(mass, poly)
        if not math.isnan(moi):
            total_moi += moi
        polys.append(poly)   
    body = pm.Body(total_mass, total_moi)
    body.position = centroid
    shapes = []
    for poly in polys:
        shp = DrawablePoly(body, poly)
        shp.friction = 0.4
        shapes.append(shp)
    print(f'shapes: {len(shapes)}')
    space.add(body, *shapes)  # Note critical * operator expands .add(b, s0, s1, s2...)

def poly_area(pts):
    area = 0.0
    for (ax, ay), (bx, by) in zip(pts, pts[1:] + [pts[0]]):
        area += ax * by
        area -= bx * ay
    return abs(area) / 2.0

def is_poly(obj): return isinstance(obj, pm.Poly) 
def is_segment(obj): return isinstance(obj, pm.Segment) 

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
        glyph_polys = [shapely.Polygon(p) for p in glyph_pt_lists[:-1] if len(p) > 2]
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

def key_pressed():
    global text_x
    if py5.key == py5.DELETE:
        # clear everything but the "box" walls
        for obj in reversed(space.shapes):
            if not is_segment(obj):
                space.remove(obj)
    elif py5.key == py5.ENTER:
        text_x = margin * 2
    elif py5.key != py5.CODED:
        for p in polys_from_text(str(py5.key), font):
            add_trianglulated_body(shapely_translate(p, text_x, 0))
        text_x += py5.text_width(str(py5.key))
        if text_x > py5.width - py5.text_width('W'):
            text_x = margin * 2


def mouse_dragged():
    # adds a tuple with the mouse coordinates if the current_poly list is empty
    # or if the x, y in current_poly[-1] are far enough from the mouse    
    mx, my = py5.mouse_x, py5.mouse_y
    if not current_poly or (py5.dist(current_poly[-1][0], current_poly[-1][1], mx, my)
                            >= MINIMUM_DIST):
        current_poly.append((mx, my))

def mouse_released():
    # creates an object if there are enough points on the list, clears list    
    if len(current_poly) >= 3:
        add_trianglulated_body(shapely.Polygon(current_poly))
    current_poly.clear()

py5.run_sketch(block=False)   # starts py5, setup() and then the main loop, draw()
