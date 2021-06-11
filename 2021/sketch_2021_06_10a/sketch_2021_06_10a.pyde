def setup():
    size(800, 800)
    noLoop()
    strokeWeight(0.1)
    stroke(0)

def draw():
    background(0)
    grade(0, 0, width - 1, height - 1, 4)

def grade(xg, yg, wxg, wyg, n=None):
    n = n or int(random(2, 5))
    x = xg
    for wx in special_range(n, wxg):
        y = yg
        for wy in special_range(n, wyg):
            if n == 1:
                fill(wy % 256, wx % 256, (wx * wy) % 256)
                rect(x, y, wx, wy)
            else:
                if wy < 100 and wx < 20:
                    fill(wy % 256, wx % 256, (wx * wy) % 256)
                    rect(x, y, wx, wy)
                else:
                    grade(x, y, wx, wy)
            y += wy
        x += wx

def special_range(n, wg):
    precalc = [int(random(1, 11)) for _ in range(n)]
    pretotal = sum(precalc) 
    for i in range(n):
        yield map(precalc[i], 0, pretotal, 0, wg)
            
def keyPressed():
    redraw()
    
    
    
