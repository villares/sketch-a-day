# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s144"  # 180524

add_library('gifAnimation')
from gif_export_wrapper import *

def setup():
    print_text_for_readme(SKETCH_NAME)
    size(700, 700, P3D)
    noFill()
    ortho()


def draw():
    background(200)
    translate(width / 2, height / 2)
    grid = 4
    border = 0
    space = (width - border * 2) / grid
    for x in range(grid):
        for y in range(grid):
            px = border + space / 2 + x * space
            py = border + space / 2 + y * space
            with pushMatrix():
                translate(px - width / 2, py - height / 2)
                rotateX(PI * frameCount / 25.)
                rotateY(PI * frameCount / 100.)
                poly_shape(0, 0, TWO_PI / 4, rot=y + 1, gen=4, scaling=x)

    gif_export(GifMaker, repeat=1, frames=99, filename=SKETCH_NAME)

def poly_shape(x, y, angle, rot, gen, scaling):
    rnd = 0
    with pushMatrix():
        translate(x, y)
        rotate(angle / rot)
        # + random(-rnd, rnd)
        radius = map(scaling, 0, 3, gen * 8, gen ** 2 * 2.7)
        ps = createShape()  # to create a polygon on a ps PShape object
        ps.beginShape()
        a = 0
        while a < TWO_PI:
            sx = cos(a) * radius
            sy = sin(a) * radius
            ps.vertex(sx + random(-rnd, rnd), sy + random(-rnd, rnd))
            a += angle
        ps.endShape(CLOSE)  # end of PShape creation
        if keyPressed:
            shape(ps, 0, 0)
        else:
            with pushMatrix():
                rotate(PI / 4)
                box(radius * sqrt(2))  # Draw the PShape

        if gen > 1:  # if the recursion 'distance'/'depth' allows...
            for i in range(ps.getVertexCount()):  # for each vertex
                pv = ps.getVertex(i)  # gets vertex as a PVector
                # recusively call poly_shape with a smaller D
                poly_shape(pv.x, pv.y, angle, rot, gen - 1, scaling)

def keyPressed():
    loop()

def print_text_for_readme(name):
    println("""
![{0}]({0}/{0}.gif)

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:])
    )
