from random import choice

step = 1

def setup():
    size(500, 500)
    frameRate(5)
        
def draw():
    background(255)
    # fill(200, 10)
    # rect(-1, -1, 501, 501)
    translate(width / 2, height / 2)
    for i in range(100):
        rotate(HALF_PI * choice((-1, 1)))  
        line(0, 0, step * i, 0)
        translate(step * i, 0)
