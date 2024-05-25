
circles = []

def setup():
    size(800, 800)
    #color_mode(HSB)
    stroke_weight(2)
    
def draw():
    background(240)
    for r in circles:
        x, y, d, (px, py), c = r
        no_stroke()
        fill(255 - d * 3, c % 255, d * 3)
        circle(x, y, d)
        stroke(0)
        line(x, y, px, py)
        fill(200)
        
def key_pressed():
    if key == 'c':
        circles.clear()
    elif key == ' ':
        add_circle()
        #save_frame(f'{frame_count:0>5}.png')
    elif key == 's':
        save_snapshot_and_code()
    elif key == 'p':
        save_frame('s###.png')
           
def c_choice():
    return random_choice((15, 30, 60))


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
    d = c_choice()
    hw, hh = d / 2, d / 2
    if base_circle is None:
        ex, ey = x, y = width / 2, height / 2
        a = c = 0
    else:
        ex, ey, ed, _, c = base_circle
        hew = heh = ed / 2
        a = random_choice(range(8)) # 3, 4))
        #b = c / 55
        ang = (TWO_PI / 8) * a
        x = ex + cos(ang) * (ed / 2 + d / 2) 
        y = ey + sin(ang) * (ed / 2 + d / 2) 
    return x, y, d, (ex, ey), a * 55 # c + 12
            
def check_circle(circ):
    x, y, d, _, _ = circ
    if not (50 < x < width - 50 and 50 < y < height - 50):
        return False
    for other in circles:
        if circle_over_circle(*circ, *other):
            return False
    return True
    
def circle_over_circle(x1, y1, d1, _0, _1 , x2, y2, d2, _2, _3):    
    d = dist(x1, y1, x2, y2)
    return d < (d1 / 2 + d2 / 2)

def save_snapshot_and_code():
    import shutil
    import datetime
    p = sketch_path()
    stamp = str(datetime.datetime.now()).replace(' ', '-').replace(':', '').replace('.', '')    
    save(p / stamp / (stamp + '.png')) 
    shutil.copyfile(__file__, p / stamp / (stamp + '.py'))
    save(p / stamp / (stamp + '.png'))
