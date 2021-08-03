from random import choice

w = 800

moves = (
    lambda i: (i, 0),
    lambda i: (0, i),
    lambda i: (-i, 0),
    lambda i: (0, -i),
   )

def setup():
    size(w, w)
    colorrange(255)
    colormode(HSB)
    speed(1)
    
def draw():
    for j in range(16, 0, -1):
        strokewidth(j / 3 + 1)
        c = color(j * 16, 128, 128)
        stroke(c)
        push()
        transform(CORNER)
        nofill()
        xo, yo = w / 2, w / 2
        autoclosepath(False)
        beginpath(xo, yo)
        direction = 1
        for i in range(100):
            direction = (direction + choice((-1, 1))) % 4
            x, y = moves[direction](i * 5)
            xo += x
            yo += y
            lineto(xo, yo)
        endpath()
        pop()