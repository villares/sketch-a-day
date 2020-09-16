"""
From a talk by Hamish Campbell
https://pyvideo.org/kiwi-pycon-2013/polyominoes-an-exploration-in-problem-solving-w.html
"""
from polyomino import Polyomino

x, y, w = 5, 3, 3

def setup():
    size(750, 550)
    background(0)
    print(count_polys(8))
    
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
