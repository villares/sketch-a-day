# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
"""
A minimal poly editor
- Add points
"""
import pickle
from copy import deepcopy
from poly import Poly
# add_library('GifAnimation')
# from gif_exporter import gif_export

# f_pts = [map(lambda x: x / 5 - 12, pair) for pair in f_pts]
polys = [Poly([(-8, -7), (-1, 0), (1, -9)],
              holes=[[(-4, -4), (-6, -6), (-1, -7)], ]
              ),
         Poly([(0, 0), (1, 1), (1, 0)], lw=5, closed=False)
         ]

def setup():
    size(500, 500, P2D)
    CELL_SIZE = 15
    order = width // CELL_SIZE
    x_offset = y_offset = int(order // 2)
    Poly.setup_grid(CELL_SIZE, order, x_offset, y_offset)
    Poly.text_on = False
    Poly.polys = polys
    f = createFont("Fira Mono", 16)
    textFont(f)

def draw():
    background(230)
    # grade
    Poly.draw_grid()
    # polígonos
    for p in polys:
        p.plot()

def mousePressed():
    if keyPressed and keyCode == CONTROL:
        for p in polys:
            if p.remove_pt():  # io, jo):
                return
    else:
        for ip, p in enumerate(polys):
            if p.set_drag():  # io, jo):
                Poly.selected_drag = ip
                return
    Poly.selected_drag = -1 # click outside known vertices deselects 

def mouseDragged():
    if Poly.selected_drag >= 0 and not keyPressed:
        # a Poly point has been selected to be dragged
        # and no modifier key is pressed...
        if Poly.drag_hole == -1:  # if no hole was selected
            polys[Poly.selected_drag].outer_pts[Poly.drag_pt] = (
                int(mouseX / Poly.cell_size) - Poly.x_offset,
                int(mouseY / Poly.cell_size) - Poly.y_offset)
        else:
            polys[Poly.selected_drag].holes[Poly.drag_hole][Poly.drag_pt] = (
                int(mouseX / Poly.cell_size) - Poly.x_offset,
                int(mouseY / Poly.cell_size) - Poly.y_offset)

def mouseReleased():
    if Poly.selected_drag >= 0 and keyPressed and keyCode == SHIFT:
        # a Poly point has been selected to be dragged
        # and SHIFT key is pressed...
        if Poly.drag_hole == -1:  # if no hole wase selected
            polys[Poly.selected_drag].outer_pts.insert(
                Poly.drag_pt, (int(mouseX / Poly.cell_size) - Poly.x_offset,
                               int(mouseY / Poly.cell_size) - Poly.y_offset))
        else:
            polys[Poly.selected_drag].holes[Poly.drag_hole].insert(
                Poly.drag_pt, (int(mouseX / Poly.cell_size) - Poly.x_offset,
                               int(mouseY / Poly.cell_size) - Poly.y_offset))

    # Poly.selected_drag = -1  # No poly selected
    Poly.drag_hole = -1  # No hole selected
    Poly.drag_pt = -1  # No point selected

def keyPressed():
    if key == "=":
        Poly.selected_drag += 1
        if Poly.selected_drag >= len(polys):
            Poly.selected_drag = -1
    if key == "d" and Poly.selected_drag >=0:
        p = deepcopy(polys[Poly.selected_drag])
        for i, pt in enumerate(p.outer_pts):
            p.outer_pts[i] = (pt[0]+2, pt[1]+1)
        polys.append(p)
        
        
    if key == " " and Poly.selected_drag >=0:
            p = polys[Poly.selected_drag]
            p.outer_pts[:] = Poly.clockwise_sort(p.outer_pts)
            for h in p.holes:
                h[:] = Poly.clockwise_sort(h)[::-1]
    # if key == "g":
    #     gif_export(GifMaker, filename=SKETCH_NAME)
    if key == "p":
        saveFrame(SKETCH_NAME + ".png")
    if key == "t":
        Poly.text_on = not Poly.text_on

    global polys
    if key == "s":
        with open("data/project.data", "wb") as file_out:
            pickle.dump(polys, file_out)
        println("project saved")

    if key == "r":
        with open("data/project.data", "rb") as file_in:
            polys = pickle.load(file_in)
        println("project loaded")

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
