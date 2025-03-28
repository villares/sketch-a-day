# You'll need py5 and a use the run_sketch tool or Thonny + thonny-py5mode
# to run this py5 "imported mode" style sketch. Learn more at py5coding.org

def setup():
    size(600, 600)
    
def draw():
    background(100)
    stroke_weight(3)
    no_fill()
    stroke(255)
    #print(RU := mouse_x, R := mouse_y)
    RU = R = 200
    r = R * sqrt(3) / 2
    rbh =  r * sqrt(2)#mouse_x
    print(rbh)
    stroke(255, 60)
    circle(300, 300, rbh)
    circle(300, 300, rbh - 43)
    stroke(255)
    unit(300, 300, RU)
    unit(300 + r * 2, 300, RU)
    unit(300 - r * 2, 300, RU)
    hexagon(300 + r, 300 - R * 3 / 2, rbh, False)
    hexagon(300 - r, 300 - R * 3 / 2, rbh, False)
    hexagon(300 + r, 300 + R * 3 / 2, rbh, False)
    hexagon(300 - r, 300 + R * 3 / 2, rbh, False)
    hexagon(300, 300, rbh, False)
    hexagon(300 + r * 2, 300, rbh, False)
    hexagon(300 - r * 2, 300, rbh, False)



def unit(xu, yu, ru): 
    vs = hex_points(xu, yu, ru)
    for x, y in vs:
        hexagon(x, y, ru / 2)
        
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
