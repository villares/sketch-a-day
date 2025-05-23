# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s308"  # 20181102
OUTPUT = ".gif"
GRID_SIZE = 24

from line_geometry import Line
from line_geometry import par_hatch

U, V = 3, 3
rule = lambda x, y: (x - y) % U == 0 and (x + y) % V

def setup():
    global xo, yo
    size(500, 500)
    smooth(8)
    init_grid(GRID_SIZE)
    
def draw():
    global rule
    rule = lambda x, y: (x - y) % U == 0 and (x + y) % V
    background(200)
    stroke(0)
    for c in Cell.cells:
        c.plot()

def init_grid(grid_size):
    Cell.border = 50.
    Cell.spacing = (width - Cell.border *2) / grid_size
    Cell.cells = []

    for x in range(0, grid_size, 2):
        for y in range(0, grid_size, 2):
                new_cell = Cell(x, y)
                Cell.cells.append(new_cell)
                Cell.grid[x, y] = new_cell

    for x in range(-1, grid_size+1, 2):
        for y in range(-1, grid_size+1, 2):
                new_node = Node(x, y)
                Cell.grid[x, y] = new_node   # extrarir do dict

    for c in Cell.cells:
        c.update_vers()
   
class Node():

    def __init__(self, x, y):
        self.ix = x
        self.iy = y
        self.px = Cell.border + Cell.spacing + x * Cell.spacing 
        self.py = Cell.border + Cell.spacing + y * Cell.spacing 
        if rule(x, y):
           mx, my = width/2, height/2
           qx = 1.5 * (self.px - mx) / (abs(self.px - mx) + 0.001)
           qy = 1.5 * (self.py - my) / (abs(self.py - my) + 0.001)
           self.px += sqrt(abs(self.px - mx)) * qx
           self.py += sqrt(abs(self.py - my)) * qy
        self.x = self.px
        self.y = self.py

class Cell():
    cells = []
    grid = dict()

    def __init__(self, x, y):
        self.ix = x
        self.iy = y
        self.px = Cell.border + Cell.spacing  + x * Cell.spacing 
        self.py = Cell.border + Cell.spacing  + y * Cell.spacing 
        self.vers = []
        self.num_hatches = int(random(5, 12))
        self.type_hatches = random(10)       
      
    def plot(self):
        strokeWeight(1)
        for l in self.lines:
            l.plot()
        beginShape()
        noFill()
        strokeWeight(2)
        for p in self.vers:
            vertex(p.x, p.y)
        endShape(CLOSE)
        
    def update_vers(self):
        self.v0 = Cell.grid.get((self.ix-1, self.iy-1))
        self.v1 = Cell.grid.get((self.ix-1, self.iy+1))
        self.v3 = Cell.grid.get((self.ix+1, self.iy-1))
        self.v2 = Cell.grid.get((self.ix+1, self.iy+1))
        # if random(10) > 2:
        self.vers = [self.v0, self.v1, self.v2, self.v3]
        self.hatch()
        
    def hatch(self):
        self.lines = []
        n = self.num_hatches
        r = self.type_hatches
        if r > 2:                        
            self.lines.extend(par_hatch(self.vers, n, 0))
        if r < 8:
            self.lines.extend(par_hatch(self.vers, n, 1))
        
def keyPressed():
    print(U, V)
    if key == "n" or key == CODED:
        init_grid(GRID_SIZE)
        saveFrame("###.png")
    if key == "s": saveFrame("###.png")
    global U, V
    if keyCode == UP: U += 1
    if keyCode == DOWN and U > 1: U -= 1
    if keyCode == RIGHT: V += 1
    if keyCode == LEFT and V > 1: V -= 1    
                
# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
