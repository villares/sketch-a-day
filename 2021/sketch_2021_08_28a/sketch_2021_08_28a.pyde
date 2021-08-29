from random import randint

m = 20
light_rects = 20
dark_rects = 10

def setup():
    size(1000, 500)
    noLoop()
    
def draw():    
    background(0, 20, 30)
    noStroke()
    fill(240, 255, 240, 100)
    for _ in range(light_rects):
        w = randint(height // (m * 2), height // m) * m
        x = (randint(m, width - w - m) // m) * m
        h = randint(w // (4 * m), w // (2 * m)) * m
        y = (randint(m, height - h - m) // m) * m
        rect(x, y, w, h)
    fill(0, 30, 20, 240)
    for _ in range(dark_rects):
        x = (randint(m, width - m * 2) // m) * m
        y = (randint(m, height - m * 2) // m) * m
        square(x, y, m)
        
def keyPressed():
    redraw()
    
