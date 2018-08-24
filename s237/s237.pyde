# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s237" #20180823

# made my own randint so no need of this: # from random import randint
from gif_export_wrapper import gif_export
from my_box import my_box
add_library('gifAnimation')
add_library('peasycam')
add_library('dxf')
add_library('OBJExport')

GRID_SIZE = 32
OUTPUT = ".gif"
# Cutting-plane position (press + & - to change)
cut_plane = GRID_SIZE
export = False

def setup():
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    size(700, 700, P3D)
    colorMode(HSB)
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
    # crear objects
    create_rods()
    #create_tubes()

def draw():
    # lights()
    background(200)
    if export:
        beginRaw("nervoussystem.obj.OBJExport", "filename.obj")

    for node in Node.nodes:
        if node.iz < cut_plane:
            node.plot()

    if export:
        endRaw()
        global export
        export = False


   

def keyPressed():
    """ press P to save an image """
    if key in ['p', 'P']:
        saveFrame("####" + SKETCH_NAME + OUTPUT)
    if key == " ":
        for node in Node.nodes:
            node.cor = None
        create_rods()
        create_tubes()
    if key == "g":
        gif_export(GifMaker, delay=2000, filename=SKETCH_NAME)
    if key == "f":
        gif_export(GifMaker, finish=True)
    # cut plane adjust
    global cut_plane, export
    if key == "-":
        cut_plane -= 1
        print(cut_plane)
    if key in ['+', '=']:
        cut_plane += 1
        print(cut_plane)
    if key == 'e':
        export = True


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

def big_ugly(px, py, pz, w, h=None, d=None, c=255):
    h = h if h else w
    d = d if d else w
    for z in range(pz, pz + d):
        for y in range(py, py + h):
            for x in range(px, px + w):
                if (0 <= x < GRID_SIZE and
                        0 <= y < GRID_SIZE and
                        0 <= z < GRID_SIZE):
                        orient1 =  x % 2 and y % 2
                        orient2 = x % 2 and z % 2
                        orient3 = y % 2 and z % 2
                        if orient1 or orient2 or orient3:
                        Node.grid[(x, y, z)].cor = c
                else:
                    Node.grid[(x, y, z)].cor = None
                


def create_tubes():
    # sets the objects, list of tuples -> hollowed boxes
    seed = int(random(1000)) #seed = 205
    println("seed: {}".format(seed))
    randomSeed(seed)
    m = GRID_SIZE - 1
    tube_list = []
    num_tubes = 10
    border = 1
    for i in range(num_tubes):
        # random size in range 3 to GRID_SIZE - borders
        w = randint(3, m - border * 2)
        h = randint(3, m - border * 2)
        d = randint(3, m - border * 2)
        # random position
        x = randint(border, m - w - border)
        y = randint(border, m - h - border)
        z = randint(border, m - d - border)
        box_tuple = (x, y, z, w, h, d)
        print(box_tuple)
        tube_list.append(box_tuple)
    # solid boxes 
    for i in range(num_tubes):
        x, y, z, w, h, d = tube_list[i]
        big_box(x, y, z, w, h, d,
                color(64 + (i % 3) * 32, 200, 200))
    # erase inside boxes, making tubes
    for i in range(num_tubes):
        x, y, z, w, h, d = tube_list[i]
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
                # use color(0) below, instead of None to debug
                # color(0))
                None)

def create_rods():
    # sets the objects, list of tuples -> hollowed boxes
    seed = int(random(1000))  # seed = 205
    println("seed: {}".format(seed))
    randomSeed(seed)
    m = GRID_SIZE - 1
    box_list = []
    num_boxes = 10
    border = 1
    for i in range(num_boxes):
        # random size in range 3 to GRID_SIZE - borders
        w = randint(3, m - border * 2)
        h = randint(3, m - border * 2)
        d = randint(3, m - border * 2)
        # random position
        x = randint(border, m - w - border)
        y = randint(border, m - h - border)
        z = randint(border, m - d - border)
        box_tuple = (x, y, z, w, h, d)
        # print(box_tuple)
        box_list.append(box_tuple)
    # solid boxes
    for i in range(num_boxes):
        x, y, z, w, h, d = box_list[i]
        big_ugly(x, y, z, w, h, d, color(128 + (i % 3) * 32, 200, 200))
        
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
            #stroke(0, 200)
            stroke(0)
            fill(self.cor)
            with pushMatrix():
                translate(self.x, self.y, self.z)
                my_box(Node.spacing * self.size_)

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
