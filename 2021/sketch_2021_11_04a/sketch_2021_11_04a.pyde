
nodes = {(0, 0): (0, 0)}
step = 20
n_size = 10
nbs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),)# (1, 1))

def setup():
    size(600, 600)
    strokeWeight(3)
    
def draw():
    background(200, 220, 240)
    translate(width / 2, height / 2)
    
    for n, v in nodes.items():
        xa, ya = n
        xb, yb = v
        stroke(0)
        line(xa * step, ya * step, xb * step, yb * step)
        noStroke()
        fill(0)
        circle(xa * step, ya * step, n_size)

def keyPressed():
    if key == ' ':
        for _ in range(10):
            grow()
            
def grow():
    for x, y in nodes.keys():
        for nx, ny in nbs:
            xnx, yny = x + nx, y + ny
            if (xnx, yny) not in nodes:
                nodes[(xnx, yny)] = (x, y)
        
