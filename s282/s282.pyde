# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s282"  # 20181007
OUTPUT = ".gif"
GRID_SIZE = 8

add_library('peasycam')
from random import seed
from random import choice
from random import randint

from node import Node

def setup():
    size(500, 500, P3D)
    colorMode(HSB)
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(750)
    cam.setMaximumDistance(750)
    random_seed(100)
    init_grid(GRID_SIZE)

            
def draw():
    background(200)
    #strokeWeight(2)
    for node in Node.nodes:
        node.plot()
                                                
def init_grid(grid_size):
    Node.border = 0
    Node.spacing = (width - Node.border * 2) / grid_size
    Node.nodes = []
    for x in range(grid_size):
        for y in range(grid_size):
            for z in range(grid_size):
                new_node = Node(x, y, z)
                Node.nodes.append(new_node)
                Node.grid[x, y, z] = new_node
                if randint(1, 10) > 5:
                    new_node.cor = 1 #color(z * 32, 255, 255)
                else:
                    new_node.cor = None

    for node in Node.nodes:
        nb0 = Node.grid.get((node.ix-1, node.iy, node.iz))
        node.nb[0] = True if nb0 and nb0.cor else False
        nb1 = Node.grid.get((node.ix+1, node.iy, node.iz))
        node.nb[1] = True if nb1 and nb1.cor else False
        nb2 = Node.grid.get((node.ix, node.iy-1, node.iz))
        node.nb[2] = True if nb2 and nb2.cor else False
        nb3 = Node.grid.get((node.ix, node.iy+1, node.iz))
        node.nb[3] = True if nb3 and nb3.cor else False

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
