from collections import Counter

import py5 # check out https://py5coding.org 

from polyomino import Polyomino # Based on a talk by Hamish Campbell

N = 8   # order
M = 20  # margin
w = 5   # component square size
    

def setup():
    py5.size(1750, 600)
    py5.background(240)
    Polyomino.REMOVE_MIRRORED = True # generates free polyomninoes
    polyominoes = Polyomino.get_polyominoes(N, up_to=True) 
    print(len(polyominoes))
    
    x, y = M, M
    for i, p in enumerate(sorted(polyominoes, key=long), 1):
        with py5.push_matrix():
            py5.translate(x, y)
            #py5.no_stroke()
            p.draw(w, color_func=colorize)
            x += N * w + w
            if x > py5.width - w * N:
                x = M
                y += N * w
                if y > py5.height:
                    print(f'{i} of {len(polyominoes)}')
                    break
    
    py5.save_frame('a.png')
    
def long(p):
    xs, ys = zip(*p.squares)
    return len(p) * 100 + max(max(xs) - min(xs), max(ys) - min(ys))
    
def colorize(x, y, i):
    py5.fill(255 - (x + 1) * w * 8,
             255 - (y + 1) * w * 8,
             (i + 1) * w * 8)
    

        
py5.run_sketch()
        