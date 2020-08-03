
from itertools import chain

def setup():
    global b
    size(500, 500)
    b = set([(0,0),(-1,0),(-2,0),(0,-1),(-1,-2)])
    
def draw():
    global b;background(-1)
    for x,y in b:
        point(x,y)
    b = step(b)
    print(b)
        
def step(board):
    newstate = set()
    recalc = board | set(chain(*map(nbs, board)))
    for pt in recalc:
        count = sum((nb in board)
                    for nb in nbs(pt))
        if count == 3 or (count ==2 and pt in board):
            newstate.add(pt)
    return newstate
    
def nbs(pt):
    x, y = pt
    for i, j in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
        yield x+i,y+j
