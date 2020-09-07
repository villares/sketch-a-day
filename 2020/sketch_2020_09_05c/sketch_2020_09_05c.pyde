import random

sf = 1
colunas = 4
seed_value = 100

gliphs = (lambda x, y, s: square(x, y, s),
          lambda x, y, s: circle(x, y, s),
          lambda x, y, s: triangle(x - s, y, x - s, y + s, x, y + s),
          lambda x, y, s: triangle(x + s, y, x + s, y - s, x, y - s),
         )

colors = (color(200, 0, 0, 230),
          color(200, 0, 200, 230),
          color(0)
          )

def ensamble(ex, ey, eo):
    # print(f"seed inside ensamble: {seed_value}")
    # random.seed(seed_value + int(ex * (ey + 100)))   # kind of works
    noStroke()
    for i in range(eo):
        fill(colors[i % len(colors) - 1])
        order, spacing, side = random.randint(6, 12), 14, 7
        x = (1 + random.randint(-5, 4)) * side * sf
        y = (1 + random.randint(-5, 4)) * side * sf
        grid(ex+x,
             ey+y,
             order,
             spacing * sf,
             random.choice(gliphs),
             side * sf)

def grid(x, y, order, spacing, function, *args):  
    if type(order) is tuple:
        cols, rows = order
    else:
        cols = rows = order
    xo, yo = (x - cols * spacing / 2 , y - rows * spacing / 2)
    for i in range(cols):
        gx = spacing / 2 + i * spacing
        for j in range(rows):
            gy = spacing/2 + j * spacing
            function(xo + gx, yo + gy, *args)


def setup():
    size(700, 700)
    noLoop()

def draw():    
    background(245, 245, 240)
    random.seed(seed_value)   # doesn't work! I wish it would work here!
    grid(width / 2, height / 2, (2, 2), 300 * sf, ensamble, 5)
    
def keyPressed():
    global seed_value
    seed_value = random.randint(1,  100000000000000)
    redraw()
