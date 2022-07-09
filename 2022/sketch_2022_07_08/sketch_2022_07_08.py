# Inspired by Antonio Maluf

def setup():
    size(800, 1000)
    
def draw():
    background(200)
    rect_mode(CENTER)
    no_stroke()
    step = 40
    hs = int(step / 2)
    speed = 1 / 100
    xoff = 100
    t = frame_count
    for y in range(hs, height, step): 
        for x in range(hs, width, step):
            w = hs + hs * os_noise(x * speed + xoff, t * speed) * 0.75
            h = hs + hs * os_noise(y * speed, t * speed) * 0.75
            fill(0)
            rect(x, y, w, h)
            next_x, next_y = x + step, y + step
            next_w = hs+ hs * os_noise(next_x * speed + xoff, t * speed) * 0.75
            next_h = hs + hs * os_noise(next_y * speed, t * speed) * 0.75
            fill(255, 100, 0)
            xb = (x + w / 2 + next_x - next_w / 2) / 2
            yb = (y + h / 2 + next_y - next_h / 2) / 2
            wb = step - w /2 - next_w / 2
            hb = step - h /2 - next_h / 2
            rect(xb, yb, wb, hb)
 
