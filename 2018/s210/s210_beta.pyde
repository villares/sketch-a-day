# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# s210 20180727

from gif_export_wrapper import *
add_library('gifAnimation')
add_library('peasycam')

GRID_SIZE = 11
SKETCH_NAME = "s210"
OUTPUT = ".png"
color_mode = True
starting_node = 0
end_cycle = False

def setup():
    size(700, 700, P3D)
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(1000)
    cam.setMaximumDistance(1000)
    # colorMode(HSB)
    strokeWeight(2)
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    Node.border = 50
    Node.spacing = (width - Node.border * 2) / GRID_SIZE
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            for z in range(GRID_SIZE):
                Node.nodes.append(Node(x, y, z))
    Node.rooms = [node for node in Node.nodes
                  if node.ix % 2 == 1 and
                  node.iy % 2 == 1 and
                  node.iz % 2 == 1]
    for node in Node.rooms:
        node.set_nbs()
        node.cor = color(0, 0, 255)

    clear_grid()

def draw():
    lights()
    background(200)

    for node in Node.nodes:
        if node.iz - 1 < frameCount / 10 % GRID_SIZE:
            node.plot()

    # gif_export(GifMaker)

    # if end_cycle == True:
    #     gif_export(GifMaker)
    #     clear_grid()
    #     global end_cycle
    #     end_cycle = False

def clear_grid():
    global starting_node, end_cycle
    starting_node += 1
    Node.corridors = []
    if starting_node < len(Node.rooms):
        for node in Node.rooms:
            node.visited = False
            node.current = False
            node.links = []
        Node.rooms[starting_node].current = True
    # else:
    #     gif_export(GifMaker, finish=True)
    #     noLoop()

    while not end_cycle:
        for node in Node.rooms:
            node.update()

class Node():
    nodes = []
    rooms = []
    corridors = []

    def __init__(self, x, y, z):
        self.ix = x
        self.iy = y
        self.iz = z
        self.x = Node.border + Node.spacing / 2 + x * Node.spacing - width / 2
        self.y = Node.border + Node.spacing / 2 + y * Node.spacing - width / 2
        self.z = Node.border + Node.spacing / 2 + z * Node.spacing - width / 2
        self.visited = False
        self.current = False
        self.links = []
        self.cor = None
        self.nbs = []
        self.rnbs = []

    def plot(self):
        if self.cor:
            fill(self.cor)
        else:
            if color_mode:
                fill(255, 50)
            else:
                fill(128)
        if color_mode or self not in Node.corridors:
            with pushMatrix():
                translate(self.x, self.y, self.z)
                box(Node.spacing)

    def set_nbs(self):
        self.nbs, self.unvisited_rnbs = [], []
        for node in Node.nodes:
            if node != self and dist(node.x, node.y, node.z,
                                     self.x, self.y, self.z) <= Node.spacing * 1:
                self.nbs.append(node)
        if self in Node.rooms:
            for node in Node.rooms:
                if node != self and dist(node.x, node.y, node.z,
                                         self.x, self.y, self.z) <= Node.spacing * 2:
                    self.rnbs.append(node)
                    self.unvisited_rnbs.append(node)
                # if (self.ix == node.ix - 1 or
                #         self.ix == node.ix + 1 or
                #         self.iy == node.iy - 1 or
                #         self.iy == node.iy + 1):

    def set_unvisited_rnbs(self):
        self.unvisited_rnbs = [node for node in self.rnbs
                               if not node.visited]

    def find_corridor(self, other):
        for n1 in self.nbs:
            for n2 in other.nbs:
                if n1 == n2:
                    return n1

    def update(self):
        self.set_unvisited_rnbs()
        if self.current:
            self.visited = True
            Node.corridors.append(self)
            if self.unvisited_rnbs:
                for unvisited_rnb in self.unvisited_rnbs[::-2]:
                    corridor = self.find_corridor(unvisited_rnb)
                    Node.corridors.append(corridor)
                    corridor.cor = color(0, 255, 0)
                    self.current = False
                    unvisited_rnb.visited = True
                    unvisited_rnb.current = True

            else:
                branch_nodes = [node for node in Node.nodes
                                if node.visited and node.unvisited_rnbs]
                if branch_nodes:
                    print(len(branch_nodes))
                    next = branch_nodes[-1]
                    self.current = False
                    next.current = True
                else:
                    print("finished")
                    global end_cycle
                    end_cycle = True
                    # noLoop()

def keyPressed():
    loop()
    global color_mode
    if key == 'c':
        color_mode = not color_mode
    if key in ['p', 'P']:
        saveFrame("####" + SKETCH_NAME + OUTPUT)
    if key == 's':
        gif_export(GifMaker, finish=True)
    # if key == 'g':
    #     gif_export(GifMaker)
    if key == 'r':
        clear_grid()
    # if key in ['=', '+']:
    #     global starting_node
    #     starting_node += 1


def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
