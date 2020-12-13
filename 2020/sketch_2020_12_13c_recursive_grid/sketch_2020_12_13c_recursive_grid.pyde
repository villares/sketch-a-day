from villares import ubuntu_jogl_fix

    
def setup():
    size(640, 640, P3D) 
    rectMode(CENTER)
    fill(0)
    colorMode(HSB)
    smooth(8)
    # strokeWeight(2)
    noLoop()
    
def draw():
    background(0)
    ortho()
    translate(width / 2, height / 2, 0)
    rotateX(QUARTER_PI)
    rotateZ(QUARTER_PI)
    rec_grid(0, 0, 16, width * 2)

    # rec_grid(width / 2, height / 2, 8, width)
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
                sbox(nx, ny, cw-2)
    popMatrix()
    
    
def sbox(x, y, s):
    pushMatrix()
    translate(x , y)
    box(s)
    popMatrix()
