SIZE, scale_factor = 10, 1
NBS = ((-1, -1), (0, -1), (1, -1), # 
       (-1,  0),          (1,  0),
       (-1,  1), (0,  1), (1,  1))
grid = {(0, 0)}  # a set of tuples

def setup():
    size(500, 500)
    noStroke()
    noLoop()  # redraw on keyPressed()
    
def draw():
    background(100, 100, 200)
    translate(width / 2, height / 2)
    scale(scale_factor)
    for c in grid:
        grow(c)
    for i, j in grid:
        fill(100, 50, 0)
        circle(i * SIZE, j * SIZE, SIZE * 1.5 )
  
def grow(c):
    i, j = c
    for noi, noj in NBS:
        ni, nj = i + noi, j + noj
        if not any(((ni + oi, nj + oj) in grid)
                for oi, oj in NBS
                if (ni + oi, nj + oj) != c):
            if random(100) < 10:
                    grid.add((ni, nj))
        
def keyPressed():
    global scale_factor
    scale_factor *= .997
    print grid
    redraw()

    
ONBS = ((0, -1),  (-1,  0), (1,  0), (0,  1))
DNBS = ((-1, -1),  (-1,  1), (1,  -1), (1,  1))      
