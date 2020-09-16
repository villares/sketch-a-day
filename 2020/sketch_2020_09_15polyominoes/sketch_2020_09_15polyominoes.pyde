"""
From a talk by Hamish Campbell
https://pyvideo.org/kiwi-pycon-2013/polyominoes-an-exploration-in-problem-solving-w.html
"""
from polyomino import Polyomino

x, y, w = 5, 5, 5

def setup():
    size(640, 480)
    background(0)
    print(count_polys(10))
    
def count_polys(target):
    global x, y
    order = 1
    polyominoes = set([Polyomino(((0,0),))])

    while order < target:
        order += 1
        next_order_polyominoes = set()
        for polyomino in polyominoes:
            next_order_polyominoes.update(polyomino.raise_order())
        polyominoes = next_order_polyominoes

    for p in polyominoes:
        push()
        translate(x, y)
        p.draw(w)
        x += len(p) * w + 1
        pop()
        if x > width:
            x = 0
            y += len(p) * w
    


    return len(polyominoes)
