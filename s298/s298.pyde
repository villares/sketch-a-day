# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s298"  # 20181023
OUTPUT = ".png"
GRID_SIZE = 16

def setup():
    size(500, 500)
    init_grid(GRID_SIZE)
    
def draw():
    translate(Cell.spacing/2 + width/2, Cell.spacing/2 + height/2)
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
                Cell.cells.append(new_node)  # mudar!
                Cell.grid[x, y] = new_node   # extrarir do dict
   
class Node():
    nodes = []
    grid = dict()

    def __init__(self, x, y):
        self.ix = x
        self.iy = y
        self.px = Cell.border + Cell.spacing / 2 + x * Cell.spacing - width / 2
        self.py = Cell.border + Cell.spacing / 2 + y * Cell.spacing - width / 2
                
    def plot(self):
        ellipse(self.px, self.py, 5, 5) 


class Cell():
    cells = []
    grid = dict()
    ver = []

    def __init__(self, x, y):
        self.ix = x
        self.iy = y
        self.px = Cell.border + Cell.spacing / 2 + x * Cell.spacing - width / 2
        self.py = Cell.border + Cell.spacing / 2 + y * Cell.spacing - width / 2
        self.ver = []
                
    def plot(self):
        ellipse(self.px, self.py, 10, 10) 
        
        
    def draw_ver(self):
        if len(self.ver) > 1:
            for n0, n1 in pairwise(self.ver):
                line(n0.x, n0.y, n1.x, n1.y)


   
# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
