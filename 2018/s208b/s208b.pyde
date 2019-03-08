# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# s208 20180725

from gif_export_wrapper import *
add_library('gifAnimation')
add_library('peasycam')

GRID_SIZE = 11
SKETCH_NAME = "s208b"
OUTPUT = ".png"
color_mode = True
starting_node = 0
end_cycle = False

def setup():
    lights()
    size(700, 700, P3D)
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(1000)
    cam.setMaximumDistance(1000)
    #colorMode(HSB)
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
                     node.iz % 2 == 1 ]            
    for node in Node.rooms:
        node.set_nbs()
        node.cor = color(0, 0, 255)

    clear_grid()


def draw():
    # lights()
    background(0)
    for node in Node.rooms:
        pass #node.plot_links()
    for node in Node.nodes:
        node.plot()
        
    # for node in Node.rooms:
    #     node.update()

    # gif_export(GifMaker)

    if end_cycle == True:
        gif_export(GifMaker)
        gif_export(GifMaker)
        clear_grid()
        global end_cycle
        end_cycle = False

def clear_grid():
    global starting_node
    starting_node += 1

    if starting_node < len(Node.nodes):
        for node in Node.nodes:
            node.visited = False
            node.current = False
            node.links = []
        Node.nodes[starting_node].current = True
    else:
        gif_export(GifMaker, finish=True)
        noLoop()


class Node():
    nodes = []

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
        self.cor = color(255)
        self.nbs = []

    def plot(self):

        fill(self.cor)
        
        with pushMatrix():
                    translate(self.x, self.y, self.z)
                    box(Node.spacing / 2)
                    
    def plot_links(self):
        for node in self.nbs:
            if node not in self.links:
                mid_x = (self.x + node.x) / 2
                mid_y = (self.y + node.y) / 2
                mid_z = (self.z + node.z) / 2
                with pushMatrix():
                    translate(mid_x, mid_y, mid_z)
                    box(Node.spacing / 3)

    def set_nbs(self):
        self.nbs, self.unvisited_nbs = [], []
        for node in Node.nodes:
            if node != self and dist(node.x, node.y, node.z,
                                     self.x, self.y, self.z) <= Node.spacing * 1:
            # if (self.ix == node.ix - 1 or
            #         self.ix == node.ix + 1 or
            #         self.iy == node.iy - 1 or
            #         self.iy == node.iy + 1):
                node.cor = color(255, 0, 0)
                self.nbs.append(node)
                self.unvisited_nbs.append(node)

    def set_unvisited_nbs(self):
        self.unvisited_nbs = [node for node in self.nbs
                              if not node.visited]

    def update(self):
        self.set_unvisited_nbs()
        if self.current:
            self.visited = True
            if not self.cor:
                self.cor = 0
            if self.unvisited_nbs:
                for unvisited_nb in self.unvisited_nbs[::-2]:
                    self.links.append(unvisited_nb)
                    unvisited_nb.links.append(self)
                    self.current = False
                    unvisited_nb.visited = True
                    unvisited_nb.current = True
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
                    global end_cycle
                    end_cycle = True
                    noLoop()

def keyPressed():
    global color_mode
    if key == 'c':
        color_mode = not color_mode
    if key in ['p', 'P']:
        saveFrame("####" + SKETCH_NAME + OUTPUT)
    loop()
    # if key == 's':
    #     gif_export(GifMaker, finish=True)
    # if key == 'g':
    #     gif_export(GifMaker)
    # if key == 'r':
    #     clear_grid()
    # if key in ['=', '+']:
    #     global starting_node
    #     starting_node += 1


def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
