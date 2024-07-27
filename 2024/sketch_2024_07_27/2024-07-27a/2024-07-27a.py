# You'll need py5 and a use the run_sketch tool or Thonny + thonny-py5mode
# to run this py5 "imported mode" style sketch. Learn more at py5coding.org
import shapely

def setup():
    size(600, 600)
    stroke_weight(3)
    stroke_join(ROUND)
    no_fill()
    
def draw():
    background(0)
    stroke(255)
    unit(300, 300, 180, 12)
    
def unit(xu, yu, r, n=6):
    vs = poly_points(xu, yu, r, n)
    unit_vs = []
    for i, (x, y) in enumerate(vs):
        svs = poly_points(x, y, r / 2, n)
        no_fill()
        with begin_closed_shape():
            vertices(svs)
        fill(255, 100)
        if i % 2 == 0:
            unit_vs.append(svs[(n//2+i)%n])
        else:
            with begin_closed_shape():
                for j in range(n-1, n+2): #5, 8):
                    unit_vs.append(svs[(i + j) % len(svs)])
    with begin_closed_shape():
        vertices(unit_vs)

    
    
def poly_points(x, y, cr, n=6, half_rot=True):
    # cr is the circumradius for hex
    # ir = cr * cos(TAU / 12)  # to be confirmed
    # a = cr * 2 * sin(TAU / 12) # to be confirmed
    ang = TAU / n
    return [(x + cos(i * ang + half_rot * ang / 2) * cr,
             y + sin(i * ang + half_rot * ang / 2) * cr)
           for i in range(n)]


def key_pressed():
    #save_frame('out.png')
    save_snapshot_and_code()
    
def save_snapshot_and_code():
    import shutil
    import datetime
    p = sketch_path()
    stamp = str(datetime.datetime.now()).replace(' ', '-').replace(':', '').replace('.', '')    
    save(p / stamp / (stamp + '.png')) 
    shutil.copyfile(__file__, p / stamp / (stamp + '.py'))
    save(stamp + '.png')