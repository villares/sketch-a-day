# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s086" # 180327

add_library('gifAnimation')
from gif_exporter import gif_export
from slider import Slider
from shapes import *

A = Slider(1, 40, 10, 'q', 'a')
B = Slider(1, 40, 10, 'w', 's')
C = Slider(1, 40, 10, 'e', 'd')
D = Slider(1, 40, 10, 'r', 'f')

def setup():
    size(600, 600, P2D)
    colorMode(HSB)
    rectMode(CENTER)

    A.position(40, height - 70)
    B.position(40, height - 30)
    C.position(width - 140, height - 70)
    D.position(width - 140, height - 30)

def draw():
    background(200)
    noFill()
    
    a = int(A.val)  # number of elements
    b = int(B.val)  # size of elements
    c = int(C.val)  # space between elements
    d = int(D.val)  # number of grids
    
    randomSeed(int(d * 100)) # a different random seed

    for i in range(d):
        tam = a * c
        x = int(random(width - tam)/c)*c
        y = int(random(height - tam)/c)*c
        stroke(rnd_choice(COLORS))
        fill(rnd_choice(COLORS), 100)
        strokeWeight(int(random(1, 3)))
        grid(x, y, a, b, c, rnd_choice(SHAPES)) 
        
    # # uncomment next lines to export GIF
    # if not frameCount % 12:
    #     gif_export(GifMaker,
    #                frames=2000,
    #                delay=340,
    #                filename=SKETCH_NAME)
    
    Slider.update_all()

def grid(x, y, num, size_, space, func):  
    for i in range(x, x + num * space, space):
        for j in range(y, y + num * space, space):
            func(i, j, size_, size_)
            
def rnd_choice(collection):
    i = int(random(len(collection)))
    return collection[i]
    
# def keyPressed():
#     saveFrame(SKETCH_NAME + '_###.gif')
