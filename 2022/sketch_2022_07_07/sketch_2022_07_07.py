

def setup():
    size(800, 1000)
    rect_mode(CENTER)
    no_stroke()
    step = 40
    hs = step / 2
    speed = 1 / 150
    for y in range(20, height, step): 
        for x in range(20, width, step):
            w = hs + hs * cos(x * speed) * 0.75
            h = hs + hs * sin(y * speed) * 0.75
            fill(0)
            rect(x, y, w, h)
            next_x, next_y = x + step, y + step
            next_w = hs + hs * cos(next_x * speed ) * 0.75
            next_h = hs + hs * sin(next_y * speed) * 0.75
            fill(255, 100, 0)
            xb = (x + w / 2 + next_x - next_w / 2) / 2
            yb = (y + h / 2 + next_y - next_h / 2) / 2
            wb = step - w /2 - next_w / 2
            hb = step - h /2 - next_h / 2
            rect(xb, yb, wb, hb)
            
# WRONG
#             xb, yb = x + hs, y + hs
#             w = hs + hs * sin(x / 40 + PI) / 2
#             h = hs + hs * sin(y / 40 + PI) / 2
#             fill(255, 100, 0)
#             rect(xb, yb, w, h)
#             fill(255)
#             circle(x, y, 10)
#             circle(xb, yb, 10)