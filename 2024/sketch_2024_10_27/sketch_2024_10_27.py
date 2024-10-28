from collections import Counter

import py5 # check out https://py5coding.org 

from polyomino import Polyomino # Based on a talk by Hamish Campbell

M = 20  # margin
w = 5   # component square size
    

def setup():
    py5.size(1850, 750)
    py5.background(0)
    # Polyomino.REMOVE_MIRRORED = True # generates 369 free octominoes
    polyominoes = get_polyominoes(8, up_to=False) # 704 one-sided octominoes
    print(len(polyominoes))
    
    x, y = M, M
    for i, p in enumerate(sorted(polyominoes, key=long), 1):
        with py5.push_matrix():
            py5.translate(x, y)
            p.draw(w, c=True)
            x += len(p) * w + w
            if x > py5.width - w * len(p):
                x = M
                y += len(p) * w
                if y > py5.height:
                    print(f'{i} of {len(polyominoes)}')
                    break
    
    py5.save_frame('a.png')
    
def long(p):
    xs, ys = zip(*p.squares)
    return max(max(xs) - min(xs), max(ys) - min(ys))
    
def get_polyominoes(target, up_to=False):
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
    if up_to:
        return all_p
    return polyominoes

        
py5.run_sketch()
        