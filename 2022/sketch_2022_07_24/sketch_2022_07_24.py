from itertools import chain

#s = 1000

def setup():
    size(600, 600)
    #random_seed(s)
    first_rectangle()
    for _ in range(3):
        rects[:] = divide_rectangles(rects)
    
def first_rectangle(margin=57):
    global rects
    rects = [(margin, margin, width - margin * 2, height - margin * 2)]
    
def draw():
    background(0)
    for (xa, ya, wa, ha), (xb, yb, wb, hb) in zip(rects, reversed(rects)):
        stroke((ya * xa) % 255, (yb * xb % 255), (xa + xb) % 255, 32)
        line(xa, ya, yb, yb)
        
def key_pressed():
    if key == ' ':
        rects[:] = divide_rectangles(rects)
        print('\n'.join(str(r) for r in rects[:20]))
    elif key == 'n':
        #random_seed(s)
        first_rectangle()
    elif key == 's':
        save_frame('sketch_2022_07_24.png')
        
def divide_rectangles(rectangles):
    return sorted(chain.from_iterable(divide_rectangle(r) for r in rectangles),
                  key=lambda r: r[1] * r[0] )
    
    
def divide_rectangle(r):
    xa, ya, w, h = r
    wa = wb = wc = w / 3
    ha = hb = hc = h / 3
    xb = xa + wa
    yb = ya + ha
    xc = xa + wa + wb
    yc = ya + ha + hb
#    if random(100) > 1:
    return (
        (xa, ya, wa, ha), (xb, ya, wb, ha), (xc, ya, wc, ha),
        (xa, yb, wa, hb),                   (xc, yb, wc, hb),
        (xa, yc, wa, hc), (xb, yc, wb, hc), (xc, yc, wc, hc),
        )                      
#     else:
#         return reversed((
#            (xa, ya, wa, ha), (xb, ya, wb, ha), (xc, ya, wc, ha),
#            (xa, yb, wa, hb),                   (xc, yb, wc, hb),
#            (xa, yc, wa, hc), (xb, yc, wb, hc), (xc, yc, wc, hc),
#         ))                        
