
rects = []

def setup():
    size(800, 800)
    rect_mode(CENTER)
    color_mode(HSB)
    stroke_weight(2)
    
def draw():
    background(200)
    for r in rects:
        x, y, w, h, (px, py) = r
        no_stroke()
        fill(w * 3, 200, h * 3)
        rect(x, y, w - 4 , h - 4)
        stroke(0)
        line(x, y, px, py)
        fill(200)
        
def key_pressed():
    if key == 'c':
        rects.clear()
    elif key == ' ':
        r = create_rect()
        while not check_rect(r):
            r = create_rect()
        rects.append(r)
        print(r)
    elif key == 's':
        #dsave_snapshot_and_code()
        save_frame('###.png')
           
def r_choice():
    return random_choice(((30, 60),
                          #(60, 60),
                             # (30, 30),
                          (60, 30)))


def create_rect():
    w, h = r_choice()
    hw, hh = w / 2, h / 2
    if not rects:
        ex, ey = x, y = width / 2, height / 2
    else:
        ex, ey, ew, eh, _ = random_choice(rects)
        hew, heh = ew / 2, eh / 2
        s = random_choice((0, 1, 2, 3))
        if s == 0:
            x = ex
            y = ey - heh - hh
        if s == 2:
            x = ex
            y = ey + heh + hh
        if s == 1:
            y = ey
            x = ex - hew - hw
        if s == 3:
            y = ey
            x = ex + hew + hw
    return x, y, w, h, (ex, ey)
            
def check_rect(r):
    x, y, w, h, _ = r
    if not (50 < x < width - 50 and 50 < y < height - 50):
        return False
    for other in rects:
        if rect_over_rect(*r, *other):
            return False
    return True
    
def rect_over_rect(x1, y1, w1, h1, _, x2, y2, w2, h2, __):
    # versão pelo centro, e sem contar borda!
    return (x1 + w1 / 2 > x2 - w2 / 2 and    # borda direita do r1 passa esquerda do r2 
            x1 - w1 / 2 < x2 + w2 / 2 and    # borda esquerda do r1 passa direita do r2
            y1 + h1 / 2 > y2 - h2/ 2 and    # topo do r1 avança sobre base do r2
            y1 - h1 / 2 < y2 + h2 / 2)       # base do r1 avança sobre topo do r2 
    

def save_snapshot_and_code():
    import shutil
    import datetime
    p = sketch_path()
    stamp = str(datetime.datetime.now()).replace(' ', '').replace(':', '').replace('.', '')    
    save(p / stamp / (stamp + '.png')) 
    shutil.copyfile(__file__, p / stamp / (stamp + '.py'))
    save(stamp + '.png')
