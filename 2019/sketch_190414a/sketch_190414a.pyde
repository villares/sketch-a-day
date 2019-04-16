# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
"""
Unfold extrusion
"""
add_library('GifAnimation')
from gif_exporter import gif_export
from parts import Face
from glue_tab import glue_tab

faces = []
THICK = 20

def setup():
    size(740, 480, P3D)
    zig = [(2.5, 3.5), (5.5, 3.5), (2.5, 5.5),
           (5.5, 5.5), (2.5, 7.5), (5.5, 7.5),
           (3.5, 9.5), (8.5, 6.5), (5.5, 6.5),
           (8.5, 4.5), (5.5, 4.5), (8.5, 2.5),
           (5.5, 2.5), (7.5, 0.5)]
    faces.append(Face(zig, THICK))


def draw():
    background(200, 210, 220)
    for f in faces:
        f.draw_3D(frameCount / -50.)
        translate(200, 0)
        fill(170)
        f.draw_2D()
        translate(200, 0)
        fill(230)
        f.draw_2D()
        x, y = 25, 350
        translate(-400, 0)
        for p1, p2 in f.edges():
            d = dist(p1[0], p1[1], p2[0], p2[1]) * 35
            fill(250)
            glue_tab((x, y), (x + d, y))
            glue_tab((x + d, y + THICK),( x, y + THICK))
            rect(x, y , d, THICK)
            x += d
            if x > width - d:
                glue_tab((x, y), (x, y + THICK))
                x = 25
                y += THICK * 2.2
        else: # a for else...
            glue_tab((x, y), (x, y + THICK))

    if frameCount/50. < TWO_PI:
        if frameCount % 2:
            gif_export(GifMaker, filename=SKETCH_NAME)
    else:
        exit()

# print text to add to the project's README.md
def settings():
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".gif"
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
