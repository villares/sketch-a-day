# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s304"  # 20181029
OUTPUT = ".png"
GRID_SIZE = 24

from line_geometry import Line
from line_geometry import par_hatch

rule = lambda x, y: (x - y) % 3 == 0

def setup():
    global xo, yo
    size(500, 500)
    smooth(8)
    init_grid(GRID_SIZE)
    
def draw():
    background(0)
    stroke(255)
    for c in Cell.cells:
        c.plot()
    
    for p in Node.nodes:
        if rule(p.ix, p.iy):
            if dist(p.x, p.y, mouseX, mouseY) < 5:
                stroke(255, 0, 0)
            else:
                stroke(255)        
            ellipse(p.x, p.y, 10, 10)    
    

def init_grid(grid_size):
    Cell.border = 50.
    Cell.spacing = (width - Cell.border *2) / grid_size
    Cell.cells = []

    for x in range(0, grid_size, 2):
        for y in range(0, grid_size, 2):
                new_cell = Cell(x, y)
                Cell.cells.append(new_cell)
                Cell.grid[x, y] = new_cell

    Node.nodes = []
    for x in range(-1, grid_size+1, 2):
        for y in range(-1, grid_size+1, 2):
                new_node = Node(x, y)
                Node.nodes.append(new_node) 
                Cell.grid[x, y] = new_node   # extrarir do dict

    for c in Cell.cells:
        c.update_vers()
   
class Node():
    nodes = []
    grid = dict()

    def __init__(self, x, y):
        self.ix = x
        self.iy = y
        self.px = Cell.border + Cell.spacing + x * Cell.spacing 
        self.py = Cell.border + Cell.spacing + y * Cell.spacing 
        if rule(x, y):
           self.px += random(-10, 10)
           self.py += random(-10, 10)
        self.x = self.px
        self.y = self.py
        self.v = PVector(self.x, self.y)

class Cell():
    cells = []
    grid = dict()
    vers = []

    def __init__(self, x, y):
        self.ix = x
        self.iy = y
        self.px = Cell.border + Cell.spacing  + x * Cell.spacing 
        self.py = Cell.border + Cell.spacing  + y * Cell.spacing 
        self.vers = []
        self.num_hatches = int(random(5, 12))
        self.type_hatches = random(10)       
      
    def plot(self):
        self.hatch()
        strokeWeight(1)
        for l in self.lines:
            l.plot()
        beginShape()
        noFill()
        strokeWeight(2)
        for p in self.vers:
            vertex(p.v.x, p.v.y)
        endShape(CLOSE)
        
    def update_vers(self):
        self.v0 = Cell.grid.get((self.ix-1, self.iy-1))
        self.v1 = Cell.grid.get((self.ix-1, self.iy+1))
        self.v3 = Cell.grid.get((self.ix+1, self.iy-1))
        self.v2 = Cell.grid.get((self.ix+1, self.iy+1))
        # if random(10) > 2:
        self.vers = [self.v0, self.v1, self.v2, self.v3]
        
    def hatch(self):
        self.lines = []
        n = self.num_hatches
        r = self.type_hatches
        if r > 5:                        
            self.lines.extend(par_hatch(self.vers, n, 0))
        if r < 6:
            self.lines.extend(par_hatch(self.vers, n, 1))
        
def keyPressed():
    if key == "n":
        init_grid(GRID_SIZE)
    if key == "s": saveFrame("###.png")
    
def mouseDragged():
    for p in Node.nodes:
        if rule(p.ix, p.iy):
            if dist(p.x, p.y, mouseX, mouseY) < 5:
                p.x, p.y = mouseX, mouseY
                p.v = PVector(p.x, p.y)
                
# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
