# Convertendo para Python o clipador de retângulos do John @Introscopia
# https://gist.github.com/Introscopia/e32720497e3c962874e3a3bd406cfa5e
# Usando py5 (https://py5coding.org) para a demo/teste

import py5

rects = []
drag_x = drag_y = None

def setup():
    py5.size(600, 800, py5.P3D)
    rects.append(Rect(50, 50, 500, 300))
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.color_mode(py5.HSB)
    
def draw():
    py5.background(0)
    py5.stroke(255)
    for i, r in enumerate(rects):
        py5.fill(r.c * 16, 100, 200, 200)
        py5.rect(r.x, r.y, r.w, r.h)
        py5.fill(255)
        py5.text(str(i), r.x + r.w / 2, r.y + r.h / 2)
        
    if drag_x:
        with py5.push_style():  # will revert rect_mode at context end
            py5.rect_mode(py5.CORNERS)
            py5.stroke(0, 255, 255)
            py5.no_fill()
            py5.rect(py5.mouse_x, py5.mouse_y, drag_x, drag_y)
          
    py5.translate(300, 600)
    py5.rotate_x(py5.QUARTER_PI)
    py5.translate(-300, -200)
    for i, r in enumerate(rects):
        py5.fill(r.c * 16, 100, 200)
        box_from_corner(r.x, r.y, 0, r.w, r.h, r.c * 16)
        

def box_from_corner(x, y, z, w, h, d):
    with py5.push_matrix():
        py5.translate(x + w / 2, y + h / 2, z + d / 2)
        py5.box(w, h, d)

def mouse_pressed():
    global drag_x, drag_y
    drag_x, drag_y = py5.mouse_x, py5.mouse_y

def mouse_released():
    global drag_x, drag_y
    sr = split_rects(rects, Rect(min(py5.mouse_x, drag_x), min(py5.mouse_y, drag_y),
                           abs(py5.mouse_x - drag_x), abs(py5.mouse_y - drag_y)))
    for r in sr:
        r.c += 1
    rects.extend(sr)
        
    drag_x = drag_y = None

def key_pressed():
    if py5.key == ' ':
        merge_rects()
    elif py5.key == 'r':
        rects[:] = [Rect(50, 50, 500, 300)]
        
class Rect:
    def __init__(self, x, y, w, h, c=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

def merge_rects(color_sensitive=True):
    
    def y_x(r):
        return r.y, r.x
    
    rects.sort(key=y_x)
    for i, r in enumerate(rects[:-1]):
        nr = rects[i + 1] # next rect
        aligned = r.y == nr.y and r.h == nr.h
        adjacent = r.x + r.w == nr.x
        color_match = not color_sensitive or r.c == nr.c        
        if aligned and adjacent and color_match:
            nr.x = r.x
            nr.w += r.w
            r.w = 0  # r will be removnred by clean_rects()
            
    clean_rects() # Filter out 0 area rects
           
           
def split_rects(rects: list[Rect], knife: Rect) -> list[Rect]:
    """
    Knife splits the area from the provided Rects, creating, resizing or
    removing axis aligned Rects (mutates the input). Returns a list of
    Rects inside the knife area. Preservers Rect .c (color) attribute.
    """
    s_rects = []
    
    if knife.w == 0 or knife.h == 0:
        return s_rects
    
    knife_r = knife.x + knife.w  # knife's right edge x
    knife_b = knife.y + knife.h  # knife's bottom edge y

    for r in rects[:]:  # iterating over a copy of rects
        r_r = r.x + r.w  # rect's right edge x
        r_b = r.y + r.h  # rect's bottom edge y

        if (knife.x >= r_r or
            knife.y >= r_b or
            knife_r <= r.x or
            knife_b <= r.y):
            continue  # not intersecting with knife

        top_in = knife.y > r.y and knife.y < r_b
        bot_in = knife_b > r.y and knife_b < r_b
        lef_in = knife.x > r.x and knife.x < r_r
        rig_in = knife_r > r.x and knife_r < r_r

        total = top_in + bot_in + lef_in + rig_in

        if total == 0:  # FULLY INSIDE
            s_rects.append(Rect(r.x, r.y, r.w, r.h, r.c))
            r.w = 0

        elif total == 1:  # RESIZE
            if top_in:
                s_rects.append(Rect(r.x, knife.y, r.w, r.h - (knife.y - r.y), r.c))
                r.h = knife.y - r.y
            elif bot_in:
                s_rects.append(Rect(r.x, r.y, r.w, r.h - (r_b - knife_b), r.c))
                r.y, r.h = knife_b, r_b - knife_b
            elif lef_in:
                s_rects.append(Rect(knife.x, r.y, r.w  - (knife.x - r.x), r.h, r.c))
                r.w = knife.x - r.x
            elif rig_in:
                s_rects.append(Rect(r.x, r.y, r.w  - (r_r - knife_r), r.h, r.c))
                r.x, r.w = knife_r, r_r - knife_r

        elif total == 2: # CORNERS AND SLICE THROUGH
            if rig_in and bot_in:  # top left corner clipped
                s_rects.append(Rect(r.x, r.y, knife_r - r.x, r.h - (r_b - knife_b), r.c))
                rects.append(Rect(r.x, knife_b, knife_r - r.x, r_b - knife_b, r.c))
                r.x, r.w = knife_r, r_r - knife_r
            elif lef_in and bot_in:  # top right corner clipped
                s_rects.append(Rect(knife.x, r.y, r_r - knife.x, r.h - (r_b - knife_b), r.c))
                rects.append(Rect(knife.x, knife_b, r_r - knife.x, r_b - knife_b, r.c))
                r.w = knife.x - r.x
            elif lef_in and top_in:  # bottom right corner clipped
                s_rects.append(Rect(knife.x, knife.y, r_r - knife.x, r.h - (knife.y - r.y), r.c))
                rects.append(Rect(knife.x, r.y, r_r - knife.x, knife.y - r.y, r.c))
                r.w = knife.x - r.x
            elif rig_in and top_in:  # bottom left corner clipped
                s_rects.append(Rect(r.x, knife.y, knife_r - r.x, r.h - (knife.y - r.y), r.c))
                rects.append(Rect(r.x, r.y, knife_r - r.x, knife.y - r.y, r.c))
                r.x, r.w = knife_r, r_r - knife_r
            elif lef_in and rig_in:  # vertical slice
                rects.append(Rect(knife_r, r.y, r_r - knife_r, r.h, r.c))
                r.w = knife.x - r.x
                s_rects.append(Rect(knife.x, r.y, knife.w, r.h, r.c))
            elif top_in and bot_in:  # horizontal slice
                rects.append(Rect(r.x, knife_b, r.w, r_b - knife_b, r.c))
                r.h = knife.y - r.y
                s_rects.append(Rect(r.x, knife.y, r.w, knife.h, r.c))

        elif total == 3:  # BITES
            if rig_in and bot_in and top_in:  # Left bite
                rects.append(Rect(r.x, r.y, knife_r - r.x, knife.y - r.y, r.c))
                rects.append(Rect(r.x, knife_b, knife_r - r.x, r_b - knife_b, r.c))
                s_rects.append(Rect(r.x, knife.y, knife_r - r.x, knife.h, r.c))
                r.x, r.w = knife_r, r_r - knife_r
            elif lef_in and bot_in and rig_in:  # top bite
                rects.append(Rect(knife.x, knife_b,  knife.w, r_b - knife_b, r.c))
                rects.append(Rect(knife_r, r.y, r_r - knife_r, r.h, r.c))
                s_rects.append(Rect(knife.x, r.y, knife.w, r.h - (r_b - knife_b), r.c))
                r.w = knife.x - r.x
            elif lef_in and top_in and bot_in:  # right bite
                rects.append(Rect(knife.x, r.y, r_r - knife.x, knife.y - r.y, r.c))
                rects.append(Rect(knife.x, knife_b, r_r - knife.x, r_b - knife_b, r.c))
                s_rects.append(Rect(knife.x, knife.y, r_r - knife.x, knife.h, r.c))
                r.w = knife.x - r.x
            elif rig_in and top_in and lef_in:  # bottom bite
                rects.append(Rect(knife.x, r.y, knife.w, knife.y - r.y, r.c))
                rects.append(Rect(knife_r, r.y, r_r - knife_r, r.h, r.c))
                s_rects.append(Rect(knife.x, knife.y, knife.w, r.h - (knife.y - r.y), r.c))
                r.w = knife.x - r.x

        elif total == 4: # HOLE
            rects.append(Rect(knife.x, r.y, knife.w, knife.y - r.y, r.c))
            rects.append(Rect(knife.x, knife_b,  knife.w, r_b - knife_b, r.c))
            rects.append(Rect(knife_r, r.y, r_r - knife_r, r.h, r.c))
            r.w = knife.x - r.x
            s_rects.append(Rect(knife.x, knife.y, knife.w, knife.h, r.c))

    clean_rects() # Filter out 0 area rects
    return s_rects

def clean_rects():
    rects[:] = [r for r in rects if r.w * r.h != 0]


py5.run_sketch()


