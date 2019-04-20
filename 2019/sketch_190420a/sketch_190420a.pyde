# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
"""
A minimal poly editor
 - Annotate points...
"""

add_library('GifAnimation')
from gif_exporter import gif_export

cell_size = 20
outer_pts = [(20, 20), (60, 40), (100, 20), (80, 60),
             (100, 100), (60, 80), (20, 100), (40, 60)]
outer_pts = [map(lambda x: x/5, pair) for pair in outer_pts]

inner_pts = [(0, 0)] #[(5,6), (6,7), (7,6), (6,5)]
outer_drag, inner_drag = -1, -1


def setup():
    global cell_size, cell_size, order, grid_size
    global x_offset, y_offset
    size(500, 500, P2D)
    order = width / cell_size
    x_offset = y_offset = 0 #int(order / 2)
    strokeJoin(ROUND)
    f = createFont("Fira Mono Bold", 16)
    textFont(f)

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
    # fill(0)
    # text(str(outer_pts), 0, order * cell_size - 10)
    # text(str(inner_pts), 0, order * cell_size)

def poly_draw():
    #  polígono
    pushStyle()
    strokeWeight(1.5)  # espessura do polígono
    noFill()
    if len(outer_pts) >= 3:
        fill(255)
        beginShape()
        for x, y in outer_pts:
            stroke(0)
            sx = (x + x_offset) * cell_size
            sy = (y + y_offset) * cell_size
            vertex(sx, sy)
        beginContour()
        for x, y in inner_pts:
            sx = (x + x_offset) * cell_size
            sy = (y + y_offset) * cell_size
            vertex(sx, sy)
        endContour()
        endShape(CLOSE)

    annotate_pts(outer_pts, color(200, 0, 0))
    annotate_pts(inner_pts, color(0, 0, 200))
    popStyle()
    
def annotate_pts(pts, c):
    strokeWeight(5)
    textSize(16)
    fill(c)
    stroke(c)
    for i, j in pts:
        x, y = (i + x_offset) * cell_size,(j + y_offset) * cell_size
        point(x, y)
        text(str((i, j)), x, y)    

def mousePressed():
    global outer_drag, inner_drag

    if keyPressed and keyCode == SHIFT:
        for i in range(order):
            x = i * cell_size
            for j in range(order):
                y = j * cell_size
                io, jo = i - x_offset, j - y_offset # grid origin correction
                if dist(mouseX, mouseY, x, y) < 10 and mouseButton == LEFT:
                    if (io, jo) in outer_pts:
                        outer_pts.remove((io, jo))
                    else:
                        outer_pts.append((io, jo))
                if dist(mouseX, mouseY, x, y) < 10 and mouseButton == RIGHT:
                    if (io, jo) in inner_pts:
                        inner_pts.remove((io, jo))
                    else:
                        inner_pts.append((io, jo))
    else:
        for i_op, op in enumerate(outer_pts):
            ox = (op[0] + x_offset) * cell_size 
            oy = (op[1] + y_offset) * cell_size
            if dist(mouseX, mouseY, ox, oy) < cell_size / 2:
                outer_drag = i_op
                return
        for i_ip, ip in enumerate(inner_pts):
            ix = (ip[0] + x_offset) * cell_size
            iy = (ip[1] + y_offset) * cell_size
            if dist(mouseX, mouseY, ix, iy) < cell_size / 2:
                inner_drag = i_ip
                return

def mouseDragged():
    if outer_drag >= 0:
        outer_pts[outer_drag] = (int(mouseX / cell_size) - x_offset,
                                 int(mouseY / cell_size) - y_offset)
    if inner_drag >= 0:
        inner_pts[inner_drag] = (int(mouseX / cell_size) - x_offset,
                                 int(mouseY / cell_size) - y_offset)

def mouseReleased():
    global outer_drag, inner_drag
    outer_drag = -1
    inner_drag = -1

def keyPressed():
    global outer_pts, inner_pts
    if key == " ":
        
        outer_pts = clockwise_sort(outer_pts)
        inner_pts = clockwise_sort(inner_pts)[::-1]
    if key == "g":
        gif_export(GifMaker, filename=SKETCH_NAME)
    if key == "p":
        println(outer_pts)
        println(inner_pts)

def clockwise_sort(xy_pairs):
    # https://stackoverflow.com/questions/51074984/sorting-according-to-clockwise-point-coordinates
    data_len = len(xy_pairs)
    if data_len > 2:
        x, y = zip(*xy_pairs)
    else:
        return xy_pairs
    centroid_x, centroid_y = sum(x) / data_len, sum(y) / data_len
    xy_sorted = sorted(xy_pairs,
                       key = lambda p: atan2((p[1]-centroid_y), (p[0]-centroid_x)))
    xy_sorted_xy = [coord for pair in list(zip(*xy_sorted)) for coord in pair]
    half_len = int(len(xy_sorted_xy)/2)
    return list(zip(xy_sorted_xy[:half_len], xy_sorted_xy[half_len:]))


def settings():
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".png"
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/2019/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
