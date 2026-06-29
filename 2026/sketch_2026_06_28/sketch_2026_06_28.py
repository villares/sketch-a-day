# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# This is a py5 "imported mode" sketch, more on <https://py5coding.org>
# Based on "s310"  # 20181104

from py5_tools import animated_gif

GRID_SIZE = 18

from villares.geometry_helpers import par_hatch, Line

rule = lambda x, y: random(40) < 20

def setup():
    #strokeCap(SQUARE)
    size(700, 700)
    # smooth(8)
    init_grid(GRID_SIZE)
    animated_gif('out.gif',
                 duration=0.266,
                 frame_numbers=range(1, 181, 10))
    
def draw():
    background(200)
    stroke(0)
    f = radians(frame_count * 2)
    t = 0.25 + sin(f) / 4 # 0.5 + sin(f) / 2    
    for c in Cell.cells:
        c.draw(t)

def init_grid(grid_size):
    Cell.border = 75.
    Cell.spacing = (width - Cell.border *2) / grid_size
    Cell.cells = []
    random_seed(1)
    for x in range(0, grid_size, 2):
        for y in range(0, grid_size, 2):
                new_cell = Cell(x, y)
                Cell.cells.append(new_cell)
                Cell.grid[x, y] = new_cell
                
    random_seed(frame_count) 
    for x in range(-1, grid_size+1, 2):
        for y in range(-1, grid_size+1, 2):
                Node.grid0[x, y] = Node(x, y)   # extrarir do dict
                Node.grid1[x, y] = Node(x, y)   # extrarir do dict


    for c in Cell.cells:
        c.update_vers()
   
class Node():
    grid0 = dict()
    grid1 = dict()

    def __init__(self, x, y):
        self.ix = x
        self.iy = y
        self.px = Cell.border + Cell.spacing + x * Cell.spacing 
        self.py = Cell.border + Cell.spacing + y * Cell.spacing
        mx, my = width/2, height/2
        if rule(x, y):
           self.px += (self.px - mx) * 0.1 
           self.py += (self.py - my) * 0.1
        else:
           self.px -= (self.px - mx) * 0.1 
           self.py -= (self.py - my) * 0.1
        
        self.x = self.px
        self.y = self.py
        
    def __iter__(self):
        return iter((self.x, self.y))

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
      
    def draw(self, t):    
        L0, V0 = self.lines, self.vers
        L1, V1 = self.lines_f, self.vers_f

        stroke_weight(1)
        for l0, l1 in zip(L0, L1):
            l = l0.lerp(l1, t)
            l.draw()
        with begin_closed_shape():
            no_fill()
            stroke_weight(2)
            for p0, p1 in zip(V0, V1):
                vertex(lerp(p0.x, p1.x, t), lerp(p0.y, p1.y, t) )
        
    def update_vers(self):
        self.v0 = Node.grid0.get((self.ix-1, self.iy-1))
        self.v1 = Node.grid0.get((self.ix-1, self.iy+1))
        self.v3 = Node.grid0.get((self.ix+1, self.iy-1))
        self.v2 = Node.grid0.get((self.ix+1, self.iy+1))
        self.vers = [self.v0, self.v1, self.v2, self.v3]
        self.v0f = Node.grid1.get((self.ix-1, self.iy-1))
        self.v1f = Node.grid1.get((self.ix-1, self.iy+1))
        self.v3f = Node.grid1.get((self.ix+1, self.iy-1))
        self.v2f = Node.grid1.get((self.ix+1, self.iy+1))
        self.vers_f = [self.v0f, self.v1f, self.v2f, self.v3f]
        self.hatch()
        
    def hatch(self):
        self.lines = []
        self.lines_f = []
        n = self.num_hatches
        r = self.type_hatches
        if r > 3:                        
            self.lines.extend(par_hatch(self.vers, n, 0))
            self.lines_f.extend(par_hatch(self.vers_f, n, 0))
        if r < 7:
            self.lines.extend(par_hatch(self.vers, n, 1))
            self.lines_f.extend(par_hatch(self.vers_f, n, 1))
        
def key_pressed():
    if key == "n" or key == CODED:
        init_grid(GRID_SIZE)
    if key == "s":
        save_frame("###.png")

