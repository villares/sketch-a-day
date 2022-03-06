from itertools import product
from random import shuffle, choice

patterns = [  # TL, BL, TR, BR (1, 2, 3, 4),
(1, 1, 1, 1), (1, 1, 0, 0), (0, 0, 1, 1), (1, 0, 0, 0),
(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 0, 0, 0), 
(2, 0, 0, 0), (0, 2, 0, 0), (0, 0, 2, 0), (0, 0, 0, 2),
]
C = {0: color(100), 1: color(0, 100, 0), 2: color(0, 0, 100)}

SPACING, MARGIN = 0.5, 8
M_SIZE = 16

modules = {}

debug = {}

def setup():
    size(516, 516)
    rect_mode(CENTER)
    text_align(CENTER, CENTER)
    positions = product(range(30), repeat=2) 
    for pos in positions:
            ptts = patterns[:]#; shuffle(ptts)
            m = Module(pos, ptts)
            modules[pos] = m
            
def draw():
    global change
    change = False
    background(200)
    for k, v in modules.items():
        v.plot()
        v.check_nbs()
    if not change:
        collapse_random()


class Module:
    def __init__(self, p, vals):
        self.p = p
        self.vals = vals
        
    def plot(self):
        stroke(128)
        ms = M_SIZE
        corners = list(product((1, -1), repeat=2))
        x = ms + self.p[0] * ms * 2 * SPACING + MARGIN
        y = ms + self.p[1] * ms * 2 * SPACING + MARGIN
        push()
        if len(self.vals) == 1:
            no_stroke()
        for k, v in enumerate(self.vals):
            pattern = list(v)
            for i, j in corners:
                v = pattern.pop()
                fill(C[v], 255 - k * 32)
                square(x + i * ms / 2, y + j * ms / 2, ms)
        pop()
        
    def check_nbs(self):
        ms = M_SIZE
        x = ms + self.p[0] * ms * 2 * SPACING + MARGIN
        y = ms + self.p[1] * ms * 2 * SPACING + MARGIN
        match = 0
        for (ni, nj), check_func in NBS_CHECK.items():
            si, sj = self.p
            nb = modules.get((si + ni, sj + nj))
            if nb:
                self.trim_nb(nb, check_func)
                
    def trim_nb(self, nb, check_func):
        global change
        for nv in reversed(nb.vals):
            match = False
            for sv in self.vals:
                if check_func(sv, nv):
                    match = True
                    break
            if not match:
                nb.vals.remove(nv)
                change = True

#     def trim_nb(self, nb, check_func):
#         global change
#         for sv in reversed(self.vals):
#             match = False
#             for nv in nb.vals:
#                 if check_func(sv, nv):
#                     match = True
#             if not match:
#                 self.vals.remove(sv)
#                 change = True

    def check_nb(self, nb, check_func):
        for nv in nb.vals:
            for sv in self.vals:
                if check_func(sv, nv):
                    return True
        return False
                     
TL, BL, TR, BR =  0, 1, 2, 3 # (-1,-1),(1,-1),(1,-1),(1,1)
NBS_CHECK = {
(0, -1): (lambda s, o: s[TL] == o[BL] and s[TR] == o[BR]),
(0,  1): (lambda s, o: s[BL] == o[TL] and s[BR] == o[TR]),
(-1, 0): (lambda s, o: s[TL] == o[TR] and s[BL] == o[BR]),
(1, 0): (lambda s, o: s[TR] == o[TL] and s[BR] == o[BL]),
}

        
def key_pressed():
    if key == 'r':
        for m in modules.values():
            shuffle(m.vals)
    if key == 'q':
        collapse_random()

def collapse_random():
        uncollapsed = [m for m in modules.values() if len(m.vals) > 1]
        if uncollapsed:
            m = choice(uncollapsed)
            m.vals[:] = [choice(m.vals)]
       # shuffle(modules[(5, 5)].vals) #[:] = [(0, 0, 0, 0)]
#         modules[(5, 5)].check_nbs()

        
        
