from random import choice, sample

walkers = (lambda: (random(-5, 5), random(-5, 5), 0),
           lambda: PVector.random2D() * 5,
            # lambda: PVector.random2D() * 5 * sqrt(2),  # not in original capture
           lambda: PVector.random2D() * random(-5, 5),
           lambda: (choice((-5, 5)), choice((-5, 5)), 0),
           lambda: (choice((-5, 0, 5)), choice((-5, 0, 5)), 0),
           lambda: sample((-5, -5, 0, 5, 5), 2) + [0]
           # lambda: sample((-5, -5, 0, 0, 5, 5), 2) + [0] # not in original capture
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
    fill(0, 100)
    circle(x, y, 5)
    mx, my, _ = mover()
    x += mx
    y += my

    if not 0 < x < width or not 0 < y < height:
        x, y = width / 2, height / 2

    if frameCount % 200 == 0:
        mover = choice(walkers)
        fill(240)
        circle(random(width), random(height), random(height))
