def setup():
    size(1024, 1024)
    noLoop()
    noStroke()

def draw():
    saveFrame("a###.png")
    background(0)
    grade(0, 0, width - 1, height - 1, 8)

def grade(xg, yg, wxg, wyg, n=8):
    x = xg
    for wx in special_range(n, wxg):
        y = yg
        for wy in special_range(n, wyg):
            if n == 1:
                fill(wy % 256, wx % 256, (wx * wy) % 256)
                rect(x, y, wx, wy)
            else:
                if wx < 24 and wy < 24:
                    fill(wy * 16 % 256, wx * 16 % 256, 255)
                    # print(wy * 16 % 256, wx * 16 % 256)
                    rect(x, y, wx - 1, wy - 1)
                else:
                    grade(x, y, wx, wy)
            y += wy
        x += wx

def special_range(n, wg):
    precalc = [int(random(1, 5)) for _ in range(n)]
    pretotal = sum(precalc) 
    for i in range(n):
        yield map(precalc[i], 0, pretotal, 0, wg)
            
def keyPressed():
    redraw()
    
    
    
