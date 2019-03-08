# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# s220 20180806

from random import randint
from gif_export_wrapper import *
add_library('gifAnimation')
add_library('peasycam')

GRID_SIZE = 32
SKETCH_NAME = "s220b"
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

    # Node.nodes is a list of nodes in a 3D grid
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            for z in range(GRID_SIZE):
                new_node = Node(x, y, z)
                Node.nodes.append(new_node)
                Node.grid[x, y, z] = new_node

    m = GRID_SIZE - 1
    box_list = []
    num_boxes = 16
    for i in range(num_boxes):
        x = randint(0, m - 3)
        y = randint(0, m - 3)
        z = randint(0, m - 3)
        w = randint(3, m - x + 4) - 2
        h = randint(3, m - y + 4) - 2
        d = randint(3, m - z + 4) - 2
        box_list.append((x, y, z, w, h, d))
    for i in range(num_boxes):
        x, y, z, w, h, d = box_list[i]
        big_box(x, y, z, w, h, d,
                color( (i % 4) * 50, 200, 200))
    for i in range(num_boxes):
        x, y, z, w, h, d = box_list[i]
        side = (i % 3) + 1
        if side == 1:
            h -= 1
            w -= 1
            z -= 1
        elif side == 2:
            d -= 1
            h -= 1
            x -= 1
        else:
            w -= 1
            d -= 1
            y -= 1
        big_box(x + 1, y + 1, z + 1, w - 1, h - 1, d - 1,
                None) #color(255))


def draw():
    lights()
    # arbitray rotation
    rotate(-1 + (TWO_PI * frameCount / 200.), 1 / 2, 1, 1 / 2)
    background(100)

    for node in Node.nodes:
        node.plot()

    if frameCount / 200. < 1:
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
            # noStroke()  # stroke(0)
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
