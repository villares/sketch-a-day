from itertools import product
from random import shuffle

patterns = [  # TL, BL, TR, BR (1, 2, 3, 4),
(1, 1, 1, 1), (1, 1, 0, 0), (0, 0, 1, 1), (1, 0, 0, 0),
(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 0, 0, 0), 
]

SPACING, MARGIN = 2, 50
M_SIZE = 20

modules = {}

debug = {}

def setup():
    size(850, 850)
    rect_mode(CENTER)
    text_align(CENTER, CENTER)
    positions = product(range(10), repeat=2) 
    for pos in positions:
            ptts = patterns[:]; shuffle(ptts)
            m = Module(pos, ptts)
            modules[pos] = m
            
def draw():
    background(200)
    for k, v in modules.items():
        v.plot()
        #v.check_nbs()

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
        
        for k, svals in enumerate(self.vals):
            vals = list(svals[:])
            translate(-5, -5)
            for i, j in corners:
                v = vals.pop()
                fill(v * 255, 100)
                square(x + i * ms / 2, y + j * ms / 2, ms)
        fill(255, 0, 0)
            #text(len(vals), x + i * ms / 2, y + j * ms / 2)
        self.check_nbs()    
        pop()
        
    def check_nbs(self):
        ms = M_SIZE
        x = ms + self.p[0] * ms * 2 * SPACING + MARGIN
        y = ms + self.p[1] * ms * 2 * SPACING + MARGIN
        match = 0
        for (ni, nj), check in NBS_CHECK.items():
            si, sj = self.p
            nb = modules.get((si + ni, sj + nj))
#             if nb and nb.vals:
#                 match = False
#                 nv = nb.vals[0]
#                 for sv in self.vals:
#                     if check(sv, nv):
#                         match = True
            if nb:
                nv = nb.vals[0]
                sv = self.vals[0]
                if check(sv, nv):
                    match += 1
                    m = 1
                else:
                    m = 0
                text(m, x + ni * M_SIZE / 2, y + nj * M_SIZE / 2) 

TL, BL, TR, BR =  0, 1, 2, 3 # (-1,-1),(1,-1),(1,-1),(1,1)
        
NBS = (
(-1, -1), (-1, 0), (-1, 1),
( 0, -1),          ( 0, 1),
( 1, -1), ( 1, 0), ( 1, 1)
)       

NBS_CHECK = {
#(-1, -1): (lambda s, o: s[TL] == o[BL] ),
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
        modules[(5, 5)].vals[:] = [(0, 0, 0, 0)]
       # shuffle(modules[(5, 5)].vals) #[:] = [(0, 0, 0, 0)]
#         modules[(5, 5)].check_nbs()

        
        
