# You'll need py5 and a use the run_sketch tool or Thonny + thonny-py5mode
# to run this py5 "imported mode" style sketch

def setup():
    size(600, 600)
    rect_mode(CENTER)
    
def draw():
    background(0)
    w = 100
    for x in range(5):
        for y in range(5):
            unit(w + x * w,
                 w + y * w, w)
        
def unit(x, y, w):
    # w = r * 2 + r * 2 / (1 + sqrt(2))
    r = w / (2 * sqrt(2))  # octagon inradius
    s = r * 2 / (1 + sqrt(2)) # square side
    # square(x, y, w)  # visual debug
    offset = - r * sqrt(2) / 2
    poly(x + offset, y + offset, r, 8)
    poly(x + r + s / 2 + offset,
           y + offset, s / 2, 4)
    poly(x + w / 2 + offset, y + w / 2 + offset, r, 8)
    poly(x - r - s / 2 + w / 2 + offset,
           y + w / 2 + offset, s / 2, 4)
    # circle(x, y, 5)  # visual debug
    
def poly(x, y, r, n):
    # inradius
    # r = R * cos(PI / 8)
    if n == 8:
        R = r / cos(PI / 8) # octagon circumradius
    elif n == 4:
        R = r * sqrt(2)
    else:
        return
    ang = TAU / n
    with begin_closed_shape():
        for i in range(n):
            vx = x + cos(i * ang + ang / 2) * R 
            vy = y + sin(i * ang + ang / 2) * R
            vertex(vx, vy)
 
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