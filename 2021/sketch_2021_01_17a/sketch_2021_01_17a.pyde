from random import choice, sample

walkers = (
           lambda: PVector.random2D() * 5 * sqrt(2),  
           lambda: (choice((-5, 5)), choice((-5, 5)), 0),
           lambda: (choice((-5, 0, 5)), choice((-5, 0, 5)), 0),
           lambda: sample((-5, 0, 0, 5), 2) + [0],
           lambda: sample((-5, -5, 0, 0, 5, 5), 2) + [0] 
           )

def setup():
    global x, y, mover
    size(500, 500)
    x, y = width / 2, height / 2
    mover = choice(walkers)
    noStroke()
    background(240)
    strokeWeight(2)

def draw():
    global x, y, mover
    
    mx, my, _ = mover()
    stroke(mx  * mx * 5,  my * my * 5, (mx * mx + my * my) * 5, 100)
    line(x, y, x + mx, y + my)
    x += mx
    y += my

    if not 0 < x < width or not 0 < y < height:
        x, y = random(width), random(height)

    if frameCount % 200 == 0:
        mover = choice(walkers)
