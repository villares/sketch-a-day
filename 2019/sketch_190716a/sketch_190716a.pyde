# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# Using JCSG library prepared for Processing by George Profenza
# A new take on my experiments with boxes from last year
# Now I can twist Cylinders!


# You'll need to copy these libs into your Processing libraries folder:
add_library('VVecMath')
add_library('jcsg')

from random import choice

dim = (200, 300, 400, 500)


def setup():
    global pshape_result
    size(600, 500, P3D)
    hint(ENABLE_DEPTH_TEST)
    hint(ENABLE_DEPTH_SORT)
    pshape_result = calculate_stuff()


def draw():
    background(100)
    lights()
    translate(width * 0.5, height * 0.5, -height)
    rotateY(map(mouseX, 0, width, -PI, PI))
    rotateX(map(mouseY, 0, height, PI, -PI))

    shape(pshape_result)


def calculate_stuff():
    solids, holes = [], []
    thick = 50
    for i, s in enumerate(range(3)):
        w, h, d = choice(dim), choice(dim), choice(dim)
        solid = Cube(w, h, d).toCSG()
        if w / 100 % 2:
            hole = csgTranslate(Cylinder(d, w, 32).toCSG(), 0, 0, -w / 2)
            # hole = Cube(w - thick, h, d - thick).toCSG()
            # hole = csgRot(hole, 0, 90, 0)
        else:
            hole = csgTranslate(Cylinder(h, w, 32).toCSG(), 0, 0, -w / 2)
            # hole = Cube(w, h - thick, d - thick).toCSG()
        hole = csgTranslate(Cylinder(200, w, 16).toCSG(), 0, 0, -w / 2)
        move = choice(dim)
        if move / 100 % 2:
            hole = csgRot(hole, 15, 0, 0)
            solid = csgRot(solid, 15, 0, 0)
        solids.append(csgTranslate(solid, move - 250, 0, 0))
        holes.append(csgTranslate(hole, move - 250, 0, 0))

    mass = solids[0].union(solids[1:])
    void = holes[0].union(holes[1:])
    result = mass.difference(void)

    return CSGToPShape(result, 1)


def csgTranslate(csg, x, y, z):
    return csg.transformed(Transform.unity().translate(x, y, z))

def csgRot(csg, x, y, z):
    return csg.transformed(Transform.unity().rot(x, y, z))

def CSGToPShape(mesh, scale):
    """
    Convert a CSG mesh to a Processing PShape
    """
    result = createShape(GROUP)  # allocate a PShape group
    # for each polygon (Note: these can have 3,4 or more vertices)
    final_i = len(mesh.getPolygons())
    for i, p in enumerate(mesh.getPolygons()):
        # make a child PShape
        polyShape = createShape()
        # begin setting vertices to it
        polyShape.beginShape()
        # for each vertex in the polygon
        for v in p.vertices:
            # add each (scaled) polygon vertex
            polyShape.vertex(v.pos.x * scale,
                             v.pos.y * scale,
                             v.pos.z * scale)

        # finish this polygon
        polyShape.endShape()
        polyShape.setFill(color(100, 200, map(i, 0, final_i, 0, 255)))
        polyShape.setStroke(False)
        # append the child PShape to the parent
        result.addChild(polyShape)

    return result

def keyPressed():
    if key == "p":
        saveFrame("###.png")
    if key == " ":
        global pshape_result
        pshape_result = calculate_stuff()

def settings():
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".png"
    println(
        """
![{0}]({2}/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT, year())
    )
