"""
A minimal poly editor
"""
ORDER = 10
click = False
cell_size = 45.
pts = [(12.0, 10.0), (12.0, 0.0), (-2.0, -2.0),
       (0.0, 12.0), (10.0, 12.0), (10.0,  10.0)]
holes = [(2.0, 2.0), (6.0, 2.0), (6.0, 6.0), (2.0, 7.0)]
md = -1


def setup():
    global xo, yo  # offset de correção da borda na tela cheia
    global cell_size, cell_half, grid_size
    size(500, 500, P2D)
    grid_size = ORDER * cell_size
    cell_half = cell_size / 2
    xo, yo = (width - grid_size) / 2, (height - grid_size) / 2
    rectMode(CENTER)
    strokeJoin(ROUND)

def draw():
    background(230)
    translate(xo, yo)
    stroke(128)
    for x in range(ORDER):
        line(cell_half + x * cell_size, cell_half,
             cell_half + x * cell_size, cell_size * ORDER - cell_half)
    for y in range(ORDER):
        line(cell_half, cell_half + y * cell_size,
             cell_size * ORDER - cell_half, cell_half + y * cell_size)
    # grade de cellulas
    for i in range(ORDER):
        x = cell_half + i * cell_size
        for j in range(ORDER):
            y = cell_half + j * cell_size
            cell(x, y)
    poly_draw()
    fill(0)
    text(str(pts), 0, grid_size)

def cell(mx, my):
    global click
    noStroke()
    if dist(mouseX - xo, mouseY - yo, mx, my) < cell_half:
        fill(209, 100)
        if click:
            x = mx / cell_size * 2 - ORDER / 2
            y = my / cell_size * 2 - ORDER / 2
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
            sx = (x + ORDER / 2) * cell_half
            sy = (y + ORDER / 2) * cell_half
            vertex(sx, sy)            
        beginContour()
        for x, y in holes[::-1]:
            sx = (x + ORDER / 2) * cell_half
            sy = (y + ORDER / 2) * cell_half
            vertex(sx, sy)  
        endContour()  
        endShape(CLOSE)

    elif len(pts) == 2:
        stroke(128)
        beginShape(LINES)
        for x, y in pts:
            sx = (x + ORDER / 2) * cell_half
            sy = (y + ORDER / 2) * cell_half
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
        x = (p[0] + ORDER / 2) * cell_half
        y = (p[1] + ORDER / 2) * cell_half
        if dist(mouseX - xo, mouseY - yo, x, y) < 10:
            md = i
            break
    global click
    if mouseButton == RIGHT:
        click = True
        
def mouseDragged():
    if md >= 0:
        mx = mouseX - xo
        my = mouseY - yo
        pts[md] = (int(mx / cell_size * 2 - ORDER / 2), 
                   int(my / cell_size * 2 - ORDER / 2))

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

[{0}](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
