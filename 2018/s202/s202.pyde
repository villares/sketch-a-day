# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# s202 20180719 (picking up from s180 20180627)

from gif_export_wrapper import *
add_library('gifAnimation')
add_library('peasycam')
GRID_SIZE = 20
SKETCH_NAME = "s202"
OUTPUT = ".png"
color_mode = True

def setup():
    lights()
    size(700, 700, P3D)
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(100)
    cam.setMaximumDistance(1000)
    colorMode(HSB)
    noStroke()
    # strokeWeight(4)
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    border = 50
    spacing = (width - border * 2) / GRID_SIZE
    Node.spacing = spacing
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            for z in range(GRID_SIZE):
                Node.nodes.append(Node(
                    border + spacing / 2 + x * spacing - width / 2,
                    border + spacing / 2 + y * spacing - width / 2,
                    border + spacing / 2 + z * spacing - width / 2))
    for node in Node.nodes:
        node.set_nbs()

    Node.nodes[500].current = True
    #Node.nodes[int(len(Node.nodes)/7)].current = True

def draw():
    lights()
    background(0)
    for node in Node.nodes:
        node.plot_links()
        node.update()

class Node():
    nodes = []

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.visited = False
        self.current = False
        self.links = []
        self.cor = 0

    def plot_links(self):
        if color_mode:
            stroke(0)
            fill(color(self.cor % 256, 255, 255))
        else:
            stroke(200)
            fill(200)
        with pushMatrix():
            translate(self.x, self.y, self.z)
            box(Node.spacing / 2)
        for node in self.links:
            mid_x = (self.x + node.x) / 2
            mid_y = (self.y + node.y) / 2
            mid_z = (self.z + node.z) / 2
            with pushMatrix():
                translate(mid_x, mid_y, mid_z)
                box(Node.spacing / 2)


    def set_nbs(self):
        self.nbs, self.unvisited_nbs = [], []
        for node in Node.nodes:
            if node != self and dist(node.x, node.y, node.z,
                                     self.x, self.y, self.z) <= Node.spacing * 1.1:
                self.nbs.append(node)
                self.unvisited_nbs.append(node)

    def set_unvisited_nbs(self):
        self.unvisited_nbs = [node for node in self.nbs
                              if not node.visited]

    def update(self):
        self.set_unvisited_nbs()
        if self.current:
            self.visited = True
            if self.unvisited_nbs:
                for unvisited_nb in self.unvisited_nbs[::2]:
                    self.links.append(unvisited_nb)
                    self.current = False
                    unvisited_nb.current = True
                    unvisited_nb.visited = True
                    unvisited_nb.cor = self.cor + 10
            else:
                branch_nodes = [node for node in Node.nodes
                                if node.visited and node.unvisited_nbs]
                if branch_nodes:
                    print(len(branch_nodes))
                    next = branch_nodes[-1]  
                    self.current = False
                    next.current = True
                else:
                    print("finished")
                    # noLoop()

def keyPressed():
    global color_mode
    if key == 'c':
        color_mode = not color_mode
    if key in ['s', 'S']:
        saveFrame("####" + SKETCH_NAME + OUTPUT)
        
        

def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
