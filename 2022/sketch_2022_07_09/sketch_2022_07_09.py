# Inspired by Antonio Maluf

size(900, 900)
background(200)
no_stroke()

margin = 0
step = 30
hs = int(step / 2)
speed = 1 / (PI * 45)
xoff = PI

t = frame_count
for y in range(margin, height, step): 
    for x in range(margin, width, step):
        w = hs + hs * sin(x * speed + xoff) * 0.75
        h = hs + hs * sin(y * speed) * 0.75
        c = remap(x, 0, width, 1, 0)
        fill(0)
        rect(x, y, w, h * c)
        fill(0, 0, 200)            
        rect(x, y + h * c, w, h * (1 - c))
        next_x, next_y = x + step, y + step
        next_w = hs+ hs * sin(next_x * speed + xoff) * 0.75
        next_h = hs + hs * sin(next_y * speed) * 0.75
        wb = step - w / 2 - next_w / 2
        hb = step - h / 2 - next_h / 2
        xb = (x + w + next_x - wb) / 2
        yb = (y + h + next_y - hb) / 2
        c = remap(y, 0, height, 1, 0)
        wc = wb * c
        fill(200, 0, 0)
        rect(xb, yb, wb * c, hb)
        fill(255, 100, 0)
        rect(xb + wb * c, yb, wb * (1 - c), hb)

from villares.helpers import save_png_with_src
save_png_with_src() 
