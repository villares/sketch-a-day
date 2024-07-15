

def setup():
    size(800, 800)
    rect_mode(CENTER)
    
def draw():
    background(0)
    w = 141.42
    for x in range(6):
        unit(x * w, 400, 50)
        unit(x * w + w / 2, 482.8, 50)
        
def unit(x, y, w):
    s = oct(x, y, w)
    square(x + w + s / 2, y, s)
    
def oct(x, y, r):
    # inradius
    # r = R * cos(PI / 8)
    R = r / cos(PI / 8) # circumradius
    ang = TAU / 8
    with begin_closed_shape():
        for i in range(8):
            vx = x + cos(i * ang + ang / 2) * R 
            vy = y + sin(i * ang + ang / 2) * R
            vertex(vx, vy)
    return r * 2 / (1 + sqrt(2)) # side
 
def key_pressed():
    save_snapshot_and_code()
    
def save_snapshot_and_code():
    import shutil
    import datetime
    p = sketch_path()
    stamp = str(datetime.datetime.now()).replace(' ', '-').replace(':', '').replace('.', '')    
    #save(p / stamp / (stamp + '.png')) 
    #shutil.copyfile(__file__, p / stamp / (stamp + '.py'))
    save(stamp + '.png')