# You'll need py5 and a use the run_sketch tool or Thonny + thonny-py5mode
# to run this py5 "imported mode" style sketch. Learn more at py5coding.org

R = 150
r = R * sqrt(3) / 2


def setup():
    size(600, 600)
    background(100)
    stroke_weight(3)
    no_fill()
    stroke(255)
    vs = hex_points(300, 300, R + R / 2, False)
    for tx, ty in vs:
        hexagon(tx, ty, (R / 2) * (sqrt(3)/2) * 2.4, False)
    #hexagon(300, 300, (R / 2) * (sqrt(3)/2) * 3, False)

    vs = hex_points(300, 300, R)
    for x, y in vs:
        hexagon(x, y, R / 2)
        
def hexagon(x, y, r, pointy=True):
    vs = hex_points(x, y, r, pointy)
    with begin_closed_shape():
            vertices(vs)

def hex_points(x, y, cr, pointy=True):
    # cr is the circumradius
    ang = TAU / 6
    return [(x + cos(i * ang + pointy * ang / 2) * cr,
             y + sin(i * ang + pointy * ang / 2) * cr)
           for i in range(6)]

def key_pressed():
    save_snapshot_and_code()
    
def save_snapshot_and_code():
    import shutil
    p = sketch_path()
    N = f'{len(list(p.iterdir())):03d}'
    save(p / N / (N + '.png')) 
    shutil.copyfile(__file__, p / N / (N + '.py'))
