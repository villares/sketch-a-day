# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# s223 20180809

from __future__ import division
# made my own randint #from random import randint
from gif_export_wrapper import *
add_library('gifAnimation')
add_library('peasycam')

GRID_SIZE = 32
SKETCH_NAME = "s223"
OUTPUT = ".gif"

def setup():
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    size(700, 700, P3D)
    colorMode(HSB)
    # hint(ENABLE_DEPTH_SORT)
    # optional PeasyCam setup to allow orbiting with a mouse drag
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(1000)
    cam.setMaximumDistance(1000)
    # sets border and grid spacing
    Node.border = 50
    Node.spacing = (width - Node.border * 2) / GRID_SIZE
    stroke(0, 10)
    # Node.nodes is a list of nodes in a 3D grid
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            for z in range(GRID_SIZE):
                new_node = Node(x, y, z)
                Node.nodes.append(new_node)
                Node.grid[x, y, z] = new_node
    create_new_boxes()


def create_new_boxes():
    #seed = 205
    seed = int(random(1000))
    println("seed: {}".format(seed))
    randomSeed(seed)
    m = GRID_SIZE - 1
    box_list = []
    num_boxes = 10
    border = 3
    for i in range(num_boxes):
        x = randint(border, m - border)
        y = randint(border, m - border)
        z = randint(border, m - border)
        w = randint(3, m - x)
        h = randint(3, m - y)
        d = randint(3, m - z)
        t = (x, y, z, w, h, d)
        print(t)
        box_list.append(t)
    # box
    for i in range(num_boxes):
        x, y, z, w, h, d = box_list[i]
        big_box(x, y, z, w, h, d,
                color((i % 6) * 255 / 12, 200, 200))
    # void
    for i in range(num_boxes):
        x, y, z, w, h, d = box_list[i]
        side = (i % 3) + 1
        if side == 1:
            h -= 2
            w -= 2
            z -= 1
        elif side == 2:
            d -= 2
            h -= 2
            x -= 1
        else:
            w -= 2
            d -= 2
            y -= 1
        big_box(x + 1, y + 1, z + 1, w, h, d,
                None)
                # use color(0) to debug
                # color(0))


def draw():
    lights()
    background(100)
    rotateX(HALF_PI)
    rotateZ(HALF_PI)

    for node in Node.nodes:
        node.plot()


def keyPressed():
    """ press P to save an image """
    if key in ['p', 'P']:
        saveFrame("####" + SKETCH_NAME + OUTPUT)
    if key == " ":
        for node in Node.nodes:
            node.cor = None
        create_new_boxes()
        gif_export(GifMaker, delay=1000, filename=SKETCH_NAME)
    if key == "f":
        gif_export(GifMaker, finish=True)


def big_box(px, py, pz, w, h=None, d=None, c=255):
    h = h if h else w
    d = d if d else w
    for z in range(pz, pz + d):
        for y in range(py, py + h):
            for x in range(px, px + w):
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
            # noStroke()  # stroke(0)
            if self.cor == color(0):
                noFill()
            else:
                fill(self.cor)
            with pushMatrix():
                translate(self.x, self.y, self.z)
                box(Node.spacing * self.size_)

def randint(a, b=None):
    if not b:
        b = a
        a = 0
    return int(random(a, b + 1))


def print_text_for_readme(name, output):
    """ prints text in the console to add to project README.md """
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
