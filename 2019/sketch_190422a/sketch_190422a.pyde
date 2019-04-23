# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
"""
A minimal poly editor
 - Multiple polys...
"""

from polys import Poly

# add_library('GifAnimation')
# from gif_exporter import gif_export
cell_size = 10

# f_pts = [map(lambda x: x / 5 - 12, pair) for pair in f_pts]
polys = [Poly([(2, 2), (2, 4), (4, 4), (4, 2)]),
         Poly([(5, 5), (5, 10), (7, 7)])
         ]

text_on = False

def setup():
    global cell_size, cell_size, order, grid_size
    global x_offset, y_offset
    size(500, 500, P2D)
    order = width / cell_size
    x_offset = y_offset = int(order / 2)
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
        
    for p in polys:
        p.plot(x_offset, y_offset, cell_size)


def mousePressed():
         for i in range(order):
             x = i * cell_size
             for j in range(order):
                y = j * cell_size
                io, jo = i - x_offset, j - y_offset  # grid origin correction
                if keyPressed and keyCode == SHIFT:
                         if dist(mouseX, mouseY, x, y) < 10 and mouseButton == LEFT:
                             pass
#     else:
#         for i, outer_pts in enumerate(outer_polys):
#             for i_op, op in enumerate(outer_pts):
#                 ox = (op[0] + x_offset) * cell_size
#                 oy = (op[1] + y_offset) * cell_size
#                 if dist(mouseX, mouseY, ox, oy) < cell_size / 2:
#                     outer_drag = i_op
#                     return



def mouseDragged():
    if Poly.drag >= 0:
        if Poly.drag_hole == -1:
           polys[Poly.drag].outer_pts[Poly.drag_pt] = (int(mouseX / cell_size) - x_offset,
                                                       int(mouseY / cell_size) - y_offset)
        else:
            polys[Poly.drag].holes[Poly.drag_hole][Poly.drag_pt] = (int(mouseX / cell_size) - x_offset,
                                                                    int(mouseY / cell_size) - y_offset)

def mouseReleased():
    Poly.drag = -1
    Poly.drag_hole = -1
    Poly.drag_drag_pt = -1

def keyPressed():
    global outer_pts, inner_pts, text_on
    if key == " ":
        for p in polys:
            p.outer_pts[:] = clockwise_sort( p.outer_pts)
            for h in p.holes:
               h[:] = clockwise_sort(h)
    # if key == "g":
    #     gif_export(GifMaker, filename=SKETCH_NAME)
    if key == "p":
        println(outer_pts)
        println(inner_pts)
    if key == "s":
        saveFrame("####.png")
    if key == "t":
        text_on = not text_on

def clockwise_sort(xy_pairs):
    # https://stackoverflow.com/questions/51074984/sorting-according-to-clockwise-point-coordinates
    data_len = len(xy_pairs)
    if data_len > 2:
        x, y = zip(*xy_pairs)
    else:
        return xy_pairs
    centroid_x, centroid_y = sum(x) / data_len, sum(y) / data_len
    xy_sorted = sorted(xy_pairs,
                       key=lambda p: atan2((p[1] - centroid_y), (p[0] - centroid_x)))
    xy_sorted_xy = [coord for pair in list(zip(*xy_sorted)) for coord in pair]
    half_len = int(len(xy_sorted_xy) / 2)
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
