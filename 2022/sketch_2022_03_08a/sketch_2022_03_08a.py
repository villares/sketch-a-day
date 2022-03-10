from itertools import product
from functools import lru_cache
from random import shuffle, choice

import pickle

patterns = [  # TL, BL, TR, BR (1, 2, 3, 4),
(1, 1, 1, 1), (1, 1, 0, 0), (0, 0, 1, 1), (1, 0, 0, 0),
(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 0, 0, 0), 
(2, 0, 0, 0), (0, 2, 0, 0), (0, 0, 2, 0), (0, 0, 0, 2),
]
C = {0: color(100), 1: color(0, 100, 0), 2: color(0, 0, 100)}

SPACING, MARGIN = 0.5, 8
M_SIZE = 16
CORNER_POS = list(product((1, -1), repeat=2))

modules = {}

debug = {}

def setup():
    size(256, 256)
    rect_mode(CENTER)
    text_align(CENTER, CENTER)
    
    with open('out2x2.k', 'rb') as f:
        patterns = pickle.load(f)
    
    positions = product(range(15), repeat=2) 
    for pos in positions:
            ptts = list(patterns) #[:]#; shuffle(ptts)
            m = Module(pos, ptts)
            modules[pos] = m
            
def draw():
    global change
    change = False
    background(200)
    for k, v in modules.items():
        v.plot()
        v.update_nbs()
    if not change:
        collapse_random()


class Module:
    def __init__(self, pos, vals):
        self.pos = pos
        self.vals = vals
        self.x = M_SIZE + self.pos[0] * M_SIZE * 2 * SPACING + MARGIN
        self.y = M_SIZE + self.pos[1] * M_SIZE * 2 * SPACING + MARGIN
                
    def plot(self):
        stroke(128)
        push()
        if len(self.vals) == 1:
            no_stroke()
        for k, v in enumerate(self.vals):
            pattern = list(v)
            for i, j in CORNER_POS:
                xo, yo =  i * M_SIZE / 2, j * M_SIZE / 2 
                v = pattern.pop()
                #fill(C[v], 255 - k * 32)
                fill(v)
                square(self.x + xo, self.y + yo, M_SIZE)
        pop()
        
    def update_nbs(self):
        for ni, nj in NBS_UDLR:
            si, sj = self.pos
            nb = modules.get((si + ni, sj + nj))
            if nb and len(nb.vals) > 1:
                self.trim_nb(nb, ni, nj)
                
    def trim_nb(self, nb, ni, nj):
        global change
        for nv in reversed(nb.vals):
            if not match(tuple(self.vals), nv, ni, nj):
                nb.vals.remove(nv)
                change = True
               
@lru_cache               
def match(svals, nv, ni, nj):
#     match = False 
#     for sv in svals:
#         if NBS_CHECK[(ni, nj)](sv, nv):
#             match = True
#             break
#     return match
    return any(map(lambda sv: NBS_CHECK[(ni, nj)](sv, nv), svals))

                     
TL, BL, TR, BR =  0, 1, 2, 3 # (-1,-1),(1,-1),(1,-1),(1,1)

NBS_UDLR = ((0, -1), (0, 1), (-1, 0), (1, 0))

NBS_CHECK = {
( 0, -1): (lambda s, o: s[TL] == o[BL] and s[TR] == o[BR]),
( 0,  1): (lambda s, o: s[BL] == o[TL] and s[BR] == o[TR]),
( 1,  0): (lambda s, o: s[TL] == o[TR] and s[BL] == o[BR]),
(-1,  0): (lambda s, o: s[TR] == o[TL] and s[BR] == o[BL]),
}

        
def key_pressed():
    if key == 'r':
        for m in modules.values():
            shuffle(m.vals)
    if key == 'q':
        collapse_random()

def collapse_random():
        uncollapsed = sorted((m for m in modules.values() if len(m.vals) > 1),
                             key=lambda m:len(m.vals))
                             
        if uncollapsed:
            m = uncollapsed[0]
            m.vals[:] = [choice(m.vals)]
       # shuffle(modules[(5, 5)].vals) #[:] = [(0, 0, 0, 0)]
#         modules[(5, 5)].update_nbs()

        
        
