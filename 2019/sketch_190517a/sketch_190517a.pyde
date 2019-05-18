# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
from __future__ import division
from random import choice
from ensamble import Ensamble

add_library('GifAnimation')
from gif_exporter import gif_export

SPACING, MARGIN = 100, 250
grid = []
N = 8

combinations = ((0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 5),
                (0, 1, 6), (0, 1, 7), (0, 2, 3), (0, 2, 4),
                (0, 2, 5), (0, 2, 6), (0, 2, 7), (0, 3, 4),
                (0, 3, 5), (0, 3, 6), (0, 3, 7), (0, 4, 5),
                (0, 4, 6), (0, 4, 7), (0, 5, 6), (0, 5, 7),
                (0, 6, 7), (1, 2, 3), (1, 2, 4), (1, 2, 5),
                (1, 2, 6), (1, 2, 7), (1, 3, 4), (1, 3, 5),
                (1, 3, 6), (1, 3, 7), (1, 4, 5), (1, 4, 6),
                (1, 4, 7), (1, 5, 6), (1, 5, 7), (1, 6, 7),
                (2, 3, 4), (2, 3, 5), (2, 3, 6), (2, 3, 7),
                (2, 4, 5), (2, 4, 6), (2, 4, 7), (2, 5, 6),
                (2, 5, 7), (2, 6, 7), (3, 4, 5), (3, 4, 6),
                (3, 4, 7), (3, 5, 6), (3, 5, 7), (3, 6, 7),
                (4, 5, 6), (4, 5, 7), (4, 6, 7), (5, 6, 7))
def setup():
    global grid_list, rad_list
    size(700, 700)
    W, H = 700, 700
    X_LIST = [x for x in range(MARGIN, 1 + W - MARGIN, SPACING)]
    Y_LIST = [y for y in range(MARGIN, 1 + H - MARGIN, SPACING)]
    print X_LIST
    grid_list = []
    for x in X_LIST:
        for y in Y_LIST:
            grid_list.append((x, y))
    grid_list.pop(len(grid_list) // 2)
    rad_list = [20, 40, 60, 80, 100, 120, 140, 160] 
    
    create_grid(grid_list, rad_list)
    
    

def create_grid(grid_list, rad_list):

    for a, b, c in combinations:
        va = PVector(*grid_list[a])
        vb = PVector(*grid_list[b])
        vc = PVector(*grid_list[c])
        e = Ensamble((va, vb, vc), [rad_list[a], rad_list[b], rad_list[c]])
        grid.append(e)

def draw():
    translate(0, 50)
    scale(1 / N, 1 / N)
    background(250, 250, 240)
    for x in range(N):
        for y in range(N):
            pushMatrix()
            translate(x * 700, y * 700)
            if x + y * N < 56:
                grid[x + y * N].plot()
            popMatrix()


def keyPressed():
    if key == " ":
        grid[:] = []
        rad_list[:] = rad_list[1::].extend(rad_list[0])
        create_grid(grid_list, rad_list)
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
