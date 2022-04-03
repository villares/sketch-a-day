s = 0.005  # noise scale

def setup():
    size(1200, 600, P3D)
    noLoop()

def draw():
    background(10)
    # ortho()
    lights()
    push()
    translate(width / 4, height / 2, -height / 2)
    rotateX(QUARTER_PI)
    rotateZ(QUARTER_PI / 2)
    translate(-width / 4, 0, 0)# -height / 2, 0)   
    
    elements = [] # ((x, w, a, b), )
    margin = 50
    x = margin
    while x < 580 - margin:
        w = max(20, min(random(20, 60), 600 - margin - x))
        a = 300 * noise(1000 + x * s)
        b = 300 * noise(x * s)
        elements.append((x, w, a, b))
        x += w
        
    rect_base(0, 0, 600, 400, *[(x, 0, w, b) for x, w, a, b in elements])
    for x, w, a, b in elements:
        rect_h(x, 0, w, b, z=a)
    rotateX(HALF_PI)
    rect_base(0, 0, 600, 400, *[(x, 0, w, a) for x, w, a, b in elements])
    for x, w, a, b in elements:
        rect_h(x, 0, w, a, z=-b)
    
    pop()
    fill(255)
    translate(600, 0)
    rect(0, 0, 600, 600)
    line(0, 300, 600, 300)
    translate(0, 0, 3)
    for x, w, a, b in elements:
        y = 300
        rect(x, y - a, w, b)
        rect(x, y - a + b, w, a)
        
def rect_h(x, y, w, h, z):
    with pushMatrix():
        translate(0, 0, z)
        rect(x, y, w, h)
    
def rect_base(x, y, w, h, *furos):
    if furos:
        beginShape()
        vertex(x, y)
        vertex(x + w, y)        
        vertex(x + w, y + h)
        vertex(x, y + h)
        for furo in furos:
            rect_base(*furo)
        endShape(CLOSE)
    else:
        beginContour()
        vertex(x, y)
        vertex(x, y + h)
        vertex(x + w, y + h)
        vertex(x + w, y)
        endContour()
        
def keyPressed():
    noiseSeed(int(random(10000)))
    redraw()
