# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

SKETCH_NAME = "s06a"  
OUTPUT = ".pdf"
GRID_SIZE = 14
MARGIN = .1
n = 1  # seed 0 -> n-1
scaleFactor = 8

from line_geometry import Line
from line_geometry import par_hatch
add_library('pdf')

rule = lambda x, y: random(40) < 20


def setup():
    global hires, s
    size(600, 600)
    smooth(8)
    randomSeed(1)
    init_grid(GRID_SIZE)    
    s = 1

def draw():
    # for s in range(1):
        background(100)
        hires = createGraphics(
            width * scaleFactor,
            height * scaleFactor,
            PDF, "{}-highres.pdf".format(s))
        beginRecord(hires)
        hires.background(240)
        hires.strokeWeight(.33)
        hires.scale(scaleFactor)
        for c in Cell.cells:
            c.plot() 
                
        hires.dispose()
        endRecord()
        # hires.save("{}-highres".format(s) + OUTPUT)
    
def init_grid(grid_size):
    Cell.border = width * MARGIN
    Cell.spacing = (width - Cell.border * 2) / grid_size
    Cell.cells = []
    for x in range(0, grid_size, 2):
        for y in range(0, grid_size, 2):
            new_cell = Cell(x, y)
            Cell.cells.append(new_cell)
            # Cell.grid[x, y] = new_cell

    # randomSeed(frameCount+2)
    for x in range(-1, grid_size + 1, 2):
        for y in range(-1, grid_size + 1, 2):
            Node.grid0[x, y] = Node(x, y)   # extrarir do dict
            # Node.grid1[x, y] = Node(x, y)   # extrarir do dict
    for c in Cell.cells:
        c.update_vers()

class Node():
    grid0 = dict()
    # grid1 = dict()

    def __init__(self, x, y):
        self.ix = x
        self.iy = y
        self.px = Cell.border + Cell.spacing + x * Cell.spacing
        self.py = Cell.border + Cell.spacing + y * Cell.spacing
        # if rule(x, y):
        #     mx, my = width / 2, height / 2
        #     self.px += (self.px - mx) * 0.15
        #     self.py += (self.py - my) * 0.15
        self.x = self.px
        self.y = self.py

class Cell():
    cells = []
    # grid = dict()

    def __init__(self, x, y):
        self.ix = x
        self.iy = y
        self.px = Cell.border + Cell.spacing + x * Cell.spacing
        self.py = Cell.border + Cell.spacing + y * Cell.spacing
        self.vers = []
        self.num_hatches = int(random(5, 12))
        self.type_hatches = random(10)

    def plot(self, t=0):
        if dist(self.px, self.py, mouseX, mouseY) < Cell.spacing:
            fill(255)
            if mousePressed:
                self.remover()
        else:
            fill(200)        
        beginShape()
        # stroke(255, 0, 0)
        for p in self.vers:
            vertex(p.x, p.y)
        endShape(CLOSE)

    def remover(self):
        # Node.grid0.get((self.ix, self.iy)) = None
        Cell.cells.remove(self)
        self.v0.x, self.v0.y = self.px, self.py
        self.v3.x, self.v3.y = self.px, self.py
        # self.v1 = Node.grid0.get((self.ix - 1, self.iy + 1))
        # self.v3 = Node.grid0.get((self.ix + 1, self.iy - 1))
        # self.v2 = Node.grid0.get((self.ix + 1, self.iy + 1))
        
    def update_vers(self):
        self.v0 = Node.grid0.get((self.ix - 1, self.iy - 1))
        self.v1 = Node.grid0.get((self.ix - 1, self.iy + 1))
        self.v3 = Node.grid0.get((self.ix + 1, self.iy - 1))
        self.v2 = Node.grid0.get((self.ix + 1, self.iy + 1))
        self.vers = [self.v0, self.v1, self.v2, self.v3]
  
