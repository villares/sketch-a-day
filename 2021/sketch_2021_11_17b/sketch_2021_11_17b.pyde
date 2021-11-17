from random import sample, shuffle, seed

nodes = {}
unvisited_nodes = []                   
step = 5
NBS = ((-2, -2), (-2, 0), (-2, 2), (0, -2), (0, 2), (2, -2), (2, 0), (2, 2))
nbs = []
color_dict = {}

def setup():
    global w, h
    size(1600, 800, FX2D)
    colorMode(HSB),
    noSmooth()
    w, h = width / 2 / step - 5, height / 2 / step - 5
    strokeWeight(2)
    start()
    
def start():
    nbs[:] = NBS
    shuffle(nbs)
    color_dict.update({nb:  color(i * 32, 255, 128)  # HSB color dict
                      for i, nb in enumerate(nbs)})  # for shuffled nbs
    nodes.clear()
    x1, y1 = int(random(-w, w)), int(random(-h, h)) 
    x2, y2 = int(random(-w, w)), int(random(-h, h))
    while not (x1 % 2 == x2 % 2) ^ (y1 % 2 == y2 % 2):
        x2, y2 = int(random(-w, w)), int(random(-h, h))
    unvisited_nodes[:] = [(x1, y1), (x2, y2)]
    
def draw():
    background(240)
    translate(width / 2, height / 2)
    for n, v in nodes.items():
        xa, ya = n
        xb, yb, c = v
        stroke(c)
        line(xa * step, ya * step, xb * step, yb * step)
    grow(frameCount // 50)
    
def keyPressed():
    if key == ' ':
        start()
                
def grow(s):
    if s % 10 == 0:
        shuffle(unvisited_nodes)
    new_nodes = []  
    while unvisited_nodes:
        x, y = unvisited_nodes.pop()
        seed(s + int(y / 25))
        xnbs = sample(NBS, int(random(5, 7)))# int(map(x, -w, w, 2, 7)))
        for nx, ny in xnbs:            
            xnx, yny = x + nx, y + ny
            visible = (abs(xnx * step) < width / 2 - step * 5 and
                       abs(yny * step) < height / 2 - step * 5 )
            if visible and (xnx, yny) not in nodes:
                c = color_dict[(nx, ny)]
                nodes[(xnx, yny)] = (x, y, c)
                new_nodes.append((xnx, yny))
    unvisited_nodes[:] = new_nodes
      
