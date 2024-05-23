
circles = []

def setup():
    size(800, 800)
    #color_mode(HSB)
    stroke_weight(2)
    
def draw():
    background(200)
    for r in circles:
        x, y, w, h, (px, py), c = r
        no_stroke()
        fill(w * 3, c % 255, h * 3)
        circle(x, y, w - 4)
        stroke(0)
        line(x, y, px, py)
        fill(200)
        
def key_pressed():
    if key == 'c':
        circles.clear()
    elif key == ' ':
        add_circle()
        save_frame(f'{frame_count:0>5}.png')
    elif key == 's':
        #dsave_snapshot_and_code()
        save_frame('s###.png')
           
def r_choice():
    return random_choice(((30, 60),
                          #(60, 60),
                             # (30, 30),
                          (60, 30)))


def add_circle():
    if not circles:
        circles.append(create_circle())
    else:
        for base in circles:
            r = create_circle(base)
            if check_circle(r):
                circles.append(r)
    print(len(circles))

def create_circle(base_circle=None):
    w, h = r_choice()
    hw, hh = w / 2, h / 2
    if base_circle is None:
        ex, ey = x, y = width / 2, height / 2
        c = 0
    else:
        ex, ey, ew, eh, _, c = base_circle
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
    return x, y, w, h, (ex, ey), c + 25
            
def check_circle(r):
    x, y, w, h, _, _ = r
    if not (50 < x < width - 50 and 50 < y < height - 50):
        return False
    for other in circles:
        if circle_over_circle(*r, *other):
            return False
    return True
    
def circle_over_circle(x1, y1, w1, h1, _0, _1 , x2, y2, w2, h2, _2, _3):
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
