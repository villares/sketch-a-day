from itertools import product
from functools import lru_cache
from random import shuffle, choice

import pickle

C = {0: color(100), 1: color(0, 100, 0), 2: color(0, 0, 100)}

SPACING, MARGIN = 0.66, 50
M_SIZE = 60
CORNER_POS = list(product((-1, 0, 1), repeat=2))

modules = {}

debug = {}

def setup():
    size(512, 512)
    rect_mode(CENTER)
    text_align(CENTER, CENTER)
    #with open('out3x3.k', 'rb') as f:
    with open('b.k', 'rb') as f:
        patterns = pickle.load(f)
    
    positions = product(range(9), repeat=2) 
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
        collapse_next()

class Module:
    def __init__(self, pos, vals):
        self.pos = pos
        self.vals = vals
        self.x = M_SIZE + self.pos[0] * M_SIZE * SPACING + MARGIN
        self.y = M_SIZE + self.pos[1] * M_SIZE * SPACING + MARGIN
                
    def plot(self):
        stroke(128)
        push()
        if len(self.vals) == 1:
            no_stroke()
        for k, v in enumerate(self.vals):
            pattern = list(v)
            for k, (i, j) in enumerate(CORNER_POS):
                xo, yo =  i * M_SIZE / 3, j * M_SIZE / 3
                v = pattern.pop()
                fill(v)
                square(self.x + xo, self.y + yo, M_SIZE / 3)
                fill(255, 0, 0)
                #text(k, self.x + xo, self.y + yo)
            text(len(self.vals), self.x, self.y)
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
    return any(map(lambda sv: nbs_check(ni, nj, sv, nv), svals))

@lru_cache               
def nbs_check(ni, nj, sv, nv):
    return NBS_CHECK[(ni, nj)](sv, nv)


NBS_UDLR = ((0, -1), (0, 1), (-1, 0), (1, 0))
TL, TM, TR = 0, 3, 6
ML, MM, MR = 1, 4, 7
BL, BM, BR = 2, 5, 8
NBS_CHECK = {
  ( 0,  1): (lambda s, o: s[TL] == o[BL] and s[TR] == o[BR] and s[TM] == o[BM]),
  ( 0, -1): (lambda s, o: s[BL] == o[TL] and s[BR] == o[TR] and s[BM] == o[TM]),
  ( 1,  0): (lambda s, o: s[TL] == o[TR] and s[BL] == o[BR] and s[ML] == o[MR]),
  (-1,  0): (lambda s, o: s[TR] == o[TL] and s[BR] == o[BL] and s[MR] == o[ML]),
}

        
def key_pressed():
    if key == 'r':
        for m in modules.values():
            shuffle(m.vals)
    if key == 'q':
        collapse_random()

def collapse_next():
        uncollapsed = sorted((m for m in modules.values() if len(m.vals) > 1),
                             key=lambda m:len(m.vals))                             
        if uncollapsed:
            m = uncollapsed[0]
            m.vals[:] = [choice(m.vals)]
        else:
            no_loop()
            print('done')

        
        
