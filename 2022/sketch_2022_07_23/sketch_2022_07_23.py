from itertools import chain

#s = 1000

def setup():
    size(600, 600)
    #random_seed(s)
    first_rectangle()
    for _ in range(5):
        rects[:] = divide_rectangles(rects)
    
def first_rectangle(margin=57):
    global rects
    rects = [(margin, margin, width - margin * 2, height - margin * 2)]
    
def draw():
    background(0, 100, 0)
    no_stroke()
    for x, y, w, h in rects:
        #rect(x + 0.5, y + 0.5, w - 1, h - 1)
        rect(x, y, w, h)
        
def key_pressed():
    if key == ' ':
        rects[:] = divide_rectangles(rects)
    elif key == 'n':
        #random_seed(s)
        first_rectangle()
    elif key == 's':
        save_frame('sketch_2022_07_23.png')
        
def divide_rectangles(rectangles):
    return chain.from_iterable(divide_rectangle(r) for r in rectangles)
    
def divide_rectangle(r):
    xa, ya, w, h = r
    wa = wb = wc = w / 3
    ha = hb = hc = h / 3
    xb = xa + wa
    yb = ya + ha
    xc = xa + wa + wb
    yc = ya + ha + hb
    return (
        (xa, ya, wa, ha), (xb, ya, wb, ha), (xc, ya, wc, ha),
        (xa, yb, wa, hb),                   (xc, yb, wc, hb),
        (xa, yc, wa, hc), (xb, yc, wb, hc), (xc, yc, wc, hc),
        )                        

