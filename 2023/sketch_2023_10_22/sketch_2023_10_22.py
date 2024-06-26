import math           # for math.isnan

import py5            # the main graphics & interaction framework
import pymunk as pm   # the 2D physics engine

from triangulate import triangulate   # my ugly triangulation code

MINIMUM_DIST = 50     # harder to draw, but more elegant objects

space = pm.Space()    # the pymunk simulation space
space.gravity = (0, 600)

current_poly = []     # (x, y) tuples while mouse dragging

def setup():
    py5.size(600, 600)
    pm.Poly.draw = draw_poly  # this is called "monkeypatching"
    pm.Segment.draw = draw_segment
    gap = 5
    walls = (
        ((gap, py5.height - gap), (py5.width - gap, py5.height - gap)),
        ((gap, py5.height - gap), (gap, gap)),
        ((py5.width - gap, py5.height - gap), (py5.width - gap, gap)),
    )
    for pa, pb in walls:
        wall = pm.Segment(space.static_body, pa, pb, 2)
        wall.friction = 0.2
        space.add(wall)

def draw():
    py5.background(0, 50, 100)
        
    py5.stroke(255)           # white stroke
    py5.fill(255, 100)        # translucent white
    for shp in space.shapes:  # draws the objects
        shp.draw()

    if current_poly:   # draws poly preview while dragging mouse
        py5.fill(255, 0, 0, 100)
        with py5.begin_closed_shape():
            py5.vertices(current_poly)

    space.step(0.01)   # advance simulation


def draw_poly(self):
    """For monkey patching pm.Poly"""
    with py5.push_matrix():
        py5.translate(self.body.position.x, self.body.position.y)
        py5.rotate(self.body.angle)
        pts = self.get_vertices()
        with py5.begin_closed_shape():
            py5.vertices(pts)

def draw_segment(self):
    """For monkey patching pm.Segment"""
    with py5.push():
        py5.stroke(255)    
        py5.stroke_weight(self.radius*2)
        py5.line(self.a.x, self.a.y, self.b.x, self.b.y)  

def min_max(pts):
    coords = tuple(zip(*pts))
    return tuple(map(min, coords)), tuple(map(max, coords))

def build_trianglulated_body(poly):
    """
    New builder that creates a multi-shape body, allowing concave objects.
    """
    triangles = triangulate(poly)
    (xa, ya), (xb, yb) = min_max(poly)
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
        shp = pm.Poly(body, poly)
        shp.friction = 0.2
        shapes.append(shp)
    space.add(body, *shapes)  # Note critical * operator expands .add(b, s0, s1, s2...)

def poly_area(pts):
    area = 0.0
    for (ax, ay), (bx, by) in zip(pts, pts[1:] + [pts[0]]):
        area += ax * by
        area -= bx * ay
    return abs(area) / 2.0

def is_poly(obj): return isinstance(obj, pm.Poly) 
def is_segment(obj): return isinstance(obj, pm.Segment) 

def key_pressed():
    if py5.key == ' ':
        # clear everything but the "box" walls
        for obj in reversed(space.shapes):
            if not is_segment(obj):
                space.remove(obj)

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
        build_trianglulated_body(current_poly)
    current_poly.clear()

py5.run_sketch()   # starts py5, setup() and then the main loop, draw()

# Used as reference...
#
# def build_poly_body(poly):
#     """Earlier convex poligonal objects builder"""
#     (xa, ya), (xb, yb) = min_max(poly)
#     centroid = (xa + xb) / 2, (ya + yb) / 2
#     cx, cy = centroid
#     poly = [(x - cx, y - cy) for x, y in poly]
#     mass = poly_area(poly) * 0.1
#     moi = pm.moment_for_poly(mass, poly)
#     print(moi)
#     body = pm.Body(mass, moi)
#     body.position = centroid
#     shp = pm.Poly(body, poly)
#     shp.friction = 0.2
#     space.add(body, shp)