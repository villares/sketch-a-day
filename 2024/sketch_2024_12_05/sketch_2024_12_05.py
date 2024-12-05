import py5
import shapely

from villares.arcs import var_bar_pts

V = py5.Py5Vector
seed = 1

def setup():
    py5.size(500, 500)
    py5.no_loop()

def draw():
    py5.random_seed(seed)
    py5.background(200, 240, 255)
    polys = branch(V(250, 500), V(0, -100))
    #ss = shapely.MultiPolygon(polys)
    tree = shapely.unary_union(polys)
    clip_rect = shapely.Polygon(((100,100), (400, 100), (400, 400), (100, 400)))
    clipped_tree = tree.intersection(clip_rect)
    py5.no_stroke()
    py5.fill(0, 200)
    py5.shape(py5.convert_cached_shape(clipped_tree))

# def my_line(xa, ya, xb, yb, w=1):
#     return shapely.LineString(((xa, ya), (xb, yb))).buffer(w)
def t_line(xa, ya, xb, yb, wa, wb):
    return shapely.Polygon(var_bar_pts(xa, ya, xb, yb, wa / 2, wb / 2,
                                       num_points=1))


def branch(origin, v):
    polys = []
    end = origin + v
    sw = v.mag / 5 # stroke weight
    shorten = 0.9 - py5.random(0.3)
    polys.append(t_line(origin.x, origin.y, end.x, end.y, sw, sw * shorten))
    ang = py5.radians(22)
    if v.mag > 5:
        ra = ang + (py5.random(2) - 1) / 6
        polys.extend(branch(end, v.copy.rotate(ra) * shorten))
        polys.extend(branch(end, v.copy.rotate(-ra) * shorten))
    return polys
    
def key_pressed():
    global seed
    py5.save_frame(f'{seed}.png')
    seed += 1
    py5.redraw()

py5.run_sketch(block=False)      