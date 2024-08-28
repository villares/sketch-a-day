# You'll need py5 and a use the run_sketch tool or Thonny + thonny-py5mode
# to run this py5 "imported mode" style sketch. Learn more at py5coding.org

R = 150

def setup():
    size(600, 600)
    background(100)
    stroke_weight(3)
    no_fill()
    stroke(255)
    vs = hex_points(300, 300, R)
#     with begin_closed_shape():
#         vertices(vs)
    for x, y in vs:
        svs = hex_points(x, y, R / 2)
        with begin_closed_shape():
            vertices(svs)
    
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
