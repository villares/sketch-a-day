
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
                squarish(nx, ny, cw-2)
    
def squarish(x, y, w):
      xa, ya = x - w / 2, y - w / 2
      xb, yb = x + w / 2, y - w / 2
      xc, yc = x + w / 2, y + w / 2
      xd, yd = x - w / 2, y + w / 2
      coords = (xa, ya, xb, yb, xc, yc, xd, yd)
      rnd_coords = (c + int(random(-10, 10) * (y / height)) for c in coords)
      quad(*rnd_coords)
