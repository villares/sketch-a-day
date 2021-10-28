"""
Based on a talk by Hamish Campbell
https://pyvideo.org/kiwi-pycon-2013/polyominoes-an-exploration-in-problem-solving-w.html
"""
from polyomino import Polyomino

x, y, w = 20, 20, 8

def setup():
    size(1000, 1000)
    background(0)
    print(count_polys(7))
    saveFrame('a.png')
    
def count_polys(target):
    global x, y
    order = 1
    polyominoes = set([Polyomino(((0,0),))])
    all_p = set([])
    
    while order < target:
        order += 1
        next_order_polyominoes = set()
        for polyomino in polyominoes:
            next_order_polyominoes.update(polyomino.raise_order())
        polyominoes = next_order_polyominoes
        all_p.update(next_order_polyominoes)

    for p in sorted(all_p, key=len):
        push()
        translate(x, y)
        p.draw(w, c=True)
        x += len(p) * w + w
        pop()
        if x > width - w * len(p):
            x = 20
            y += len(p) * w
            if y > height:
                print('ugh!')
    
    return len(all_p)
