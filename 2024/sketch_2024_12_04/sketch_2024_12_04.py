import py5
import shapely

V = py5.Py5Vector
seed = 1

def setup():
    py5.size(500, 500)
    py5.stroke_cap(py5.SQUARE)

def draw():
    py5.random_seed(seed)
    py5.background(240, 240, 200)
    for _ in range(10):
        margin = py5.width / 10
        ox = py5.random(margin, py5.width - margin)
        oy = py5.random(margin * 2, py5.height)
        bh = py5.sqrt(oy * 2) * 2
        branch(V(ox, oy), V(0, -bh))

def branch(origin, v):
    end = origin + v
    py5.stroke_weight(v.mag / 8)
    py5.line(origin.x, origin.y, end.x, end.y)
    shorten = 0.9 - py5.random(0.3)
    ang = py5.radians(22)
    if v.mag > 5:
        ra = ang + (py5.random(2) - 1) / 6
        branch(end, v.copy.rotate(ra) * shorten)
        branch(end, v.copy.rotate(-ra) * shorten)

def key_pressed():
    global seed
    py5.save_frame(f'{seed}.png')
    seed += 1

py5.run_sketch(block=False)      