# You'll need py5 and a use the run_sketch tool or Thonny + thonny-py5mode
# to run this py5 "imported mode" style sketch. Learn more at py5coding.org

def setup():
    size(600, 600)
    
def draw():
    background(100)
    stroke_weight(3)
    no_fill()
    stroke(255)
    RU = R = 300
    r = R * sqrt(3) / 2
    unit(300, 300, RU)


def unit(xu, yu, ru): 
    vs = regular_poly_points(xu, yu, ru / 2, 6)
    for i, (x, y) in enumerate(vs):
        tri(x, y, ru / 2, radians(60) * (i + 1))


def tri(x, y, r, angle=0):
    stroke_join(ROUND)
    fill(100, 200, 100)
    vs = regular_poly_points(x, y, r, 3, angle)
    with begin_closed_shape():
            vertices(vs)
    fill(128)
    svs = regular_poly_points(x, y, r / 2, 3, angle + radians(60))
    with begin_closed_shape():
            vertices(svs)
    fill(100, 100, 200)
    svs = regular_poly_points(x, y, r / 4, 3, angle)
    with begin_closed_shape():
            vertices(svs)
    fill(200, 100, 100)
    circle(*svs[0], 10)


def hexagon(x, y, r, pointy=False):
    vs = regular_poly_points(x, y, r, 6, pointy * radians(30))
    with begin_closed_shape():
            vertices(vs)

def regular_poly_points(x, y, cr, N, rot=0):
    # cr is the circumradius
    ang = TAU / N
    return [(x + cos(i * ang + rot) * cr,
             y + sin(i * ang + rot) * cr)
           for i in range(N)]

def key_pressed():
    save_snapshot_and_code()
    
def save_snapshot_and_code():
    import shutil
    p = sketch_path()
    N = f'{len(list(p.iterdir())):03d}'
    save(p / N / (N + '.png')) 
    shutil.copyfile(__file__, p / N / (N + '.py'))
