from random import shuffle
from itertools import product

import py5  # check out https://github.com/py5coding 

grid = {}
heads = []
still_heads = []
S = 18
W = 10
NBS = [
    (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1) 
    ]

def setup():
    global img
    py5.size(600, 600)
    img = py5.load_image('brasil.png')
    start()
    
def start():
    grid.clear()
    heads.clear()
    shuffle(NBS)
    print(NBS)
    for _ in range(10):
        i, j = py5.random_int(0,7), py5.random_int(-3, 4)
        heads.append((i, j))
        grid[i, j] = None
 
def draw():  
    py5.background(240)
    #py5.image(img, 0, 0)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.stroke(0, 100, 0)
    py5.stroke_weight(W)
    for k, v in grid.items():
        if v is not None:
            i, j = k
            m, n = v 
            py5.line(i * S, j * S, m * S, n * S)
    for i, j in heads + still_heads:
        if img.get_pixels(i * S + 300, j * S + 300) == py5.color(0):
            h = grid.get((i, j))
            if h:
                py5.circle(i * S, j * S, W / 2)




def grow_all():
    for k, head in enumerate(heads):
       if new_head := grow_head(head):
           heads[k] = new_head
            
def grow_head(head):
    shuffle(NBS)
    i, j = head
    if True: #check_b(i, j):
        for oi, oj in NBS:
            ni, nj = i + oi, j + oj        
            if check_b(ni, nj) and grid.get((ni, nj)) is None:
                grid[ni, nj] = i, j
                return ni, nj
        else:
            still_heads.append(head)
    return find_new_head()
    
def find_new_head():
    ni, nj = list(grid.keys())[-1]
    while grid.get((ni, nj)):
        ni, nj = py5.random_int(-20, 20), py5.random_int(-20, 20)
    return ni, nj    
        
        
    return False
        
def check_b(ni, nj):
    px = img.get_pixels(ni * S + 300, nj * S + 300)
    #print(px)
    return px == py5.color(0)
        
def key_pressed():   # py5 will call this when a key is pressed
    if py5.key == ' ':
        grow_all()
    elif py5.key == py5.DELETE:
        start()
    elif py5.key == 's':
        py5.save_frame('###.png')
        
py5.run_sketch(block=False)
        
        



