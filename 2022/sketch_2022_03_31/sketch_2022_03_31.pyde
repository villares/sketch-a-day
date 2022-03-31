def setup():
    size(600, 600, P3D)

def draw():
    background(10)
    # ortho()
    lights()
    translate(width / 2, height / 2, -height / 2)
    rotateX(QUARTER_PI)
    rotateZ(QUARTER_PI)
    translate(-width / 2, 0, 0)# -height / 2, 0)   

    # elements = ((x, w, a, b), )
    elements = (
        (400, 50, 150, 150),
        (300, 80, 200, 100),
        (50, 200, 50, 300),
        )
        
    rect_base(0, 0, 600, 400, *[(x, 0, w, b) for x, w, a, b in elements])
    for x, w, a, b in elements:
        rect_h(x, 0, w, b, z=a)
    rotateX(HALF_PI)
    rect_base(0, 0, 600, 400, *[(x, 0, w, a) for x, w, a, b in elements])
    for x, w, a, b in elements:
        rect_h(x, 0, w, a, z=-b)
    
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
        
