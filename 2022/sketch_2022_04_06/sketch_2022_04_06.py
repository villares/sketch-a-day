# You'll need py5 -https://py5.ixora.io
# Also needs http://pymunk.org

import py5
import pymunk as pm
from villares.line_geometry import point_inside_poly

space = pm.Space()
space.gravity = (0, 600)

constraints = []
current_poly = []
stiffness = 1000
damping = 100
mass = 1


def setup():
    py5.size(500, 500)
    pm.Poly.draw = draw_poly  # this is called "monkeypatching"
    pm.Circle.draw = draw_circle
    pm.Segment.draw = draw_segment
    pm.DampedSpring.draw = draw_link
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
    py5.background(100, 100, 20)
        
    py5.no_stroke()
    py5.fill(255, 100)    
    for shp in space.shapes:
        shp.draw()

    py5.stroke(0)
    for link in constraints:
        link.draw()

    if current_poly:
        py5.fill(255, 0, 0, 100)
        with py5.begin_closed_shape():
            py5.vertices(current_poly)

    space.step(0.01)


def draw_poly(obj):
    with py5.push_matrix():
        py5.translate(obj.body.position.x, obj.body.position.y)
        py5.rotate(obj.body.angle)
        pts = obj.get_vertices()
        with py5.begin_closed_shape():
            py5.vertices(pts)

def draw_segment(obj):
    with py5.push():
        py5.stroke(255)    
        py5.stroke_weight(obj.radius*2)
        py5.line(obj.a.x, obj.a.y, obj.b.x, obj.b.y)  

def draw_link(obj):
    xa, ya = obj.a.position
    xb, yb = obj.b.position
    py5.line(xa, ya, xb, yb)   

def draw_circle(obj):
    py5.circle(obj.body.position.x,
               obj.body.position.y,
               obj.radius * 2)

def build_polybody(poly):
    (xa, ya), (xb, yb) = min_max(poly)
    centroid = (xa + xb) / 2, (ya + yb) / 2
    cx, cy = centroid
    poly = [(x - cx, y - cy) for x, y in poly]
    mass = poly_area(poly) * 0.1
    moi = pm.moment_for_poly(mass, poly)
    body = pm.Body(mass, moi)
    body.position = centroid
    shp = pm.Poly(body, poly)
    shp.friction = 0.2
    space.add(body, shp)


def build_softpoly(x, y, cols, rows, ex, radius, mass, poly):  
    ey = py5.sqrt(3) * 0.5 * ex
    moi = pm.moment_for_circle(mass, 0, radius, (0, 0))
    grid = {}  # dict for grid elements, (i, j) as keys
    for j in range(rows):
        odd_row = j % 2
        for i in range(cols + odd_row):
            body = pm.Body(mass, moi)
            bx, by = x - (odd_row * 0.5 * ex) + i * ex, y + j * ey
            if point_inside_poly(bx, by, poly):                
                body.position = (bx, by)
                shp = pm.Circle(body, radius)
                shp.elasticity = 0.6
                shp.friction = 0.6
                space.add(body, shp)
                grid[(i, j)] = body
    for j in range(rows):
        odd_row = j % 2
        for i in range(cols + odd_row):
            if not (me := grid.get((i, j))):
                continue
            if right := grid.get((i + 1, j)):
                create_link(me, right, ex)
            if down := grid.get((i, j + 1)):
                create_link(me, down, ex)
            if not odd_row and (down_right := grid.get((i + 1, j + 1))):
                create_link(me, down_right, ex)
            elif down_left := grid.get((i - 1, j + 1)):
                create_link(me, down_left, ex)

def build_softbody(x, y, cols, rows, ex, radius, mass):   # ex (x espacing)
    ey = py5.sqrt(3) * 0.5 * ex
    moi = pm.moment_for_circle(mass, 0, radius, (0, 0))
    grid = {}  # dict for grid elements, (i, j) as keys
    for j in range(rows):
        odd_row = j % 2
        for i in range(cols + odd_row):
            body = pm.Body(mass, moi)
            body.position = (x - (odd_row * 0.5 * ex) + i * ex, y + j * ey)
            shp = pm.Circle(body, radius)
            shp.elasticity = 0.6
            shp.friction = 0.6
            space.add(body, shp)
            grid[(i, j)] = body
    for j in range(rows):
        odd_row = j % 2
        for i in range(cols + odd_row):
            me = grid.get((i, j))
            if right := grid.get((i + 1, j)):
                create_link(me, right, ex)
            if down := grid.get((i, j + 1)):
                create_link(me, down, ex)
            if not odd_row and (down_right := grid.get((i + 1, j + 1))):
                create_link(me, down_right, ex)
            elif down_left := grid.get((i - 1, j + 1)):
                create_link(me, down_left, ex)

def create_link(me, other, ex):
                link = pm.DampedSpring(me, other, (0, 0), (0, 0),
                                       ex, stiffness, damping)
                space.add(link)
                constraints.append(link)

 

def min_max(pts):
    """
    Return two tuples with the most extreme coordinates,
    resulting in "bounding box" corners.
    """
    coords = tuple(zip(*pts))
    return tuple(map(min, coords)), tuple(map(max, coords))

def poly_area(pts):
    pts = list(pts)
    area = 0.0
    for (ax, ay), (bx, by) in zip(pts, pts[1:] + [pts[0]]):
        area += ax * by
        area -= bx * ay
    return abs(area) / 2.0

def key_pressed():
    if py5.key == ' ':
        for obj in reversed(space.shapes):
            if not is_segment(obj):
                space.remove(obj)

def mouse_pressed():
    if py5.mouse_button == py5.RIGHT:
        build_softbody(py5.mouse_x, py5.mouse_y, 8, 4, 20, 10, mass)


def mouse_dragged():
    current_poly.append((py5.mouse_x, py5.mouse_y))


def mouse_released():
    if len(current_poly) > 3:
        #build_polybody(current_poly[:])
        cp = current_poly[:]
        (xa, ya), (xb, yb) = min_max(cp)
        build_softpoly(xa, ya, 50, 50, 20, 10, mass, cp)
        current_poly[:] = []


def is_circle(obj): return isinstance(obj, pm.Circle)
def is_poly(obj): return isinstance(obj, pm.Poly) 
def is_segment(obj): return isinstance(obj, pm.Segment) 


py5.run_sketch()

