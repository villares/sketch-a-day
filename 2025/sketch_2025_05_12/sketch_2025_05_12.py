import py5
from py5_tools import animated_gif

V = py5.Py5Vector
right = V(1, 0)
down = V(0, 1)

def setup():
    py5.size(450, 450)
    py5.no_stroke()
    animated_gif('out.gif', duration=0.2, frame_numbers=range(1, 361, 5))

def draw():
    global up60d, down30d
    a = 30 - py5.frame_count
    up60d = V(1, 0).rotate(py5.radians(-90 + a))
    down30d = V(1, 0).rotate(py5.radians(a))
    u_offset = right + down30d
    v_offset = down - up60d
    side = 90
    for col in range(-4, 4):
        for row in range(-4, 4):
            pos = col * u_offset * side + row * v_offset * side
            group(pos.x + py5.width / 2, pos.y + py5.height / 2, side)
    
def group(x, y, u):
    a = V(x, y)
    b = a + up60d * u
    c = a + right * u
    d = c + up60d * u
    e = d + down30d * u
    f = c + down30d * u
    g = c + down * u
    h = g + down30d * u
    i = a + down * u
    py5.fill(200, 0, 0)
    poly(a, b, c)
    py5.fill(250, 100, 100)
    poly(b, d, c)
    py5.fill(0, 0, 200)
    poly(c, d, e, f)
    py5.fill(0, 200, 0)
    poly(c, f, g)
    py5.fill(100, 250, 100)
    poly(f, g, h)
    py5.fill(100, 100, 250)
    poly(a, c, g, i)

def poly(*pts):
    with py5.begin_closed_shape():
        py5.vertices(pts)

def key_pressed():
    save_frame('###.png')

py5.run_sketch()    
