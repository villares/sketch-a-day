# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# Using JCSG library prepared for Processing by George Profenza
# Work in progress...

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
    # fill(100, 200, 200, 240)
    pshape_result = calculate_stuff()


def draw():
    background(240)
    lights()
    translate(width * 0.5, height * 0.5, -height)
    rotateY(map(mouseX, 0, width, -PI, PI))
    rotateX(map(mouseY, 0, height, PI, -PI))
    for ps in pshape_result:
        shape(ps)


def calculate_stuff():
    solids, holes = [], []
    thick = 50
    for i, s in enumerate(range(2)):
        w, h, d = choice(dim), choice(dim), choice(dim)
        move = choice(dim)
        solid = csgCuboid(w, h, d, x=move-250)
        solids.append(solid)
        if w / 100 % 2:
            hole = csgCuboid(w - thick, h, d - thick, x=move-250)
            holes.append(hole)
        else:
            hole = csgCuboid(w, h - thick, d - thick)
            holes.append(hole)
            hole = csgRot(csgCylinder(100, h, x=move-250), 90, 0, 0)
            holes.append(hole)

        # if move / 100 % 2:
        #     hole = csgRot(hole, 15, 0, 0)
        #     solid = csgRot(solid, 15, 0, 0)

        

    mass = solids[0].union(solids[1:])
    void = holes[0].union(holes[1:])
    sub_result = mass.difference(void)
    results = []
    for s in solids:
        results.append(sub_result.intersect(s))
    for i, r in enumerate(results):
        results[i] = r.difference(solids[i - 1])
    results.append(solids[0].intersect(solids[1]).intersect(sub_result))
    
    
    colors = [lambda: color(100, random(50), 0),
              lambda: color(0, 100, random(50)),
              lambda: color(0, 50, 100)]
    return [CSGToPShape(r, 1, colors[i % len(results)])
            for i, r in enumerate(results)]

def csgCuboid(w, h, d, x=0, y=0, z=0):
    return csgTranslate(Cube(w, h, d).toCSG(), x, y, z)


def csgCylinder(d, w, x=0, y=0, z=0):
    return csgTranslate(Cylinder(d, w, 32).toCSG(), x, y, z-w / 2)

def csgTranslate(csg, x, y, z):
    return csg.transformed(Transform.unity().translate(x, y, z))

def csgRot(csg, x, y, z):
    return csg.transformed(Transform.unity().rot(x, y, z))

def CSGToPShape(mesh, scale, color_maker):
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
            polyShape.vertex(v.pos.x * scale,
                             v.pos.y * scale,
                             v.pos.z * scale)

        # finish this polygon
        polyShape.endShape()
        polyShape.setFill(color_maker())
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
