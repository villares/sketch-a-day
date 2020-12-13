
def setup():
    size(512 +128, 512 + 128) #, PDF, "a.pdf")
    rectMode(CENTER)
    fill(0)
    colorMode(HSB)
    noSmooth()
    noLoop()
    
def draw():
    background(0)
    rec_grid(width / 2, height / 2, 8, width)
    saveFrame("###.png")
    
def keyPressed():
    redraw()
    
def rec_grid(x, y, n, tw):
    pushMatrix()
    translate(x, y)
    cw = float(tw) / n
    margin = (cw - tw) / 2.0
    for i in range(n):
        nx = cw * i + margin
        for j in range(n):
            ny = cw * j + margin
            if cw > 8 and random(10) < 5:
                rec_grid(nx, ny, 2, cw)
            else:
                stroke(8 + 2 * cw, 255, 255)
                square(nx, ny, cw-2)
    popMatrix()
