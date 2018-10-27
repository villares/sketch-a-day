# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s301"  # 20181026
OUTPUT = ".png"
GRID_SIZE = 24

from line_geometry import edges
from line_geometry import Line
from line_geometry import inter_lines

def setup():
    global xo, yo
    size(500, 500)
    init_grid(GRID_SIZE)

def draw():
    background(200)
    for c in Cell.cells:
        c.plot()

def init_grid(grid_size):
    Cell.border = 50
    Cell.spacing = (width - Cell.border * 2) / grid_size
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
                #Cell.cells.append(new_node)  # mudar!
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
        # if x/2 % 3: self.px += random(-10, 10)
        # if y/2 % 3: self.py += random(-10, 10)
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
        self.px = Cell.border + Cell.spacing / 2 + x * Cell.spacing 
        self.py = Cell.border + Cell.spacing / 2 + y * Cell.spacing 
        self.vers = []        
      
    def plot(self):
        stroke(0)
        strokeWeight(1)
        for l in self.lines:
            l.plot()
        beginShape()
        noFill()
        stroke(0)
        strokeWeight(2)
        for p in self.vers:
            vertex(p.x, p.y)
        endShape(CLOSE)
        
    def update_vers(self):
        self.v0 = Cell.grid.get((self.ix-1, self.iy-1))
        self.v1 = Cell.grid.get((self.ix-1, self.iy+1))
        self.v3 = Cell.grid.get((self.ix+1, self.iy-1))
        self.v2 = Cell.grid.get((self.ix+1, self.iy+1))
        if random(10) > 2:
            self.vers = [self.v0, self.v1, self.v2, self.v3]
        elif random(2) > 1:
            self.vers = [self.v0, self.v1, self.v1, self.v3]
        else:
             self.vers = [self.v0, self.v2, self.v2, self.v3]
        self.hatch()
        
    def hatch(self):
        poly_points = self.vers
        # min_, max_ = min_max(poly_points)
        self.lines = []
        s = int(random(3, 7))
        r = random(10)
        if r > 5:            
            for y in range(-height, height*2, s):        
                a = PVector(-width, y - self.v0.y/2.)
                b = PVector(width*2, y + self.v0.y/3.)
                lines = inter_lines(Line(a, b), poly_points)
                for l in lines:
                    self.lines.append(l)          
        if r < 6:
            for x in range(-width, width*2, s):        
                a = PVector(x + self.v2.x/2., -height)
                b = PVector(x - self.v2.x/3., height*2,)
                lines = inter_lines(Line(a, b), poly_points)
                for l in lines:
                    self.lines.append(l)          
                        
def keyPressed():
    if key == "n":
        init_grid(GRID_SIZE)
    if key == "s": saveFrame("###.png")

# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
