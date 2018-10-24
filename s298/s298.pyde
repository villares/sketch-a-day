# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s298"  # 20181023
OUTPUT = ".png"
GRID_SIZE = 16

from line_geometry import edges
from line_geometry import Line
from line_geometry import inter_lines

def setup():
    global xo, yo
    size(500, 500)
    init_grid(GRID_SIZE)

def draw():
    noLoop()
    background(200)
    for c in Cell.cells:
        c.draw_vers()
        c.hatch()

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
        self.px = Cell.border + Cell.spacing / 2 + x * Cell.spacing 
        self.py = Cell.border + Cell.spacing / 2 + y * Cell.spacing 
        self.px += random(-10, 10)
        self.py += random(-10, 10)
        self.x = self.px
        self.y = self.py

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
      
    def draw_vers(self):
        if len(self.vers) > 1:
            for n0, n1 in edges(self.vers):
                line(n0.px, n0.py, n1.px, n1.py)
        for l in self.lines:
            l.plot()

    def update_vers(self):
        v0 = Cell.grid.get((self.ix-1, self.iy-1))
        v1 = Cell.grid.get((self.ix-1, self.iy+1))
        v3 = Cell.grid.get((self.ix+1, self.iy-1))
        v2 = Cell.grid.get((self.ix+1, self.iy+1))
        self.vers = [v for v in [v0, v1, v2, v3] if v]
        self.hatch()
        
    def hatch(self):
        poly_points = self.vers
        # min_, max_ = min_max(poly_points)
        if random(10) > 5:            
            for y in range(-height, height*2, int(random(2, 7))):        
                a = PVector(-width, y)
                b = PVector(width*2, y)
                lines = inter_lines(Line(a, b), poly_points)
                if lines: self.lines.append(lines)        
        else:
            for x in range(-width, width*2, int(random(2, 7))):        
                a = PVector(x, -height)
                b = PVector(x, height*2,)
                lines = inter_lines(Line(a, b), poly_points)
                if lines: self.lines.append(lines)        
                        
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
