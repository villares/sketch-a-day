def setup():
    size(600, 600)
    noLoop()
    rectMode(CENTER)
    colorMode(HSB)
    noStroke()

def draw():
    clear()
    grade(300, 300, 3, 600.)

def grade(xo, yo, n, tw):
    cw = tw / n
    offset = (cw - tw) / 2.
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y =  yo + offset + cw * j
            if cw > 21 and random(10) < 5:
                grade(x, y, 3, cw)
            else:
                fill(i*16 + j*64, 200, 200)
                # fill(127 + i*32 - j*64)
                # t = "i{} j{} t{}".format(i, j, (127 + i*32 - j*64))
                square(x, y, cw)
                # fill(0, 200, 200)
                # text(t, x, y)

def keyPressed():
    saveFrame("####.png")
    redraw()
