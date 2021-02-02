
NBS = ((-1, -1), (0, -1), (1, -1),
       (-1,  0),          (1,  0),
       (-1,  1), (0,  1), (1,  1))
ONBS = ((0, -1),  (-1,  0), (1,  0), (0,  1))
DNBS = ((-1, -1),  (-1,  1), (1,  -1), (1,  1))

SIZE = 10
sf = 1

def setup():
    size(500, 500)
    noStroke()
    Cell(0, 0)
    noLoop()
    
def draw():
    background(100, 100, 200)
    translate(width / 2, height / 2)
    scale(sf)
    for c in Cell.grid.values():
        c.grow()
    for c in Cell.grid.values():
        c.display()


def keyPressed():
    global sf
    sf *= .99
    # for c in Cell.grid.values():
    #     c.grow()
    #     c.display()
    print Cell.grid.keys()
    redraw()


class Cell:
    grid = {}

    def __init__(self, i, j):
        self.pos = (i, j)
        self.grid[self.pos] = self
        
    def display(self):
        i, j = self.pos
        fill(0, 100, 0, 100)
        circle(i * SIZE, j * SIZE, SIZE * 1.5 )
        
        
    def grow(self):
        i, j = self.pos
        for noi, noj in NBS:
            ni, nj = i + noi, j + noj
            # fill(255, 100)
            # circle(ni * SIZE, nj * SIZE, SIZE * .5 )
            if not any(self.grid.get((ni + oi, nj + oj)) 
                       for oi, oj in DNBS
                       if (ni + oi, nj + oj) != self.pos):
                if random(100) < 50 and ((ni, nj) not in self.grid):
                    Cell(ni, nj)
            
    
        
        
