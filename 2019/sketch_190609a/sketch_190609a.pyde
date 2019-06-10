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


def setup():
    size(500, 500, P2D)

    f = createFont("Fira Mono", 16)
    textFont(f)

    CELL_SIZE = 15
    order = width // CELL_SIZE
    x_offset = y_offset = int(order // 2)
    Poly.setup_grid(CELL_SIZE, order, x_offset, y_offset)
    p1 = Poly([(0, 0, 2), (6, 0, 1), (6, 6, 3), (0, 6, 4)])
    Poly.polys.append(p1)
    p2 = Poly([(-1, -1), (-6, -1), (-6, -6), (-1, -6)],
              holes=[[(-2, -3), (-3, -3), (-2, -2)]])
    Poly.polys.append(p2)

def draw():
    background(230)
    # grade
    Poly.draw_grid()
    # polígonos
    for p in Poly.polys:
        p.plot()

def mousePressed():
    Poly.mousePressed()

def mouseDragged():
    Poly.mouseDragged()

def mouseReleased():
    Poly.mouseReleased()
    
def keyPressed():
    if key == "=":
        Poly.selected_drag += 1
        if Poly.selected_drag >= len(Poly.polys):
            Poly.selected_drag = -1
    if key == "d" and Poly.selected_drag >= 0:
        new_poly = deepcopy(Poly.polys[Poly.selected_drag])
        for i, pt in enumerate(new_poly.pts):
            new_poly.pts[i] = (pt[0] + 2, pt[1] + 1)
        for h in new_poly.holes:
            for i, pt in enumerate(h):
                h[i] = (pt[0] + 2, pt[1] + 1)
        Poly.polys.append(new_poly)

    if key == " " and Poly.selected_drag >= 0:
        p = Poly.polys[Poly.selected_drag]
        p.pts[:] = Poly.clockwise_sort(p.pts)
        for h in p.holes:
            h[:] = Poly.clockwise_sort(h)[::-1]
    # if key == "g":
    #     gif_export(GifMaker, filename=SKETCH_NAME)
    if key == "p":
        saveFrame(SKETCH_NAME + ".png")
    if key == "t":
        Poly.text_on = not Poly.text_on

    if key == "s":
        with open("data/project.data", "wb") as file_out:
            pickle.dump(Poly.polys, file_out)
        println("project saved")

    if key == "r":
        with open("data/project.data", "rb") as file_in:
            Poly.polys = pickle.load(file_in)
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
