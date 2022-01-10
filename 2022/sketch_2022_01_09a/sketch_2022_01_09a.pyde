add_library('VVecMath')
add_library('jcsg')

from random import choice
from csg_helpers import CSGToPShape

dim = (200, 300, 400, 500)


def setup():
    global pshape_result
    size(600, 500, P3D)
    hint(ENABLE_DEPTH_TEST)
    hint(ENABLE_DEPTH_SORT)
    # fill(100, 200, 200, 240)
    pshape_result = calculate_stuff()


def draw():
    background(0)
    lights()
    translate(width * 0.5, height * 0.5, -height)
    rotateY(map(mouseX, 0, width, -PI, PI))
    rotateX(0)
    for ps in pshape_result:
        shape(ps)


def calculate_stuff():
    solids, holes = [], []
    thick = 50
    for i, s in enumerate(range(3)):
        w, h, d = choice(dim), choice(dim), choice(dim)
        solid = Cube(w, h, d).toCSG()
        if w / 100 % 2:
            hole = Cube(w - thick, h, d - thick).toCSG()
        else:
            hole = Cube(w, h - thick, d - thick).toCSG()
        move = choice(dim)
        if move / 100 % 2:
            hole = csgRot(hole, 15, 0, 0)
            solid = csgRot(solid, 15, 0, 0)
        solids.append(csgTranslate(solid, move - 250, 0, 0))
        holes.append(csgTranslate(hole, move - 250, 0, 0))

    mass = solids[0].union(solids[1:])
    void = holes[0].union(holes[1:])
    sub_result = mass.difference(void)
    results = []
    for s in solids:
        results.append(sub_result.intersect(s))
    for i, r in enumerate(results):
        results[i] = r.difference(solids[i - 1])
        
    colors = [lambda i: color(i % 255, 100, 100),
              lambda i: color(i % 255, 127, 100),
              lambda i : color(i % 255, 100, i % 255)]
    return [CSGToPShape(r, 1, choice(colors))
            for i, r in enumerate(results)]


def keyPressed():
    if key == "p":
        saveFrame("###.png")
    if key == " ":
        global pshape_result
        pshape_result = calculate_stuff()




def csgTranslate(csg, x, y, z):
    return csg.transformed(Transform.unity().translate(x, y, z))

def csgRot(csg, x, y, z):
    return csg.transformed(Transform.unity().rot(x, y, z))
   
