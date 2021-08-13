import pickle
from poly import Poly

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
        Poly.selected_drag = (Poly.selected_drag + 1) % len(Poly.polys)
    if key == "d":
        Poly.duplicate_selected()

    if key == " " and Poly.selected_drag >= 0:
        p = Poly.polys[Poly.selected_drag]
        p.pts[:] = Poly.clockwise_sort(p.pts)
        for h in p.holes:
            h[:] = Poly.clockwise_sort(h)[::-1]
    if key == "p":
        saveFrame("####.png")
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
        try:
            with open("data/project.data", "rb") as file_in:
                Poly.polys = pickle.load(file_in)
            println("project loaded")
        except IOError:
            println("not found")
