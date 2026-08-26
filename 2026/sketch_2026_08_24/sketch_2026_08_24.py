import py5
from shapely import Point

p = Point(256, 256).buffer(400) | Point(384, 384).buffer(400)


GRID_N = 15
rnd_seed = 1
grid_offset = 0

cores_b = (
    '#fec31c',
    '#f15628',
    '#d1212b',
    )
cores_a = (
    '#21a5a8',
    '#1f79ac',
    '#174a92',
    )
cores_t = cores_a + cores_b


def setup():
    py5.size(1280, 720, py5.P3D)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.no_fill()  # sem contorno
    py5.stroke_weight(3)

def draw():
    py5.background(0)
    py5.random_seed(rnd_seed)

    t = (py5.frame_count % 101) / 100
    v = p.exterior.interpolate(t, normalized=True)
    
    f = py5.constrain(py5.remap(v.x, 50, py5.width - 50, 0, 1), 0, 1)
    g = py5.constrain(py5.remap(v.y, 40, py5.height - 50, 0, 1), 0, 1)
    base_spacing = int(py5.width / (GRID_N + 0.01))

    v = py5.remap(f, 1, 0, base_spacing * 1.5, base_spacing * py5.sqrt(3))
    h = base_spacing * py5.sqrt(3) #remap(f, 1, 0, base_spacing * sqrt(3), base_spacing * 2)
    for i in range(GRID_N):  # um i p/ cada coluna
        for j in range(GRID_N): # um j p/ cada linha
            if j % 2:
                x = i * h + (f * h / 4) 
            else:
                x = i * h - (f * h / 4) 
            y = j * v
            n = 6 #8 - int(3 * f)
            vp = poly(
                py5.random(-5, 5) * grid_offset,
                py5.random(-5, 5) * grid_offset,
                base_spacing, 6,
                rot=f * py5.radians(30),
                #rnd=g * 20
            )
            vq = rquad(0, 0, h,
                #rnd=g * 20
            )
            for s in range(1, 6):
                with py5.push_matrix():
                    py5.translate(x, y)
                    sf = py5.remap(g, 0, 1, 1 / s, 1)
                    py5.scale(sf)
                    py5.stroke_weight(3/sf)
                    py5.stroke(cores_t[s-1])
                    with py5.begin_closed_shape():
                        py5.vertices(lerp_poly(reversed(vq), vp, f))


def lerp_poly(p0, p1, t):
    """Create interpolated version of poly - using tuples for points """
    return [tuple(py5.lerp(c0, c1, t) for c0, c1 in zip(sp0, sp1))
            for sp0, sp1 in zip(p0, p1)]


def rquad(x, y, w, rnd=0):
    vertices_base = [
        (x + w / 2, y - w / 2),
        (x + w / 2, y - w / 2),
        (x - w / 2, y - w / 2),
        (x - w / 2, y + w / 2),
        (x - w / 2, y + w / 2),
        (x + w / 2, y + w / 2),
    ]
    vs = []
    for cx, cy in vertices_base:
        ox, oy = py5.random(-rnd, rnd), py5.random(-rnd, rnd)
        vs.append((cx + ox, cy + oy))
    return vs
    
    
def poly(x, y, r, n=6, rot=0, rnd=0):
    vs = []
    for i in range(n):
        ox, oy = py5.random(-rnd, rnd), py5.random(-rnd, rnd)
        sx = x + py5.cos(i * py5.TWO_PI / n + rot) * r + ox
        sy = y + py5.sin(i * py5.TWO_PI / n + rot) * r + oy
        vs.append((sx, sy))
    return vs

def key_pressed():
    global rnd_seed
    if py5.key == ' ':
        rnd_seed += 1
    elif py5.key == 's':
        py5.save_frame('####.png')

def mouse_wheel(e):
    global grid_offset
    grid_offset = max(0, grid_offset + e.get_count())


py5.run_sketch()

