# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s285"  # 20181010
OUTPUT = ".gif"
GRID_SIZE = 10

from random import seed
from random import choice
from random import randint

from node import Node

def setup():
    global ang
    ang = 0
    size(500, 500)
    strokeWeight(2)
    rectMode(CENTER)
    random_seed(101)
    init_grid(GRID_SIZE)
            
def draw():
    translate(width/2, height/2)
    background(200)
    
    ang = frameCount/31.
    
    for node in Node.nodes:
        node.plot(ang)
    
    if not frameCount % 12:
        init_grid(GRID_SIZE)    
                
    if ang <= PI:
        saveFrame("###.png")
    else:
        noLoop()
                                            
def init_grid(grid_size):
    Node.border = 50
    Node.spacing = (width - Node.border * 2) / grid_size
    Node.nodes = []
    for x in range(grid_size):
        for y in range(grid_size):
                new_node = Node(x, y)
                Node.nodes.append(new_node)

 
def keyPressed():
    if key == "n":
        init_grid(GRID_SIZE)
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
