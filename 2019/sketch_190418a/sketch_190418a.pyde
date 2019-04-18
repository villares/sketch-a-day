"""
A minimal poly editor
"""
cell_size = 25
outer_pts = [(12.0, 10.0), (12.0, 0.0), (-2.0, -2.0),
             (0.0, 12.0), (10.0, 12.0), (10.0, 10.0)]
inner_pts = [(2.0, 2.0), (6.0, 2.0), (6.0, 6.0), (2.0, 7.0)]
outer_drag = -1
inner_drag = -1

def setup():
    global cell_size, cell_size, order, grid_size
    size(500, 500, P2D)
    order = width / cell_size
    # grid_size = order * cell_size
    strokeJoin(ROUND)

def draw():
    background(230)
    # grade de cellulas
    stroke(128)
    noFill()
    for x in range(order):
        for y in range(order):
            rect(x * cell_size, y * cell_size,
                 cell_size, cell_size)

    poly_draw()
    fill(0)
    text(str(outer_pts), 0, order * cell_size)


def poly_draw():
    #  polígono
    pushStyle()
    strokeWeight(3)  # espessura do polígono
    noFill()
    if len(outer_pts) >= 3:
        fill(255)
        beginShape()
        for x, y in outer_pts[::-1]:
            stroke(0)
            sx = x * cell_size
            sy = y * cell_size
            vertex(sx, sy)
        beginContour()
        for x, y in inner_pts[::-1]:
            sx = x * cell_size
            sy = y * cell_size
            vertex(sx, sy)
        endContour()
        endShape(CLOSE)

    elif len(outer_pts) == 2:
        stroke(128)
        beginShape(LINES)
        for x, y in outer_pts:
            vertex(x * cell_size, y * cell_size)
        endShape()
        for x, y in inner_pts:
            fill(0)
            ellipse(x * cell_size, y * cell_size, 5, 5)

    else:
        for x, y in outer_pts:
            fill(255)
            ellipse(x * cell_size, y * cell_size, 5, 5)
        for x, y in inner_pts:
            fill(0)
            ellipse(x * cell_size, y * cell_size, 5, 5)

    popStyle()

def keyPressed():
    global outer_pts
    if key == " ":
        outer_pts = []  # empty outer_pts
    if key == "p":
        println(outer_pts)

def mousePressed():
    global outer_drag, inner_drag

    if keyPressed and keyCode == SHIFT:
        for i in range(order):
            x = i * cell_size
            for j in range(order):
                y = j * cell_size
                if dist(mouseX, mouseY, x, y) < 10 and mouseButton == LEFT:
                    if (i, j) in outer_pts:
                        outer_pts.remove((i, j))
                    else:
                        outer_pts.append((i, j))
                if dist(mouseX, mouseY, x, y) < 10 and mouseButton == RIGHT:
                    if (i, j) in inner_pts:
                        inner_pts.remove((i, j))
                    else:
                        inner_pts.append((i, j))
    else:
        for i_op, op in enumerate(outer_pts):
            ox = op[0] * cell_size
            oy = op[1] * cell_size
            if dist(mouseX, mouseY, ox, oy) < cell_size / 2:
                outer_drag = i_op
                return
        for i_ip, ip in enumerate(inner_pts):
            ix = ip[0] * cell_size
            iy = ip[1] * cell_size
            if dist(mouseX, mouseY, ix, iy) < cell_size / 2:
                inner_drag = i_ip
                return

def mouseDragged():
    if outer_drag >= 0:
        outer_pts[outer_drag] = (int(mouseX / cell_size),
                                 int(mouseY / cell_size))
    if inner_drag >= 0:
        inner_pts[inner_drag] = (int(mouseX / cell_size),
                                 int(mouseY / cell_size))

def mouseReleased():
    global outer_drag, inner_drag
    outer_drag = -1
    inner_drag = -1


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
