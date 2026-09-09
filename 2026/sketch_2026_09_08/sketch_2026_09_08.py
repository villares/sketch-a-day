import py5
from py5_tools import animated_gif
from shapely import Point


keys = set()
X_ROT = 0
GRID_N = 25
offset_x = offset_y = 100
rnd_seed = 1
mode = 0

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
    py5.size(600, 600, py5.P3D)
    py5.no_smooth()
    py5.no_fill()  # sem preenchimento
    py5.stroke_weight(3)
    py5.frame_rate(12)
    animated_gif('out.gif',  duration=0.2, frame_numbers=range(1, 241, 4))

def draw():
    global offset_x, offset_y, si, ei, sj, ei
    base_spacing = int(py5.width / (GRID_N + 0.01))
    cell_size = base_spacing
    py5.background(0)
    py5.random_seed(rnd_seed)
    #py5.rotate_x(py5.radians(py5.mouse_y)) 

    t = (py5.frame_count % 241) / 240
    st = py5.sin(py5.remap(t, 0, 1, 0, py5.TWO_PI))    
    ct = py5.cos(py5.remap(t, 0, 1, 0, py5.TWO_PI))    
    g = py5.constrain(py5.remap(st, -1, 1, 0, 1), 0, 1)
    f = py5.constrain(py5.remap(ct, -1, 1, 0, 1), 0, 1)
    #print(g)

    v = py5.remap(f, 1, 0, base_spacing * 1.5, base_spacing * py5.sqrt(3))
    h = base_spacing * py5.sqrt(3) #remap(f, 1, 0, base_spacing * sqrt(3), base_spacing * 2)
    
    if mode == 1:
        py5.stroke(255)
        py5.shape(p)
        py5.circle(ip.x, ip.y, 10)
    elif mode == 0:
        for i in range(GRID_N):  # um i p/ cada coluna
            for j in range(GRID_N): # um j p/ cada linha
                if j % 2:
                    x = i * h + (f * h / 4) 
                else:
                    x = i * h - (f * h / 4) 
                y = j * v
                vp = poly(
                    0, 0,
                    base_spacing, 6,
                    rot=f * py5.radians(30),
                    #rnd=g * 20
                )
                vq = rquad(0, 0, h,
                    #rnd=g * 20
                )
                for s in range(1, 6):
                    with py5.push_matrix():
                        py5.translate(x + py5.random(-20, 20) * (1-f),
                                      y + py5.random(-20, 20) * (1-f),
                                      (1-f) * 50 * s)
                        sf = py5.remap(g, 0, 1, 1/s, 1)
                        py5.scale(sf)
                        py5.no_fill()
                        py5.stroke_weight(4)
                        py5.stroke(cores_t[s-1])
                        with py5.begin_closed_shape():
                            py5.vertices(lerp_poly(reversed(vq), vp, f))

    if py5.LEFT in keys:
        offset_x -= 2
    if py5.RIGHT in keys:
        offset_x += 2
    if py5.UP in keys:
        offset_y -= 2
    if py5.DOWN in keys:
        offset_y += 2


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
    elif py5.key == py5.CODED:
        keys.add(py5.key_code)

    print(offset_x, si, ei)

def key_released():
    if py5.key == py5.CODED:
        keys.discard(py5.key_code)

# def mouse_wheel(e):
#     global grid_offset
#     grid_offset = max(0, grid_offset + e.get_count())


py5.run_sketch()



