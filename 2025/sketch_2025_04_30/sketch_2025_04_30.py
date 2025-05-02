import py5
import pymunk

CT_DEFAULT = 0
CT_SPECIAL = 1
CT_WALL = 2

MINIMUM_DIST = 50
current_poly = [] # (x, y) tuples while mouse dragging
wall_start = None
drawing_dict = {}
save_filename = 'data.pickle'
mass_scale = 0.1

def setup():
    global space
    py5.size(600, 600)
    space = pymunk.Space()
    space.gravity = 0, 900
    space.add_collision_handler(
        CT_SPECIAL, CT_DEFAULT
    ).pre_solve = color_collision
    add_wall(100, 500, 500, 500)
    add_static_box(300, 300, 100, 20)
    add_static_box(200, 200, 100, 20)
    add_static_box(400, 400, 100, 20)


def draw():  # py5's main loop
    py5.background(200, 200, 150)  # R, G, B
    for item, (draw_func, kwargs) in list(drawing_dict.items()):
        draw_func(item, **kwargs)
        py = item.body.position.y if hasattr(item, 'body') else item.position.y        
        if py > py5.height + 50:
            space.remove(item)
            del drawing_dict[item]
    # many new balls
    if py5.is_key_pressed and py5.key_code == py5.SHIFT:     
        add_ball(py5.mouse_x + py5.random(-1, 1),
                 py5.mouse_y)
    # wall preview
    fill_and_stroke('red', 'red', 3)
    if wall_start:
        py5.line(*wall_start, py5.mouse_x, py5.mouse_y)
    if current_poly:   # draws poly preview while dragging mouse
        with py5.begin_closed_shape():
            py5.vertices(current_poly)
    # advance the simulation
    space.step(1 / 60)


def color_collision(arbiter, space, data):
    s1, s2 = arbiter.shapes
    s2.collision_type=CT_SPECIAL
    s1.collision_type=CT_DEFAULT
    drawing_dict[s2][1]['fill'] = int(py5.color(255, 0, 0))
    drawing_dict[s1][1]['fill'] = 0
    return True

def add_ball(
    x, y, diameter=10, stroke=None, fill=0, collision_type=CT_DEFAULT
    ):
    radius = diameter / 2
    mass = py5.PI * radius ** 2 * mass_scale
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    body.position = x, y
    shp = pymunk.Circle(body, radius, (0, 0))
    shp.friction = 0.99
    space.add(body, shp)
    drawing_dict[shp] = (
        draw_circle,
        {'stroke': stroke, 'fill': fill}
        )

def add_static_ball(
    x, y, diameter=10, stroke=None, fill=0, collision_type=CT_DEFAULT
    ):
    radius = diameter / 2
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shp = pymunk.Circle(body, radius, (x, y))
    shp.friction = 0.99
    space.add(body, shp)
    drawing_dict[shp] = (
        draw_circle,
        {'s': None, 'f': f}
        )

def add_wall(xa, ya, xb, yb):
    shape = pymunk.Segment(space.static_body,
                           (xa, ya), (xb, yb),
                           radius=1.5)
    shape.collision_type = CT_WALL
    shape.friction = 100.99
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    space.add(body, shape)
    drawing_dict[shape] = (
        draw_static_segment,
        {'stroke': 128}
        )

def add_poly(poly, stroke=0, fill=255):
    triangles = triangulate(poly)
    # this is bad, I should use shapely!
    (xa, ya), (xb, yb) = min_max(poly)
    cx, cy = (xa + xb) / 2, (ya + yb) / 2
    polys = []
    total_mass = total_moi = 0
    for tri in triangles:
        tri_poly = [(x - cx, y - cy) for x, y in tri]
        mass = poly_area(tri_poly) * 0.1
        total_mass += mass
        moi = pymunk.moment_for_poly(mass, tri_poly)
        if not py5.np.isnan(moi):
            total_moi += moi
        polys.append(tri_poly)   
    body = pymunk.Body(total_mass, total_moi)
    body.position = cx, cy
    shapes = []
    for tri_poly in polys:
        shp = pymunk.Poly(body, tri_poly)
        shp.friction = 0.2
        shapes.append(shp)
    drawing_dict[body] = (
        draw_poly,
        {'stroke': stroke, 'fill': fill,
         'poly':  [(x - cx, y - cy) for x, y in poly]}
    )
    space.add(body, *shapes)  # Note critical * operator expands .add(b, s0, s1, s2...)
    

def add_static_ball(
    x, y, diameter=20, fill=0
    ):
    radius = diameter / 2
    shp = pymunk.Circle(space.static_body, radius, (x, y))
    shp.friction = 0.99
    space.add(shp)
    drawing_dict[shp] = (
        draw_circle,
        {'stroke': None, 'fill': f}
        )

def add_box(x, y, w, h, stroke=None, fill=0):
    mass = w * h * mass_scale
    moment = pymunk.moment_for_box(mass, (w, h))
    body = pymunk.Body(mass, moment)
    body.position = (x , y)
    shp = pymunk.Poly.create_box(body, (w, h))
    shp.friction = 100.99
    space.add(body, shp)
    drawing_dict[shp] = (
        draw_poly,
        {'stroke': stroke, 'fill': fill}
    )

def add_static_box(x, y, w, h, stroke=None, fill=128):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (x , y)
    shp = pymunk.Poly.create_box(body, (w, h))
    shp.friction = 100.99
    space.add(body, shp)
    drawing_dict[shp] = (
        draw_poly,
        {'stroke': stroke, 'fill': fill}
    )

def fill_and_stroke(fill=255, stroke=0, weight=None):
    py5.stroke_weight(weight or 1)
    if stroke is not None:
        py5.stroke(stroke)
    else:
        py5.no_stroke()
    if fill is not None:
        py5.fill(fill)
    else:
        py5.no_fill()
 
def draw_circle(shape, fill=0, stroke=None):
    fill_and_stroke(fill, stroke)
    py5.circle(shape.body.position.x,
               shape.body.position.y,
               shape.radius * 2)

def draw_static_segment(shape, fill=None, stroke=0, weight=3):
    fill_and_stroke(fill, stroke, weight)
    py5.line(shape.a.x, shape.a.y,
             shape.b.x, shape.b.y)

def draw_poly(item, fill=0, stroke=255, weight=None, poly=None):
    if isinstance(item, pymunk.Poly):
        fill_and_stroke(fill, stroke, weight) 
        with py5.push_matrix():
            py5.translate(item.body.position.x, item.body.position.y)
            py5.rotate(item.body.angle)
            pts = item.get_vertices()
            with py5.begin_closed_shape():
                py5.vertices(pts)
    else:
        fill_and_stroke(fill, stroke, weight) 
        with py5.push_matrix():
            py5.translate(item.position.x, item.position.y)
            py5.rotate(item.angle)
            print(poly)
            with py5.begin_closed_shape():
                py5.vertices(poly)
        


def mouse_clicked():
    if py5.is_key_pressed and py5.key_code == py5.CONTROL:
        f = py5.color(255, 255, 0)
        ct = CT_SPECIAL
    else:
        f = 0
        ct = CT_DEFAULT
    add_ball(py5.mouse_x + py5.random(-1, 1),
                    py5.mouse_y,
                    fill=f,
                    collision_type=ct)

def mouse_dragged():
    global wall_start
    mx, my = py5.mouse_x, py5.mouse_y
    if py5.is_key_pressed and py5.key_code == py5.CONTROL:
        if (not current_poly or
            py5.dist(current_poly[-1][0],
                     current_poly[-1][1],
                    mx, my) >= MINIMUM_DIST):
            current_poly.append((mx, my))
    elif not wall_start:
        wall_start = (mx, my)
   
def min_max(pts):
    coords = tuple(zip(*pts))
    return tuple(map(min, coords)), tuple(map(max, coords))
   
def mouse_released():
    global wall_start
    if len(current_poly) >= 3:
        add_poly(current_poly)
    elif (wall_start and
        py5.dist(*wall_start,
                 py5.mouse_x, py5.mouse_y) > 5):
        inicio_x, inicio_y = wall_start
        add_wall(inicio_x, inicio_y,
                          py5.mouse_x, py5.mouse_y)
    wall_start = None
    current_poly.clear()

 
def key_pressed():
    global wall_start, space, drawing_dict
    # tecla DELETE apaga walls
    if wall_start and py5.key in (py5.DELETE, py5.ESC):
        py5.intercept_escape()
        wall_start = None
    elif py5.key == py5.DELETE:
        for shape in reversed(drawing_dict.keys()):
            if isinstance(shape, pymunk.Segment):
                space.remove(shape)
                del drawing_dict[shape]
                break
    # "c" limpa balls
    elif py5.key in ('c', 'C'):
        for shape in space.shapes:
            if isinstance(shape, pymunk.Circle):
                space.remove(shape)
                del drawing_dict[shape]
    # "s" salve simulation state
    elif py5.key == 's':
        py5.save_pickle((space, drawing_dict), 'data.pickle')
        print(f'Saved {save_filename}.')
    # "l" load from previous saved state
    elif py5.key == 'l':
        if py5.Path(save_filename).is_file():
            space, drawing_dict = py5.load_pickle(save_filename)
            print(f'Loaded {save_filename}.')

    print(f'shapes in simulation: {len(space.shapes)}')

def mouse_wheel(e):
    for obj in space.shapes:
         info = obj.point_query((py5.mouse_x, py5.mouse_y))
         if info.distance < 2:
             obj.body.angle += py5.radians(e.get_count())


def triangulate(original_shape):
    """
    Based on https://gist.github.com/Shaptic/6297978
    """
    # Use orientation of the top-left-most vertex.
    shape = list(original_shape[:])
    left, starting_index = shape[0], 0
    for i, v in enumerate(shape):
        if v[0] < left[0] or (v[0] == left[0] and v[1] < left[1]):
            left = v
            starting_index = i
    orientation = ccw(get_ear(shape, starting_index))
    triangles = []
    while len(shape) >= 3:
        reflex_vertices = []
        eartip = -1
        for i, v in enumerate(shape):  # For each vertex in the shape
            if eartip >= 0:
                break
            triangle = get_ear(shape, i)  # A triangle from vertex to adjacents.
            # If polygon's orientation doesn't match that of the triangle,
            # it's definitely a reflex and not an ear.
            if ccw(triangle) != orientation:
                reflex_vertices.append(v)
                continue  # Test reflex vertices first.
            for rv in reflex_vertices:
                if rv in triangle:
                    continue  # If we are testing ourselves, skip.
                elif in_poly(rv, triangle):
                    break  # If any reflex vertex in triangle, not ear.
            else:  # No reflexes, so we test all past current vertex.
                for past_current_v in shape[i + 2:]:
                    if past_current_v in triangle:
                        continue
                    elif in_poly(past_current_v, triangle):
                        break  # No vertices in the triangle, we are an ear.
                else:
                    eartip = i
        if eartip == -1:
            break
        triangles.append(get_ear(shape, eartip))
        del shape[eartip] 
    return triangles

def ccw(tri):
    assert len(tri) == 3, 'must be a triangle'
    a, b, c = tri
    return (b[0] - a[0]) * (c[1] - a[1]) > (b[1] - a[1]) * (c[0] - a[0])

def in_poly(p, points):
    # ray-casting algorithm based on
    # https://wrf.ecse.rpi.edu/Research/Short_Notes/pnpoly.html
    inside = False
    if len(points[0]) == 3:
        for i, (xi, yi, _) in enumerate(points):
            xj, yj, _= points[i - 1]  
            if ((yi > p[1]) != (yj > p[1])) and (p[0] < (xj - xi) * (p[1] - yi)
                                                / (yj - yi) + xi):
                inside = not inside  # an intersection was found
        return inside
    else:   
        for i, (xi, yi) in enumerate(points):
            xj, yj = points[i - 1]  
            if ((yi > p[1]) != (yj > p[1])) and (p[0] < (xj - xi) * (p[1] - yi)
                                                / (yj - yi) + xi):
                inside = not inside  # an intersection was found
        return inside
    
def get_ear(shape, ear):
    return (shape[ear - 1], shape[ear], shape[(ear+1) % len(shape)])


def poly_area(pts):
    area = 0.0
    for (ax, ay), (bx, by) in zip(pts, pts[1:] + [pts[0]]):
        area += ax * by
        area -= bx * ay
    return abs(area) / 2.0

py5.run_sketch(block=False)
