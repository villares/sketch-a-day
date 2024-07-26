# You'll need py5 and a use the run_sketch tool or Thonny + thonny-py5mode
# to run this py5 "imported mode" style sketch. Learn more at py5coding.org

R = 150

def setup():
    size(600, 600)
    stroke_weight(3)
    stroke_join(ROUND)
    no_fill()
    
def draw():
    background(0)
    unit(300, 300, 200, 100)
#    unit(300, 300, mouse_x, mouse_y)
    
def unit(xu, yu, s1, s2):
    vs = hex_points(xu, yu, s1)
    stroke(255)
    #with begin_closed_shape():
    #    vertices(vs)
    for i, (x, y) in enumerate(vs):
        svs = hex_points(x, y, s2)
        no_fill()
        with begin_closed_shape():
            vertices(svs)
        fill(255, 100)
        if i % 2 == 0:
            circle(*svs[(3+i)%6], 10)
        else:
            with begin_closed_shape():
                for j in range(5, 8):
                    vertex(svs[(i + j) % len(svs)])
    
def hex_points(x, y, cr, pointy=True):
    # cr is the circumradius
    # ir = cr * cos(TAU / 12)  # to be confirmed
    # a = cr * 2 * sin(TAU / 12) # to be confirmed
    ang = TAU / 6
    return [(x + cos(i * ang + pointy * ang / 2) * cr,
             y + sin(i * ang + pointy * ang / 2) * cr)
           for i in range(6)]


def key_pressed():
    save_frame('out.png')
    
def save_snapshot_and_code():
    import shutil
    import datetime
    p = sketch_path()
    stamp = str(datetime.datetime.now()).replace(' ', '-').replace(':', '').replace('.', '')    
    #save(p / stamp / (stamp + '.png')) 
    #shutil.copyfile(__file__, p / stamp / (stamp + '.py'))
    save(stamp + '.png')