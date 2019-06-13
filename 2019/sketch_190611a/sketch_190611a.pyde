# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
"""
A minimal poly editor
r: load polys from pickled data
s: save polys
t: show pt annotations
SHIFT: to drag-add points
CONTROL: to remove points
01234567890-: change vertex radius (- makes it -1, "hidden")
m + drag - move whole poly

TODO: Create modes for move, add vertex, change vertex, remove vertex
"""
import pickle
from poly import Poly
add_library('GifAnimation')
from gif_exporter import gif_export


def setup():
    size(500, 500)

    f = createFont("Fira Mono", 16)
    textFont(f)

    CELL_SIZE = 20
    order = width // CELL_SIZE
    x_offset = y_offset = int(order // 2)
    Poly.setup_grid(CELL_SIZE, order, x_offset, y_offset)
    # p1 = Poly([(0, 0, -1), (6, 0, 1), (6, 6, 1), (0, 6, 0)])
    # Poly.polys.append(p1)
    # p2 = Poly([(-1, -1, 0), (-6, -1, 0), (-6, -6, 0), (-1, -6, 0)],
    #           holes=[[(-2, -3, 0), (-3, -3, 1), (-2, -2, 0)]])
    # Poly.polys.append(p2)

def draw():
    background(230)
    # grade
    Poly.draw_grid()
    # polígonos
    for p in Poly.polys:
        p.plot()

def mousePressed():
    Poly.mouse_pressed()

def mouseDragged():
    Poly.mouse_dragged()

def mouseReleased():
    Poly.mouse_released()
    
def keyPressed():
    if key == "=":
        Poly.selected_drag += 1
        if Poly.selected_drag >= len(Poly.polys):
            Poly.selected_drag = -1
    if key == "d":
        Poly.duplicate_selected()

    if key == " " and Poly.selected_drag >= 0:
        p = Poly.polys[Poly.selected_drag]
        p.pts[:] = Poly.clockwise_sort(p.pts)
        for h in p.holes:
            h[:] = Poly.clockwise_sort(h)[::-1]
    if key == "g":
        gif_export(GifMaker, filename=SKETCH_NAME)
    if key == "p":
        saveFrame(SKETCH_NAME + ".png")
    if key == "t":
        Poly.text_on = not Poly.text_on
    if key == "c" and Poly.selected_drag >= 0:
        p = Poly.polys[Poly.selected_drag]
        p.closed = not p.closed
        if p.closed:
            p.lw = 1
        else:
            p.lw = 5

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
