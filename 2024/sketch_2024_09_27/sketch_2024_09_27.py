from random import shuffle

import py5  # check out https://github.com/py5coding 
from py5_tools import animated_gif

grid = {}
heads = []
S = 20
NBS = [
    (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1) 
    ]

def setup():   # py5 will call this once to set things up
    py5.size(600, 600)
    py5.stroke_weight(4)
    start()
    
def start():
    grid.clear()
    heads.clear()
    shuffle(NBS)
    print(NBS)
    for _ in range(20):
        i, j = py5.random_int(-5, 5), py5.random_int(-5, 5)
        heads.append((i, j))
 
def draw():   # py5 will call this in a loop
    py5.background(200)
    py5.translate(py5.width / 2, py5.height / 2)
    for (i, j), (m, n) in grid.items():
        py5.line(i * S, j * S, m * S, n * S)
    for i, j in heads:
        py5.circle(i * S, j * S, 10)

def grow_all():
    for k, head in enumerate(heads):
       if new_head := grow_head(head):
           heads[k] = new_head
            
def grow_head(head):
    shuffle(NBS)
    i, j = head
    for oi, oj in NBS:
        ni, nj = i + oi, j + oj
        #py5.circle(ni * S, nj * S, 5)
        if grid.get((ni, nj)) is None:
            grid[ni, nj] = i, j
            #py5.circle(ni * S, nj * S, 10)
            return ni, nj
    return False
        
        
def key_pressed():   # py5 will call this when a key is pressed
    if py5.key == ' ':
        grow_all()
    elif py5.key == py5.DELETE:
        start()
    elif py5.key == 's':
#         f = py5.frame_count
#         animated_gif('out3.gif', frame_numbers=range(f + 1, f + 361, 4), duration=0.075) 
        py5.save_frame('out.png')
py5.run_sketch(block=False)
        
        



