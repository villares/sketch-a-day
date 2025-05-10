import py5

V = py5.Py5Vector
right = V(1, 0)
up60d = V(1, 0).rotate(py5.radians(-60))
down30d = V(1, 0).rotate(py5.radians(+30))
down = V(0, 1)

def setup():
    py5.size(450, 450)
    u_offset = right + down30d
    v_offset = down - up60d
    side = 90
    for col in range(4):
        for row in range(4):
            pos = col * u_offset * side + row * v_offset * side
            group(pos.x, pos.y - side, side)
    
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
