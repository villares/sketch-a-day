tris = []
unvisited_tris = set()


def setup():
    size(600, 600)
    inicial = ((0, -10), (0, 10), (15, 0))
    #profile_growall()



def draw():
    background(0)
    translate(width / 2, height / 2)
    stroke(255, 64)
    fill(190, 100, 200, 100)
    for t in tris:
        begin_shape()
        for x, y in t:
            vertex(x, y)
        end_shape(CLOSE)


def mouse_dragged():
    ox, oy = width / 2, height / 2
    drag = ((mouse_x - ox, mouse_y - oy), (pmouse_x - ox, pmouse_y - oy))
    unvisited_tris.add(drag)
    tris.append(drag)


def key_pressed():
    growall()
    
def growall():    
#     for t in list(unvisited_tris):
#         grow(t)
    map(grow,  list(unvisited_tris))
    print(len(tris))  # , len(visited_tris)



def mouse_pressed():
    if mouse_button == RIGHT:
        print_line_profiler_stats()

def grow(t):
    edges = get_edges(t)
    unvisited_tris.remove(t)
    for e in edges:
        e0, e1 = e[0], e[1]
        a = edge_angle(e)
        m = midpoint(e)
        d = edge_dist(e) * 0.87
        p = point_offset(m, d, a - HALF_PI)
        if not point_in_tris(p):
            n = (e0, p, e1)
            tris.append(n)
            unvisited_tris.add(n)


def get_edges(t):
    t0 = t[0]
    return [
        ((xa, ya), (xb, yb)) for (xa, ya), (xb, yb) in zip(t, t[1:] + (t0,))
    ]


def edge_angle(edge):
    (xa, ya), (xb, yb) = edge
    return atan2(yb - ya, xb - xa) + PI


def point_offset(p, offset, angle):
    return (int(p[0] + offset * cos(angle)), int(p[1] + offset * sin(angle)))


def point_in_tris(p):
    x, y = p
    p_in_t = lambda t: point_inside_poly(x, y, t)
    return any(map(p_in_t, tris))


def point_inside_poly(x, y, points):
    # ray-casting algorithm based on
    # https://wrf.ecse.rpi.edu/Research/Short_Notes/pnpoly.html
    inside = False
    for i, p in enumerate(points):
        pp = points[i - 1]
        xi, yi = p
        xj, yj = pp
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
    return inside


def edge_dist(edge):
    (xa, ya), (xb, yb) = edge
    return dist(xa, ya, xb, yb)


def midpoint(edge):
    (xa, ya), (xb, yb) = edge
    return (xa + xb) / 2.0, (ya + yb) / 2.0
