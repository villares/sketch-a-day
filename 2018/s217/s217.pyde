# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# s216 20180802

from random import randint
from gif_export_wrapper import *
add_library('gifAnimation')
add_library('peasycam')

GRID_SIZE = 32
SKETCH_NAME = "s217"
OUTPUT = ".gif"

def setup():
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    size(700, 700, P3D)
    # hint(ENABLE_DEPTH_SORT)
    # optional PeasyCam setup to allow orbiting with a mouse drag
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(1000)
    cam.setMaximumDistance(1000)
    # sets border and grid spacing
    Node.border = 50
    Node.spacing = (width - Node.border * 2) / GRID_SIZE

    # Node.nodes is a list of nodes in a 3D grid
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            for z in range(GRID_SIZE):
                new_node = Node(x, y, z)
                Node.nodes.append(new_node)
                Node.grid[x, y, z] = new_node

    m = GRID_SIZE - 1
    for s in range(GRID_SIZE):
        Node.grid[(0, 0, s)].cor = color(255, 0, 0)
        Node.grid[(0, s, 0)].cor = color(0, 0, 255)
        Node.grid[(s, 0, 0)].cor = color(0, 255, 0)
        Node.grid[(m, m, s)].cor = color(255, 0, 0)
        Node.grid[(m, s, m)].cor = color(0, 0, 255)
        Node.grid[(s, m, m)].cor = color(0, 255, 0)
        Node.grid[(0, m, s)].cor = color(255, 0, 0)
        Node.grid[(0, s, m)].cor = color(0, 0, 255)
        Node.grid[(s, 0, m)].cor = color(0, 255, 0)
        Node.grid[(m, 0, s)].cor = color(255, 0, 0)
        Node.grid[(m, s, 0)].cor = color(0, 0, 255)
        Node.grid[(s, m, 0)].cor = color(0, 255, 0)
    for i in range(1,50):
        c = 255 if i < 25 else None
        x = randint(1,m)-1
        y = randint(1,m)-1
        z = randint(1,m)-1
        w = randint(1,m-x+1)-1
        h = randint(1,m-y+1)-1
        d = randint(1,m-z+1)-1
        big_box(x, y, z, w, h, d, c) 



def draw():
    lights()
    # arbitray rotation
    rotate(-1 + TWO_PI / (GRID_SIZE * 2) * frameCount, 1 / 2, 1, 1 / 2)
    background(100)

    for node in Node.nodes:
        node.plot()

    if frameCount < GRID_SIZE*2:
        gif_export(GifMaker, filename=SKETCH_NAME)
    else:
        gif_export(GifMaker, finish=True)


def big_box(px, py, pz, w, h=None, d=None, c=255):
    h = h if h else w
    d = d if d else w
    for x in range(px, px + w):
        for y in range(py, py + h):
            for z in range(pz, pz + d):
                if (0 <= x < GRID_SIZE and
                    0 <= y < GRID_SIZE and
                    0 <= z < GRID_SIZE):
                    Node.grid[(x, y, z)].cor = c


class Node():
    nodes = []
    grid = dict()

    def __init__(self, x, y, z):
        self.ix = x
        self.iy = y
        self.iz = z
        self.x = Node.border + Node.spacing / 2 + x * Node.spacing - width / 2
        self.y = Node.border + Node.spacing / 2 + y * Node.spacing - width / 2
        self.z = Node.border + Node.spacing / 2 + z * Node.spacing - width / 2
        self.size_ = 1
        self.cor = None

    def plot(self):
        """ draws box """
        if self.cor:
            #noStroke()  # stroke(0)
            fill(self.cor)
            with pushMatrix():
                translate(self.x, self.y, self.z)
                box(Node.spacing * self.size_)


def keyPressed():
    """ press P to save an image """
    if key in ['p', 'P']:
        saveFrame("####" + SKETCH_NAME + OUTPUT)

def print_text_for_readme(name, output):
    """ prints text in the console to add to project README.md """
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
