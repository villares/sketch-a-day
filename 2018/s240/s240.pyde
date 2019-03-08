# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s240"  # 20180826
OUTPUT = ".gif"

from gif_export_wrapper import gif_export
from my_box import my_box
add_library('gifAnimation')
add_library('peasycam')
add_library('dxf')
add_library('OBJExport')

GRID_SIZE = 48

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
    # create objects
    create_frames()

def draw():
    global export
    rotateY(-QUARTER_PI)
    lights()
    background(100)
    # if export:
    #     beginRaw("nervoussystem.obj.OBJExport", "filename.obj")

    ang = frameCount  / 30.
    steps = abs(sin(ang))
    deploy_frames(steps)

    for node in Node.nodes:
        if node.iz < cut_plane:
            node.plot()
    if ang < TWO_PI:
        gif_export(GifMaker, delay=100, filename=SKETCH_NAME)
    else:
        gif_export(GifMaker, finish=True)
        
    # if export:
    #     endRaw()
    #     export = False



def keyPressed():
    """ press P to save an image """
    if key in ['p', 'P']:
        saveFrame("####" + SKETCH_NAME + OUTPUT)
    if key == " ":
        create_frames()
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
    if key == "z":
       deploy_frames(map(mouseX, 1, width, 0, 1))


def cube_frame(px, py, pz, w, h=None, d=None, c=255):
    h = h if h else w
    d = d if d else w
    for z in range(pz, pz + d + 1):
        for y in range(py, py + h + 1):
            for x in range(px, px + w + 1):
                if (0 <= x < GRID_SIZE and
                        0 <= y < GRID_SIZE and
                        0 <= z < GRID_SIZE):
                    if ((x == px and y == py) or
                            (x == px + w and y == py + h) or
                            (x == px + w and y == py) or
                            (x == px and y == py) or
                            (x == px and y == py + h) or
                            (y == py + h and z == pz) or
                            (y == py + h and z == pz + d) or
                            (y == py and z == pz) or
                            (y == py and z == pz + d) or
                            (z == pz and x == px) or
                            (z == pz + d and x == px) or
                            (z == pz and x == px + w) or
                            (z == pz + d and x == px + w)
                            ):
                        Node.grid[(x, y, z)].cor = c
                    else:
                        pass
                        #Node.grid[(x, y, z)].cor = None

def create_frame_list(num_boxes):
    # sets the objects, list of tuples -> hollowed boxes
    seed = int(random(1000))  # seed = 205
    println("seed: {}".format(seed))
    randomSeed(seed)
    m = GRID_SIZE - 1
    frame_list = []
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
        frame_list.append(box_tuple)    
    return frame_list

def create_frames():
    Node.num_boxes = 9
    Node.frames1 = create_frame_list(Node.num_boxes)
    Node.frames2 = create_frame_list(Node.num_boxes)

def deploy_frames(step):
    for node in Node.nodes:
        node.cor = None
    for i in range(Node.num_boxes):
        tuple = (int(lerp(a, b, step)) for a, b in zip(Node.frames1[i], Node.frames2[i]))
        x, y, z, w, h, d = tuple
        cube_frame(x, y, z, w, h, d, color(64 + (i % 3) * 32, 200, 200))

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
            # stroke(0, 200)
            noStroke() #stroke(0)
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
