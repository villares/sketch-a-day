
from py5_tools import animated_gif


def setup():
    size(500, 500)
    no_stroke()
    frame_rate(16)
    animated_gif('out.gif', 32, 0.06, 0.06)
    
def draw():
    background(100)
    x, y, w, h = 200, 100, 200, 300
    fill(0 if random(50) > 1 else 255)
    rect(x, y, w, h)
    fill(128)
    for i in range(x, x + w):
        rect(i, random(y, y + h), 1, random(2, 5))

    fill(255)
    for i in range(x, x + w):
        rect(i, random(y, y + h), random(1, 2), random(5, 20))
        
    fill(100)
    rect(x, y + h, w, 20)