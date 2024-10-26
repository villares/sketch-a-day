# check out https://py5coding.org 

from collections import Counter
from functools import partial
from random import triangular

import py5

def setup():
    py5.size(400, 400)
    r = partial(triangular, 10, 390)
    c = Counter(int(r()) for _ in range(50_000))
    for x, h, in c.items():
        py5.line(x, 390, x, 390 - h)
        
py5.run_sketch()
        