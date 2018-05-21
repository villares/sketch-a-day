# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s141"  # 180521 Revisitig ideas from sketch s071 180312

# add_library('gifAnimation')
# from gif_exporter import *


def setup():
    print_text_for_readme(SKETCH_NAME)
    size(700, 700)
    noFill()

def draw():
    background(200)
    grid = 4
    border = 5
    space = (width - border * 2) / grid
    for x in range(grid):
        for y in range(grid):
            px = border + space / 2 + x * space
            py = border + space / 2 + y * space
            poly_shape(px, py, TWO_PI / (3 + y), x, 4, 2.7)
    #gif_export(GifMaker, frames=10, filename=SKETCH_NAME)
    saveFrame(SKETCH_NAME+".png")
    noLoop()

def poly_shape(x, y, angle, rnd, gen, S):
    with pushMatrix():
        translate(x, y)
        radius = gen * gen * S #+ random(-rnd, rnd)
        ps = createShape()  # to create a polygon on a ps PShape object
        ps.beginShape()
        a = 0
        while a < TWO_PI:
            sx = cos(a) * radius
            sy = sin(a) * radius
            ps.vertex(sx + random(-rnd, rnd), sy + random(-rnd, rnd))
            a += angle
        ps.endShape(CLOSE)  # end of PShape creation
        shape(ps, 0, 0)  # genraw the PShape
        if gen > 1:  # if the recursion 'distance'/'depth' allows...
            for i in range(ps.getVertexCount()):
                # for each vertex
                pv = ps.getVertex(i)  # gets vertex as a PVector
                # recusively call poly_shape with a smaller gen
                poly_shape(pv.x, pv.y, angle, rnd, gen - 1, S)

def keyPressed():
    loop()

def print_text_for_readme(name):
    println("""
![{0}]({0}/{0}.png)

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0})  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(name, name[1:])
    )
