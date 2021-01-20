def setup():
    size(512 +128, 512 + 128) #, PDF, "a.pdf")
    rectMode(CENTER)
    noFill()
    stroke(0, 0, 255)
    noSmooth()
    noLoop()
    
def draw():
    background(0)
    rec_grid(width / 2, height / 2, 8, width)
    saveFrame("###.png")
    
def keyPressed():
    redraw()
    
def rec_grid(x, y, n, tw):
    cw = float(tw) / n
    margin = (cw - tw) / 2.0
    for i in range(n):
        nx = x + cw * i + margin
        for j in range(n):
            ny = y + cw * j + margin
            if cw > 8 and random(10) < 9:
                rec_grid(nx, ny, 2, cw)
            else:
                pushMatrix()
                rx = int(random(-15, 15) * (ny / height))
                ry = int(random(-15, 15) * (ny / height))
                translate(nx + rx, ny + ry)
                d = int(random(-30, 30) * (ny / height))
                rotate(radians(d))
                square(0, 0, cw - 2)
                popMatrix()
            
      
