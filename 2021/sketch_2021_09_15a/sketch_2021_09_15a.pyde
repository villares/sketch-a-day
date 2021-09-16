def setup():
    size(500, 500)
    background(128)
    stroke(0, 0, 100)
    region(100, 000, 400, 400)
    stroke(0, 100, 0)
    region(0, 100, 400, 400)


def region(xo, yo, w, h):
    for x in range(xo, xo + w):
        for y in range(yo, yo + h):
            if ((random(w) > x - xo) ^
                (random(w) < y - yo)):
                point(x, y)
                
