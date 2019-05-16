# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# rework of sketch_190401b
from __future__ import division
from random import choice
from ensamble import Ensamble

add_library('GifAnimation')
from gif_exporter import gif_export

grid = []
N = 5

def setup():
    size(740, 740)
    for _ in range(N * N):    
        grid.append(Ensamble())


def draw():
    translate(20, 20)
    scale(1/N, 1/N)
    background(250, 250, 240)
    for x in range(N):
        for y in range(N):
            pushMatrix()
            translate(x * 700, y * 700)
            grid[x + y * N].plot()
            popMatrix()



def keyPressed():
    # if key == " ":
    #         # e.create_list()
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
