# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# rework of sketch_190401b

from random import choice
from polys import poly, poly_arc_augmented
add_library('GifAnimation')
from gif_exporter import gif_export

SPACING, MARGIN = 50, 150
X_LIST, Y_LIST = [], []  # listas de posições para elementos
rad_list = [80, 40, 20, 10] ##list(range(5, 50, 10))

def setup():
    size(500, 500)
    X_LIST[:] = [x for x in range(MARGIN, 1 + width - MARGIN, SPACING)]
    Y_LIST[:] = [y for y in range(MARGIN, 1 + height - MARGIN, SPACING)]
    create_list()

def create_list():
    global p_list
    p_list = []
    for r in rad_list:
        new_p = PVector(choice(X_LIST), choice(Y_LIST))
        while new_p in p_list:
            new_p = PVector(choice(X_LIST), choice(Y_LIST))
        p_list.append(new_p)

def draw():
    background(240)
    noFill()
    strokeWeight(5)
    stroke(50, 50, 255)
    strokeJoin(ROUND)
    poly(p_list)
    strokeWeight(2)
    stroke(0, 0, 0)
    for _ in rad_list:
        poly_arc_augmented(p_list, rad_list)
        rad_list[:] = [rad_list[-1]] + rad_list[:-1]


def keyPressed():
    if key == " ":
            create_list()
    if key == "s":
        saveFrame("###.png")
    if key == "g":
        gif_export(GifMaker, filename=SKETCH_NAME, delay=1200)   
        
def settings():
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".gif"
    println(
        """
![{0}]({2}/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT, year())
    )
