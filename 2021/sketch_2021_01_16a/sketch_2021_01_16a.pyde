from random import choice, sample

walkers = (lambda: (random(-5, 5), random(-5, 5), 0),
           # lambda: PVector.random2D() * 5,
            lambda: PVector.random2D() * 5 * sqrt(2),  
           lambda: PVector.random2D() * random(-5, 5),
           lambda: (choice((-5, 5)), choice((-5, 5)), 0),
           lambda: (choice((-5, 0, 5)), choice((-5, 0, 5)), 0),
           # lambda: sample((-5, -5, 0, 5, 5), 2) + [0]
           lambda: sample((-5, -5, 0, 0, 5, 5), 2) + [0] 
           )

def setup():
    global x, y, mover
    size(500, 500)
    x, y = width / 2, height / 2
    mover = choice(walkers)
    noStroke()
    background(240)

def draw():
    global x, y, mover
    
    mx, my, _ = mover()
    x += mx
    y += my
    fill(mx * 59,  my * 50, sqrt(mx * mx + my * my) * 50, 100)
    circle(x, y, 5)

    if not 0 < x < width or not 0 < y < height:
        x, y = width / 2, height / 2

    if frameCount % 200 == 0:
        mover = choice(walkers)
