def setup():
    size(512, 512)
    noLoop()
    rectMode(CENTER)
    colorMode(HSB)
    noStroke()

def draw():
    clear()
    grade(256, 256, 4, 512)

def grade(xo, yo, n, tw):
    cw = tw / n
    offset = (cw - tw) / 2
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y =  yo + offset + cw * j
            if cw > 4 and random(10) < 8.5:
                grade(x, y, 2, cw)
            else:
                fill((i*64 + j*64) % 256, 200, 200)
                square(x, y, cw)

def keyPressed():
    saveFrame("####.png")
    redraw()
