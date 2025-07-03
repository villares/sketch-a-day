# Alexandre B A Villares -https://abav.lugaralgum.com/sketch-a-day
# Inspired by my sketch "s315"  # 20181109
# py5 imported mode sketch, learn more at py5coding.org

from villares.line_geometry import Line, par_hatch

GRID_SIZE = 36
SEED = 2

# this rule was used to choose nodes that would move on 
# earlier regular grid deformation sketches (now it's just a random selection)
rule = lambda x, y: random(40) < 20

def setup():
    size(700, 700)
    stroke_cap(SQUARE)
    init_grid(GRID_SIZE)
    background(0)
    random_seed(SEED)

def draw():
    f = frame_count / 10
    t = cos(f) / 2 + 0.25
    
    if frame_count % 2 == 0:
        print(t)
        for c in Cell.cells:
            c.plot(t)  
            
    if 0 < f < TWO_PI:
        pass # possible save frames 
    else:
        no_loop()


def init_grid(grid_size):
    Cell.border = 100.
    Cell.spacing = (width - Cell.border *2) / grid_size
    Cell.cells = []
    for x in range(0, grid_size, 2):
        for y in range(0, grid_size, 6):
                new_cell = Cell(x, y)
                Cell.cells.append(new_cell)
                Cell.grid[x, y] = new_cell
                
    #random_seed(frame_count + 2) 
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
        if rule(x, y):
           mx, my = width/2, height/2
           self.px += (self.px - mx) * 0.15 
           self.py += (self.py - my) * 0.15
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
        self.num_hatches = int(random(3, 6))#int(random(5, 12))
        self.type_hatches = random(10)      
      
    def plot(self, t):    
        L0, V0 = self.lines, self.vers
        L1, V1 = self.lines_f, self.vers_f

        stroke_weight(1)
        c = lerp_color(color(255, 0, 0),
                       color(0, 0, 255, 100), t)
        stroke(c) 
        for l0, l1 in zip(L0, L1):
            l = l0.lerp(l1, t)
            l.plot()
        no_fill()
        with begin_closed_shape():
            #strokeWeight(1)
            #stroke(100, 0, 100)
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
        if r > 2:                        
            self.lines.extend(par_hatch(self.vers, n, 0))
            self.lines_f.extend(par_hatch(self.vers_f, n, 0))
        if r < 8:
            self.lines.extend(par_hatch(self.vers, n, 1))
            self.lines_f.extend(par_hatch(self.vers_f, n, 1))
        
def key_pressed():
    if key == "s":
        save_frame(f"{SEED}.png")

