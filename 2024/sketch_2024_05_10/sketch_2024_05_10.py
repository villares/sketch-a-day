
rects = []

def setup():
    size(800, 800)
    rect_mode(CENTER)
    fill(255, 100)
    
def draw():
    background(200)
    for r in rects:
        rect(*r)
        
def key_pressed():
    if key == 'c':
        rects.clear()
    elif key == ' ':
        create_rect()
    
def r_choice():
    return (
        random_choice((50, 100, 200)), 
        random_choice((50, 100, 200)) 
    )


def create_rect():
    w, h = r_choice()
    hw, hh = w / 2, h / 2
    if not rects:
        x, y = width / 2, height / 2
    else:
        ex, ey, ew, eh = random_choice(rects)
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
    rects.append((x, y, w, h))
            
            


    
    