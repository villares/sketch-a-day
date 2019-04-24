# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
"""
A minimal poly editor
- Drag points from holes
- Remove any point with CNTRL + click
"""

from polys import Poly
Poly.cell_size = 25
Poly.text_on = False

# add_library('GifAnimation')
# from gif_exporter import gif_export

# f_pts = [map(lambda x: x / 5 - 12, pair) for pair in f_pts]
polys = [Poly([(2, 2), (2, 4), (4, 4), (4, 2)]),
         Poly([(5, 5), (5, 7), (3, 3)]),
         Poly([(-8, -7), (-1, 0), (1, -9)],
              holes=[[(-4, -4), (-6, -6), (-1, -7)], ]),
         ]

def setup():
    global x_offset, y_offset, order
    size(500, 500, P2D)
    order = width / Poly.cell_size
    x_offset = y_offset = int(order / 2)
    strokeJoin(ROUND)
    f = createFont("Fira Mono Bold", 16)
    textFont(f)

def draw():
    background(230)
    # grade
    Poly.grid(order)
    
    for p in polys:
        p.plot(x_offset, y_offset)


def mousePressed():
    for i in range(order):
        x = i * Poly.cell_size
        for j in range(order):
            y = j * Poly.cell_size
            io, jo = i - x_offset, j - y_offset  # grid origin correction
            if dist(mouseX, mouseY, x, y) < Poly.cell_size / 2:
                if keyPressed and keyCode == CONTROL:
                    for p in polys:
                        if p.remove_pt(io, jo):
                            break
                else:
                    for ip, p in enumerate(polys):
                        for ipt, pt in enumerate(p.outer_pts):
                            if pt == (io, jo):
                                Poly.drag = ip
                                Poly.drag_pt = ipt
                                break
                        for ih, h in enumerate(p.holes):
                            for ipt, pt in enumerate(h):
                                if pt == (io, jo):
                                    Poly.drag = ip
                                    Poly.drag_hole = ih
                                    Poly.drag_pt = ipt
                                    break

def mouseDragged():
    if Poly.drag >= 0:  # a Poly point has been selected to be dragged
        if Poly.drag_hole == -1:  # if no hole wase selected
            polys[Poly.drag].outer_pts[Poly.drag_pt] = (
                int(mouseX / Poly.cell_size) - x_offset,
                int(mouseY / Poly.cell_size) - y_offset)
        else:
            polys[Poly.drag].holes[Poly.drag_hole][Poly.drag_pt] = (
                int(mouseX / Poly.cell_size) - x_offset,
                int(mouseY / Poly.cell_size) - y_offset)

def mouseReleased():
    Poly.drag = -1  # No poly selected
    Poly.drag_hole = -1  # No hole selected
    Poly.drag_pt = -1  # No point selected

def keyPressed():
    if key == " ":
        for p in polys:
            p.outer_pts[:] = clockwise_sort(p.outer_pts)
            for h in p.holes:
                h[:] = clockwise_sort(h)[::-1]
    # if key == "g":
    #     gif_export(GifMaker, filename=SKETCH_NAME)
    if key == "s":
        saveFrame(SKETCH_NAME+"#.png")
    if key == "t":
        Poly.text_on = not Poly.text_on

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
