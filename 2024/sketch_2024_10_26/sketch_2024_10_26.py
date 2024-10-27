# check out https://py5coding.org 

from collections import Counter

import py5

def setup():
    py5.size(500, 500)
    r = lambda : 250 + py5.random_gaussian() * 50
    c = Counter(int(r()) for _ in range(40_000))
    for x, h, in c.items():
        py5.line(x, 450, x, 450 - h)
        
py5.run_sketch()
        