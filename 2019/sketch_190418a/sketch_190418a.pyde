"""
A minimal poly editor
"""
click = False
cell_size = 25
pts = [(12.0, 10.0), (12.0, 0.0), (-2.0, -2.0),
       (0.0, 12.0), (10.0, 12.0), (10.0,  10.0)]
holes = [(2.0, 2.0), (6.0, 2.0), (6.0, 6.0), (2.0, 7.0)]
md = -1


def setup():
    global cell_size, cell_half, order, grid_size
    size(500, 500, P2D)
    order = width / cell_size
    grid_size = order * cell_size
    cell_half = cell_size / 2
    rectMode(CENTER)
    strokeJoin(ROUND)

def draw():
    background(230)
    stroke(128)
    for x in range(order):
        line(x * cell_size, 0,
             x * cell_size, cell_size * order)
    for y in range(order):
        line(0, y * cell_size,
             cell_size * order , y * cell_size)
    # grade de cellulas
    for i in range(order):
        x = cell_half + i * cell_size
        for j in range(order):
            y = cell_half + j * cell_size
            cell(x, y)
    poly_draw()
    fill(0)
    text(str(pts), 0, grid_size)

def cell(mx, my):
    global click
    noStroke()
    if dist(mouseX, mouseY, mx, my) < cell_half:
        fill(209, 100)
        if click:
            x = mx / cell_size * 2
            y = my / cell_size * 2 
            if (x, y) in pts:
                pts.remove((x, y))
            else:
                pts.append((x, y))
            click = False
    else:
        noFill()
    ellipse(mx, my, cell_size, cell_size)

def poly_draw():
    #  polígono
    pushStyle()
    strokeWeight(3)  # espessura do polígono
    noFill()
    if len(pts) >= 3:
        fill(255)
        beginShape()
        for x, y in pts[::-1]:
            stroke(0)
            sx = x * cell_half
            sy = y * cell_half
            vertex(sx, sy)            
        beginContour()
        for x, y in holes[::-1]:
            sx = x * cell_half
            sy = y * cell_half
            vertex(sx, sy)  
        endContour()  
        endShape(CLOSE)

    elif len(pts) == 2:
        stroke(128)
        beginShape(LINES)
        for x, y in pts:
            sx = x * cell_half
            sy = y * cell_half
            vertex(sx, sy)
        endShape()
    popStyle()

def keyPressed():
    global pts
    if key == " ":
        pts = []  # empty pts
    if key == "p":
        println(pts)
        
def mousePressed():
    global md
    for i, p in enumerate(pts):
        x = p[0] * cell_half
        y = p[1] * cell_half
        if dist(mouseX, mouseY, x, y) < 10:
            md = i
            break
    global click
    if mouseButton == RIGHT:
        click = True
        
def mouseDragged():
    if md >= 0:
        pts[md] = (int(mouseX / cell_size * 2), 
                   int(mouseY / cell_size * 2))

def mouseReleased():
    global md
    md = -1        
        
def settings():
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".gif"
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/2019/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
