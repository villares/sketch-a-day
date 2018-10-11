# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s284"  # 20181009
OUTPUT = ".gif"
GRID_SIZE = 6

add_library('peasycam')
from random import seed
from random import choice
from random import randint

from node import Node

def setup():
    global ang
    ang = 0
    size(500, 500, P3D)
    colorMode(HSB)
    strokeWeight(2)
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(750)
    cam.setMaximumDistance(750)
    random_seed(101)
    init_grid(GRID_SIZE)

            
def draw():
    global ang
    background(0)
    rotateY(ang)
    for node in Node.nodes:
        node.plot()

    for l in range(GRID_SIZE):         
        beginShape()    
        for x, y, z, iz in Node.ver:
            if l == iz:
                vertex(x, y, z+1)
        endShape()
    
    if ang <= TWO_PI:
        #saveFrame("###.png")
        ang += 0.02
                                                
def init_grid(grid_size):
    Node.border = 10
    Node.spacing = (width - Node.border * 2) / grid_size
    Node.nodes = []
    Node.ver = []
    for x in range(grid_size):
        for y in range(grid_size):
            for z in range(grid_size):
                new_node = Node(x, y, z)
                Node.nodes.append(new_node)
                Node.grid[x, y, z] = new_node
                if randint(1, 10) > 5:
                    new_node.cor = color(z * 28, 255, 255)
                else:
                    new_node.cor = None

    for node in Node.nodes:
        node.update_nbs()
        
    for node in Node.nodes:
        for x1, y1, x2, y2 in node.borders:
                Node.ver.append((x1, y1, node.z, node.iz))
                Node.ver.append((x2, y2, node.z, node.iz))


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
