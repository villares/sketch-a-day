# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# s215 20180801

from gif_export_wrapper import *
add_library('gifAnimation')
add_library('peasycam')

GRID_SIZE = 15
SKETCH_NAME = "s215"
OUTPUT = ".gif"

def setup():
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    size(700, 700, P3D)
    #hint(ENABLE_DEPTH_SORT)
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
                Node.nodes.append(Node(x, y, z))


        
def draw():
    lights()
    # arbitray rotation
    rotate(-1, 1/2, 1, 1/2)
    background(100)
    # angle based on frameCount to animate box sizes
    ang = frameCount/10.
    
    # Node.rooms is a list of spaced nodes inside the grid
    s = 1 + (frameCount % GRID_SIZE)
    Node.rooms = set([node for node in Node.nodes
                  if node.ix % s == 0 and
                     node.iy % s == 0 and
                     node.iz % s == 0])
    for node in Node.nodes:
        if node in Node.rooms:
            node.cor = color(0, 128, 255)
        else:
            node.cor = None
    for node in Node.nodes:
            node.plot()
            #node.update(ang)
            
    # stop after a full size animatiom cycle
    if frameCount < 16:
        gif_export(GifMaker, filename=SKETCH_NAME)
    else:
        gif_export(GifMaker, finish=True)
    

class Node():
    nodes = []
    rooms = []

    def __init__(self, x, y, z):
        self.ix = x
        self.iy = y
        self.iz = z
        self.x = Node.border + Node.spacing / 2 + x * Node.spacing - width / 2
        self.y = Node.border + Node.spacing / 2 + y * Node.spacing - width / 2
        self.z = Node.border + Node.spacing / 2 + z * Node.spacing - width / 2
        self.size_ = 1 
        self.cor = None
        self.update(0)

    def plot(self):
        """ draws box """
        if self.cor:
            stroke(0)
            fill(self.cor)
        else:
            stroke(255, 10)
            noFill()
        with pushMatrix():
                translate(self.x, self.y, self.z)
                box(Node.spacing * self.size_)

    def update(self, ang):
        """ changing box size """
        if self.cor == None:
            self.size_ = 1
        else:
            self.size_ = cos(ang) #self.x + self.y + self.z + ang)


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
