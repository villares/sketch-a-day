# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

"""
First trial of the JCSG library prepared for Processing by George Profenza https://stackoverflow.com/users/89766/george-profenza
"""
# You'll need to copy these libs into your Processing libraries folder:
add_library('VVecMath')
add_library('jcsg')

from random import choice

dim = (2, 3, 4, 5, 6)


def setup():
    global pshape_result
    size(600, 500, P3D)
    noStroke()
    csg_result = calculate_stuff()
    pshape_result = CSGToPShape(csg_result, 45)


def draw():
    background(0)
    lights()
    translate(width * 0.5, height * 0.5, -height/2)
    rotateY(map(mouseX, 0, width, -PI, PI))
    rotateX(map(mouseY, 0, height, PI, -PI))
    shape(pshape_result)


def calculate_stuff():
    solids = []
    for i, s in enumerate(range(5)):
        w, h, d = choice(dim), choice(dim), choice(dim)
        cube = Cube(w, h, d).toCSG()
        if w % 2:
            hole = Cube(w-1, h, d-1).toCSG()
        else:
            hole = Cube(w, h-1, d-1).toCSG()
        solid = cube.difference(hole)
        solids.append(csgTranslate(solid, i * 3, 0, 0))

    union = solids[0].union(solids[1:])

    # translate merged geometry back by half to pivot around centre
    return csgTranslate(union, -6, 0, 0)


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
    for p in mesh.getPolygons():
        # make a child PShape
        polyShape = createShape()
        # begin setting vertices to it
        polyShape.beginShape()
        # for each vertex in the polygon
        for v in p.vertices:
            # add each (scaled) polygon vertex
            polyShape.vertex(v.pos.getX() * scale,
                             v.pos.getY() * scale,
                             v.pos.getZ() * scale)

        # finish this polygon
        polyShape.endShape()
        # append the child PShape to the parent
        result.addChild(polyShape)

    return result

def keyPressed():
    if key == "p":
        saveFrame("###.png")
    if key == " ":
         global pshape_result
         csg_result = calculate_stuff()
         pshape_result = CSGToPShape(csg_result, 45)

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
