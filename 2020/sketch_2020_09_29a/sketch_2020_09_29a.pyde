def setup():
    size(400, 400)
    noLoop()

def draw():
    grade(0, 0, width - 1, height - 1, 4)

def grade(xg, yg, wxg, wyg, n=None):
    n = n or int(random(1, 5))
    x = xg
    for wx in special_range(n, wxg):
        y = yg
        for wy in special_range(n, wyg):
            print(wx, wy)
            if n == 1:
                fill(wy % 256, wx % 256, (wx * wy) % 256)
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
    precalc = [random(10) for _ in range(n)]
    pretotal = sum(precalc)
    return [map(precalc[i], 0, pretotal, 0, wg)
            for i in range(n)]

def keyPressed():
    redraw()
