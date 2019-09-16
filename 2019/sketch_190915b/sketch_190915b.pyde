
def setup():
    size(512, 512)
    noLoop()
    rectMode(CENTER)
    colorMode(HSB)

def draw():clear();r(256, 256, 2, 512)
    
def r(x, y, n, tw):
    ox, oy = 0, 0
    cw = tw / n
    m = (cw - tw) / 2
    for i in range(n):
        nx = cw * i + m
        for j in range(n):
            ny = cw * j + m
            if cw > 8 and random(10) < 8.5:
                r(nx-x, ny-y, 2, cw)
            else:
                fill(55 + dist(ox, oy, nx, ny) % 200, 200, 200)
                square(nx-x, ny-y, cw)                
                ox += x
                oy += y  

def keyPressed():
    saveFrame("####.png")
    redraw()

    
    
    
