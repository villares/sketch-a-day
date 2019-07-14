# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

"""
First trial of the JCSG library prepared for Processing by George Profenza https://stackoverflow.com/users/89766/george-profenza
"""
# You'll need to copy these libs into your Processing libraries folder:
add_library('VVecMath')
add_library('jcsg')

from csg_helpers import *

def setup():
    global pshape_result
    size(600, 500, P3D)
    noStroke()
    csg_result = calculate_stuff()
    pshape_result = CSGToPShape(csg_result, 45)


def draw():
    background(0)
    lights()
    translate(width * 0.5, height * 0.5, 0)
    rotateY(map(mouseX, 0, width, -PI, PI))
    rotateX(map(mouseY, 0, height, PI, -PI))
    shape(pshape_result)


def calculate_stuff():
    global csgResult  # the PShape reference which will contain the converted

    # Jsample code:
    # we use cube and sphere_ as base geometries
    cube = RoundedCube(2).toCSG()
    sphere_ = Sphere(1.25).toCSG()

    # perform union, difference and intersection
    cubePlusSphere = cube.union(sphere_)
    cubePlusSphere = csgTranslate(cubePlusSphere, 6, 0, 0)

    cubeMinusSphere = cube.difference(sphere_)
    cubeMinusSphere = csgTranslate(cubeMinusSphere, 9, 0, 0)

    cubeIntersectSphere = cube.intersect(sphere_)
    cubeIntersectSphere = csgTranslate(cubeIntersectSphere, 12, 0, 0)

    sphere_ = csgTranslate(sphere_, 3, 0, 0)
    union = cube.union((sphere_,
                        cubePlusSphere,
                        cubeMinusSphere,
                        cubeIntersectSphere))

    # translate merged geometry back by half to pivot around centre
    return csgTranslate(union, -6, 0, 0)


def keyPressed():
    saveFrame("###.png")


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
