# You'll need py5 - made to run in py5 imported mode, more info at https://py5coding.org
# Also needs http://pymunk.org

import pymunk as pm

space = pm.Space()
space.gravity = (0, 600)

shapes, bodies, constraints = [], [], []
polys = []
current_poly = []
stiffness = 600
damping = 20
mass = 0.5

def setup():
    size(500, 500)
    build_softbody(50, 50, 4, 5, 20, 8, mass)
    build_softbody(150, 50, 5, 5, 20, 8, mass)
    build_softbody(50, 150, 6, 5, 20, 8, mass)
    walls = (
        ((0, height), (width, height)),
        ((0, height), (0, 0)),
        ((width, height), (width, 0)),
    )
    for pa, pb in walls:
        wall = pm.Segment(space.static_body, pa, pb, 2)
        space.add(wall)
    
def draw():
    background(0, 0, 100)
    stroke(255)
    for link in constraints:
        xa, ya = link.a.position
        xb, yb = link.b.position
        line(xa, ya, xb, yb)
    no_stroke()
    fill(255, 100)
    for b in bodies:
        circle(b.position.x, b.position.y, 16)
    for shp in polys:
        draw_poly(shp)

    if current_poly:
        fill(255, 0, 0, 100)
        with begin_closed_shape():
            vertices(current_poly)

    space.step(0.01)
 
def draw_poly(obj):
    push_matrix()
    translate(obj.body.position.x, obj.body.position.y)
    rotate(obj.body.angle)
    pts = obj.get_vertices()
#     begin_shape()
#     for x, y in pts:
#         vertex(x, y)
#     end_shape(CLOSE)
    with begin_closed_shape():
        vertices(pts)
    pop_matrix()
 
def mouse_pressed():
    if mouse_button == RIGHT:
        build_softbody(mouse_x, mouse_y, 4, 8, 20, 8, mass)

def mouse_dragged():
    current_poly.append((mouse_x, mouse_y))
    
def mouse_released():
    if len(current_poly) > 3:
        raw_poly = current_poly[:]
        (xa, ya), (xb, yb) = min_max(raw_poly)
        centroid = (xa + xb) / 2, (ya + yb) / 2
        cx, cy = centroid
        poly = [(x - cx, y - cy) for x, y in raw_poly]
        mass = poly_area(poly) * 0.1
        moi = pm.moment_for_poly(mass, poly)
        body = pm.Body(mass, moi)
        body.position = centroid
        shp = pm.Poly(body, poly)
        space.add(body, shp)
        polys.append(shp)
        current_poly[:] = []
  
def build_softbody(x, y, col, row, ex, radius, mass):   # ex é o espaçamento
    ey = sqrt(3) * 0.5 * ex
    moi = pm.moment_for_circle(mass, 0, radius, (0, 0))
    body_count = len(bodies)
    for j in range(col):
        p = j % 2
        for i in range(row + p):
            body = pm.Body(mass, moi)
            body.position = (x - (p * 0.5 * ex) + i * ex,
                             y + j * ey)
            shp = pm.Circle(body, radius)
            shp.elasticity = 0.6
            shp.friction = 0.8
            space.add(body, shp)
            bodies.append(body)
            shapes.append(shp)

    k = body_count
    for j in range(col - 1):
        p = j % 2
        for i in range(row + p):    
            jleft = jright = 1
            if i == 0 and p:
                jleft = 0
            if i == row and p:
                jright = 0
            if jleft:
                link = pm.DampedSpring(bodies[k], bodies[k + row],
                                         (0, 0), (0, 0),
                                         ex, stiffness, damping)
                space.add(link)
                constraints.append(link)
            if jright:
                link = pm.DampedSpring(bodies[k], bodies[k + row + 1],
                                         (0, 0), (0, 0),
                                         ex, stiffness, damping)
                space.add(link)
                constraints.append(link)
                if p or (not p and i < row - 1):
                    link = pm.DampedSpring(bodies[k], bodies[k + 1],
                                         (0, 0), (0, 0),
                                         ex, stiffness, damping)
                    space.add(link)
                    constraints.append(link)   
            k += 1
    p = col % 2
    for i in range(row - p):
        link = pm.DampedSpring(bodies[k], bodies[k + 1],
                                         (0, 0), (0, 0),
                                         ex, stiffness, damping)
        space.add(link)
        constraints.append(link)
        k += 1        



def min_max(points):
    """
    Return two tuples with the most extreme coordinates,
    resulting in "bounding box" corners.
    """
    coords = tuple(zip(*points))
    return tuple(map(min, coords)), tuple(map(max, coords))
    
def poly_area(pts):
    pts = list(pts)
    area = 0.0
    for (ax, ay), (bx, by) in zip(pts, pts[1:] + [pts[0]]):
        area += ax * by
        area -= bx * ay
    return abs(area) / 2.0

