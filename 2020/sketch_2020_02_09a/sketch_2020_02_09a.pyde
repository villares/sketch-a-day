# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

SKETCH_NAME = "s09a"
OUTPUT = ".pdf"
GRID_SIZE = 30
MARGIN = .1
n = 1  # seed 0 -> n-1
scaleFactor = 8

from line_geometry import Line
from line_geometry import par_hatch
add_library('pdf')

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
    # beginRecord(hires)
    # hires.background(240)
    # hires.strokeWeight(.33)
    # hires.scale(scaleFactor)
    for c in Cell.cells:
        c.plot()

    # hires.dispose()
    # endRecord()
    # hires.save("{}-highres".format(s) + OUTPUT)

def keyPressed():
    if key == ' ':
        init_grid(GRID_SIZE)
    if key == 's':
        saveFrame("###.png")
    if key == 'r':
        for c in Cell.cells:
            if random(10) < 1:
                c.update()


def mousePressed():
    for c in Cell.cells:
        if dist(c.px, c.py, mouseX, mouseY) < Cell.spacing:
            c.update()

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
            Node.grid[x, y] = Node(x, y)   # extrarir do dict
            # Node.grid1[x, y] = Node(x, y)   # extrarir do dict
    for c in Cell.cells:
        c.set_vers()

class Node():
    grid = dict()

    def __init__(self, x, y):
        self.ix = x
        self.iy = y
        self.px = Cell.border + Cell.spacing + x * Cell.spacing
        self.py = Cell.border + Cell.spacing + y * Cell.spacing
        # if random(20) > 10:
        #     mx, my = width / 2, height / 2
        #     self.px -= (self.px - mx) * 0.15
        #     self.py -= (self.py - my) * 0.15
        self.x = self.px
        self.y = self.py

class Cell():
    cells = []

    def __init__(self, x, y):
        self.ix = x
        self.iy = y
        self.px = Cell.border + Cell.spacing + x * Cell.spacing
        self.py = Cell.border + Cell.spacing + y * Cell.spacing
        self.vers = []
        self.can_change = True

    def plot(self, t=0):
        if dist(self.px, self.py, mouseX, mouseY) < Cell.spacing:
            fill(255, 100)
        else:
            fill(200, 100)
        beginShape()
        # stroke(255, 0, 0)
        for p in self.vers:
            vertex(p.x, p.y)
        endShape(CLOSE)

    def update(self):
        Cell.cells.remove(self)
        if self.can_change:
            self.can_change = False
            r = random(100)
            y01 = (self.v0.y + self.v1.y) / 2
            y23 = (self.v2.y + self.v3.y) / 2
            x12 = (self.v1.x + self.v2.x) / 2
            x30 = (self.v3.x + self.v0.x) / 2
            if r < 33:
                self.v0.y = y01  # -1-1
                self.v1.y = y01  # -1+1
                self.v2.y = y23  # +1-1
                self.v3.y = y23  # +1+1
            elif r < 66:
                self.v0.x = x30  # -1-1
                self.v1.x = x12  # -1+1
                self.v2.x = x12  # +1-1
                self.v3.x = x30  # +1+1
            else:
                self.v0.y, self.v0.x = y01, x30
                self.v1.y, self.v1.x = y01, x12
                self.v2.y, self.v2.x = y23, x12
                self.v3.y, self.v3.x = y23, x30

            # self.v3.x, self.v3.y = self.px, self.py
            # mx, my = width / 2, height / 2
            # for v in self.vers:
            #     v.x -= (v.x - mx) * 0.15
            #     v.y += (v.y - my) * 0.15
            # self.v1 = self.v2 = self.v0

    def set_vers(self):
        self.v0 = Node.grid.get((self.ix - 1, self.iy - 1))
        self.v1 = Node.grid.get((self.ix - 1, self.iy + 1))
        self.v3 = Node.grid.get((self.ix + 1, self.iy - 1))
        self.v2 = Node.grid.get((self.ix + 1, self.iy + 1))
        self.vers = [self.v0, self.v1, self.v2, self.v3]
