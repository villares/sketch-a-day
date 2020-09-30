t = 0
def setup():
    size(400, 400)
    # noLoop()

def draw():
    randomSeed(2)

    global t
    t += 0.00001
    grade(0, 0, width - 1, height - 1, 5)

def grade(xg, yg, wxg, wyg, n=None):
    # randomSeed(int(xg + yg * 1000))
    n = n or int(random(1, 7))
    x = xg
    sry = special_range(n, wyg)
    for wx in special_range(n, wxg):
        y = yg
        for wy in sry:
            if n == 1:
                fill(wy % 256, wx % 256, (wx + wy) % 256)
                rect(x, y, wx, wy)
            else:
                if wy < 20 or wx < 20:
                    fill(wy % 256, wx % 256, (wx * wy) % 256)
                    rect(x, y, wx, wy)
                else:
                    grade(x, y, wx, wy)
            y += wy
        x += wx

def special_range(n, wg):
    precalc = [noise(i * 1 + wg, t) for i in range(n)]
    pretotal = sum(precalc)
    return [map(precalc[i], 0, pretotal, 0, wg)
            for i in range(n)]

# def keyPressed():
#     redraw()
