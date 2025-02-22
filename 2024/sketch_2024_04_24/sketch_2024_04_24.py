# based on sketch_2023_10_24.py

import py5            # the main graphics & interaction framework
import pymunk as pm   # the 2D physics engine
from trimesh.creation import triangulate_polygon
import shapely
from shapely.affinity import translate as shapely_translate

MINIMUM_DIST = 50     # harder to draw, but more elegant objects

space = pm.Space()    # the pymunk simulation space
space.gravity = (0, 600)

current_poly = []     # (x, y) tuples while mouse dragging

def setup():
    #global margin
    py5.size(800, 800)
    py5.color_mode(py5.HSB)
    
    margin = 10
    walls = (
        ((margin, py5.height - margin), (py5.width - margin, py5.height - margin)),
        ((margin, py5.height - margin), (margin, margin)),
        ((py5.width - margin, py5.height - margin), (py5.width - margin, margin)),
    )
    for pa, pb in walls:
        wall = pm.Segment(space.static_body, pa, pb, 2)
        wall.friction = 0.4
        space.add(wall)

def draw():
    py5.background(100)
    for b in space.bodies:  # draws the objects
        b.draw()

    if current_poly:   # draws poly preview while dragging mouse
        py5.fill(255, 0, 0, 100)
        with py5.begin_closed_shape():
            py5.vertices(current_poly)

    space.step(0.01)   # advance simulation

class DrawableBody(pm.Body):
    def draw(self):
        with py5.push():
            py5.no_stroke()
            py5.translate(self.position.x, self.position.y)
            py5.rotate(self.angle)
            a = self.position.y / 3 
            py5.fill((100 + self.area / 1000) % 255, 200, 200, 200)
            py5.shape(self.py5shape, 0, 0)
   

def min_max(pts):
    coords = tuple(zip(*pts))
    return tuple(map(min, coords)), tuple(map(max, coords))


def add_trianglulated_body(poly: shapely.Polygon):
    """
    Todo, look at shapely centroid and improve
    DrawableBody class maybe to get the shapely.Poly
    Maybe passe everything t the DrawableBody class?
    """
    from math import isnan
    vs, faces = triangulate_polygon(poly)
    triangles = [(vs[a], vs[b], vs[c]) for a, b, c in faces]
    cp = shapely.centroid(poly)
    cx, cy = centroid = cp.x, cp.y
    translated_tris = []
    total_mass = total_moi = 0
    for tri in triangles:
        translated_tri = [(x - cx, y - cy) for x, y in tri]
        mass = poly_area(translated_tri) * 0.1
        total_mass += mass
        moi = pm.moment_for_poly(mass, translated_tri)
        if not isnan(moi):
            total_moi += moi
        translated_tris.append(translated_tri)   
    body = DrawableBody(total_mass, total_moi)
    body.area = poly.area
    body.py5shape = py5.convert_shape(shapely_translate(poly, -cx, -cy))
    body.py5shape.disable_style()
    body.position = centroid
    shapes = []
    for tri in translated_tris:
        shp = pm.Poly(body, tri)
        shp.friction = 0.4
        shapes.append(shp)
    #print(f'shapes: {len(shapes)}')
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
    global text_x
    if py5.key == py5.DELETE:
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
        add_trianglulated_body(shapely.Polygon(current_poly))
    current_poly.clear()

py5.run_sketch(block=False)   # starts py5, setup() and then the main loop, draw()

