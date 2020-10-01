t = 0
def setup():
    size(500, 500)
    # noLoop()
    # noStroke()
    strokeWeight(0.1)

def draw():
    global t
    t += 0.00004
    grade(0, 0, width - 1, height - 1, 4)

def grade(xg, yg, wxg, wyg, n=None):
    n1 = n or 1 + int(6 * noise(xg * 0.1, t))
    x = xg
    sry = special_range(n1, wyg)
    n2 = n or 1 + int(6 * noise(yg * 0.1, xg * 0.1, t))
    for wx in special_range(n2, wxg):
        y = yg
        for wy in sry:
            if wy < 12 or wx < 12:
                fill((wy * 10) % 256,
                     (wx * 10) % 256,
                     (2 * wx * wy) % 256, 100)
                rect(x, y, wx, wy)
            else:
                grade(x, y, wx, wy)
            y += wy
        x += wx

def special_range(n, target, pos=None):
    """ Return a list of n float numbers that add up to target."""
    precalc = [noise(i * 0.1 + target, t)
               for i in range(n)]
    total = sum(precalc)
    if not pos:
        return [map(precalc[i], 0, total, 0, target)
            for i in range(n)]


# def keyPressed():
#     redraw()
