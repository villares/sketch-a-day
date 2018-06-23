# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
from random import choice
from gif_export_wrapper import *
add_library('gifAnimation')

GRID_SIZE = 40
SKETCH_NAME = "s175"
OUTPUT = ".gif"

def setup():
    size(500, 500)
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    border = 25
    spacing = (width - border * 2) / GRID_SIZE
    Node.spacing = spacing
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            Node.nodes.append(Node(border + spacing / 2 + x * spacing,
                                   border + spacing / 2 + y * spacing))
    for node in Node.nodes:
        node.set_nbs()

    Node.nodes[0].current = True

def draw():

    background(100)
    for node in Node.nodes:
        node.plot_links()
        node.update()

    if frameCount % 2:
        gif_export(GifMaker, filename=SKETCH_NAME)

class Node():
    nodes = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.current = False
        self.links = []

    def plot_links(self):
        for node in self.links:
            stroke(255)
            strokeWeight(5)
            line(node.x, node.y, self.x, self.y)

    def set_nbs(self):
        self.nbs, self.unvisited_nbs = [], []
        for node in Node.nodes:
            if node != self and dist(node.x, node.y,
                                     self.x, self.y) <= Node.spacing:
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
                rnd_choice = choice(self.unvisited_nbs)
                self.links.append(rnd_choice)
                self.current = False
                rnd_choice.current = True
                rnd_choice.visited = True
            else:
                branch_nodes = [node for node in Node.nodes
                                if node.visited and node.unvisited_nbs]
                if branch_nodes:
                    print(len(branch_nodes))
                    rnd_choice = choice(branch_nodes)
                    self.current = False
                    rnd_choice.current = True
                else:
                    print("finished")
                    gif_export(GifMaker, finish=True)


def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
