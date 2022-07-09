"""
sketch_2022_07_07 - d'aprés Antonio Maluf 1926—2005
Alexandre B A Villares - abav.lugaragum.com/sketch-a-day
"""

size(800, 1000)
rect_mode(CENTER)
no_stroke()
step = 40
hs = int(step / 2)
speed = 1 / 150
for y in range(hs, height, step): 
    for x in range(hs, width, step):
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
 
