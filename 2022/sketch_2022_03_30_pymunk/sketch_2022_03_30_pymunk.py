import py5
import pymunk as pm

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
    py5.background(0, 100, 20)
        
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


def build_softbody(x, y, cols, rows, ex, radius, mass):   # ex é o espaçamento
    ey = py5.sqrt(3) * 0.5 * ex
    moi = pm.moment_for_circle(mass, 0, radius, (0, 0))
    bodies = []
    for j in range(rows):
        p = j % 2
        for i in range(cols + p):
            body = pm.Body(mass, moi)
            body.position = (x - (p * 0.5 * ex) + i * ex,
                             y + j * ey)
            shp = pm.Circle(body, radius)
            shp.elasticity = 0.6
            shp.friction = 0.6
            space.add(body, shp)
            bodies.append(body)

    k = 0
    for j in range(rows - 1):
        p = j % 2
        for i in range(cols + p):
            jleft = jright = 1
            if i == 0 and p:
                jleft = 0
            if i == cols and p:
                jright = 0
            if jleft:
                link = pm.DampedSpring(bodies[k], bodies[k + cols],
                                       (0, 0), (0, 0),
                                       ex, stiffness, damping)
                space.add(link)
                constraints.append(link)
            if jright:
                link = pm.DampedSpring(bodies[k], bodies[k + cols + 1],
                                       (0, 0), (0, 0),
                                       ex, stiffness, damping)
                space.add(link)
                constraints.append(link)
                if p or (not p and i < cols - 1):
                    link = pm.DampedSpring(bodies[k], bodies[k + 1],
                                           (0, 0), (0, 0),
                                           ex, stiffness, damping)
                    space.add(link)
                    constraints.append(link)
            k += 1
    p = rows % 2
    for i in range(cols - p):
        link = pm.DampedSpring(bodies[k], bodies[k + 1],
                               (0, 0), (0, 0),
                               ex, stiffness, damping)
        space.add(link)
        constraints.append(link)
        k += 1

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
        build_polybody(current_poly[:])
        current_poly[:] = []


def is_circle(obj): return isinstance(obj, pm.Circle)
def is_poly(obj): return isinstance(obj, pm.Poly) 
def is_segment(obj): return isinstance(obj, pm.Segment) 


py5.run_sketch()
