# You'll need py5 and a use the run_sketch tool or Thonny + thonny-py5mode
# to run this py5 "imported mode" style sketch. Learn more at py5coding.org

palete = []

def setup():
    size(600, 600)
    no_loop()

def draw():
    background(100)
    stroke_weight(3)
    no_fill()
    stroke(255)
    palete[:] = [color(random_int(255), random_int(255), random_int(255))
                 for _ in range(4)]
    RU = R = 300
    #r = R * sqrt(3) / 2
    unit(300, 300, RU)



def unit(xu, yu, ru): 
    vs = regular_poly_points(xu, yu, ru / 2, 6)
    for i, (x, y) in enumerate(vs):
        tri(x, y, ru / 2, radians(60) * (i + 1))


def tri(x, y, r, angle=0):
    stroke_join(ROUND)
    evs = regular_poly_points(x, y, r, 3, angle)
#     with begin_closed_shape():
#             vertices(evs)
#     fill(128)
#     svs = regular_poly_points(x, y, r / 2, 3, angle + radians(60))
#     with begin_closed_shape():
#             vertices(svs)
    fill(palete[-1])
    ivs = regular_poly_points(x, y, r / 4, 3, angle)
    with begin_closed_shape():
            vertices(ivs)
#     for a, b in zip(evs, ivs):
#         line(*a, *b)
    for i in range(3):
        fill(palete[i])
        a = evs[i]
        b = evs[i - 1]
        c = ivs[i - 1]
        d = ivs[i]
        quad(*a, *b, *c, *d)
        


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
    if key == ' ':
        redraw()
    elif key == 'S':
        save_snapshot_and_code()
    elif key == 's':
        save(__file__[:-3]+'.png')
    
def save_snapshot_and_code():
    import shutil
    p = sketch_path()
    n = Path(__file__[:-3]+'.png').is_file()
    N = f'{len(list(p.iterdir()))-n:03d}'
    save(p / N / (N + '.png')) 
    shutil.copyfile(__file__, p / N / (N + '.py'))
