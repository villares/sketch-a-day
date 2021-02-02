SIZE, scale_factor = 10, 1
NBS = ((-1, -1), (0, -1), (1, -1), # 
       (-1,  0),          (1,  0),
       (-1,  1), (0,  1), (1,  1))
grid = {(0, 0):(0, 0)}  # a dict, the value is the parent node

def setup():
    size(500, 500)
    strokeWeight(5)
    noLoop()  # redraw on keyPressed()
    
def draw():
    background(100, 200, 100)
    translate(width / 2, height / 2)
    scale(scale_factor)
    for c in grid:
        grow(c)
    for (xa, ya), (xb, yb) in grid.items():
        stroke(100, 50, 0)
        line(xa * SIZE, ya * SIZE, xb * SIZE, yb * SIZE)
  
def grow(c):
    i, j = c
    for noi, noj in NBS:
        ni, nj = i + noi, j + noj
        if not any(((ni + oi, nj + oj) in grid)
                for oi, oj in NBS
                if (ni + oi, nj + oj) != c):
            if random(100) < 10:
                    grid[(ni, nj)] = (i, j)
        
def keyPressed():
    global scale_factor
    scale_factor *= .997
    print grid
    redraw()

    
ONBS = ((0, -1),  (-1,  0), (1,  0), (0,  1))
DNBS = ((-1, -1),  (-1,  1), (1,  -1), (1,  1))      
