# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s286"  # 20181011
OUTPUT = ".gif"
GRID_SIZE = 10
BORDER = 50
trans = False
ang = -HALF_PI

from random import seed
from random import choice
from node import Node

def setup():
    size(500, 500)
    strokeWeight(2)
    rectMode(CENTER)
    frameRate(10)
    random_seed(101)
    Node.init_grid(GRID_SIZE, BORDER)
            
def draw():
    translate(width/2, height/2)
    background(200)
    
    for node in Node.nodes:
        node.plot(ang)

    global ang            
    if ang < TWO_PI * 2:
        #saveFrame("###.png")
        ang += 0.03
        if abs(ang - TWO_PI) <= 0.03:
            Node.send_back()
            
 
def keyPressed():
    if key == "n":
        Node.init_grid(GRID_SIZE, BORDER)
    if key == "s": saveFrame("###.png")
    
    
def random_seed(s=None):
    global rnd_seed
    if s:
        rnd_seed = s
        seed(rnd_seed)
        randomSeed(rnd_seed)    
    else:
        seed(rnd_seed)
        randomSeed(rnd_seed)
    
# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
