import py5
import pymunk

# my ugly triangulation & area code (TO DO: use shapely)
from triangulate import triangulate, poly_area

CT_DEFAULT = 0
CT_SPECIAL = 1
CT_WALL = 2

MINIMUM_DIST = 50
current_poly = [] # (x, y) tuples while mouse dragging
wall_start = None
drawing_dict = {}
save_filename = 'data.pickle'

def setup():
    global space
    py5.size(600, 600)
    space = pymunk.Space()
    space.gravity = 0, 900
    space.add_collision_handler(
        CT_SPECIAL, CT_DEFAULT
    ).pre_solve = color_collision
    add_wall(100, 500, 500, 500)

def draw():  # py5's main loop
    py5.background(0, 200, 100)  # R, G, B
    for item, (draw_func, kwargs) in list(drawing_dict.items()):
        draw_func(item, **kwargs)
        if item.body.position.y > py5.height + 50:
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
    x, y, fill=0, collision_type=CT_DEFAULT
    ):
    body = pymunk.Body(10, 100)
    body.position = x, y
    shape = pymunk.Circle(body, 10, (0, 0))
    shape.friction = 0.99
    shape.collision_type=collision_type
    space.add(body, shape)
    drawing_dict[shape] = (
        draw_circle,
        {'stroke': None, 'fill': fill}
        )

def add_wall(xa, ya, xb, yb):
    shape = pymunk.Segment(space.static_body,
                           (xa, ya), (xb, yb),
                           radius=1.5)
    shape.collision_type = CT_WALL
    shape.friction = 100.99
    space.add(shape)
    drawing_dict[shape] = (
        draw_static_segment,
        {'stroke': 128}
        )

def add_poly(poly):
    triangles = triangulate(poly)
    # this is bad, I should use shapely!
    (xa, ya), (xb, yb) = min_max(poly)
    cx, cy = (xa + xb) / 2, (ya + yb) / 2
    polys = []
    total_mass = total_moi = 0
    for tri in triangles:
        poly = [(x - cx, y - cy) for x, y in tri]
        mass = poly_area(poly) * 0.1
        total_mass += mass
        moi = pymunk.moment_for_poly(mass, poly)
        if not py5.np.isnan(moi):
            total_moi += moi
        polys.append(poly)   
    body = pymunk.Body(total_mass, total_moi)
    body.position = cx, cy
    shapes = []
    for poly in polys:
        shp = pymunk.Poly(body, poly)
        shp.friction = 0.2
        shapes.append(shp)
        drawing_dict[shp] = (
            draw_poly,
            {'stroke': None, 'fill': 255}
        )
    space.add(body, *shapes)  # Note critical * operator expands .add(b, s0, s1, s2...)
    

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

def draw_poly(shape,fill=255, stroke=None, weight=None):
    fill_and_stroke(fill, stroke, weight) 
    with py5.push_matrix():
        py5.translate(shape.body.position.x, shape.body.position.y)
        py5.rotate(shape.body.angle)
        pts = shape.get_vertices()
        with py5.begin_closed_shape():
            py5.vertices(pts)

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

py5.run_sketch(block=False)
