from itertools import product

import py5

N = 21

def setup():
    global truchets
    py5.size(900, 690)
    # I was using -1 and -2 for black and white modules
    # but it created trouble with the hashes...
    configs = product((0, 1, 2, 3, -10, -20),repeat=4)
    truchets = sorted({Truchets(config) for config in configs})
    print(len(truchets))

    py5.background(150)
    cel = py5.width / N
    k = 0
    for i , j in product(range(N), repeat=2):
        x = j * cel + cel / 2
        y = i * cel + cel / 2
        if k < len(truchets):
            truchets[k].draw(x, y , int(cel) - 10)
        k += 1        

    py5.save(__file__[:-3] + '.png')

class Truchets:
    
    def __init__(self, config):
        self.config = tuple(m for m in config)
    
    def __hash__(self):
        c = self.config
        h = hash(c)
        for _ in range(3):
            c = rot_config(c)
            rh = hash(c)
            h =  min(rh, h)
        return h
        
    def __eq__(self, other):
        return hash(self) == hash(other)
    
    def __lt__(self, other):
        return self.config < other.config
    
    def draw(self, x, y, w):
        pos = ((x - w / 4, y - w / 4),
               (x + w / 4, y - w / 4),
               (x + w / 4, y + w / 4),
               (x - w / 4, y + w / 4))
        for (x, y), m in zip(pos, self.config):
            self.module(x , y, w / 2, m)

    @staticmethod  
    def module(x, y, w, m):
        py5.no_stroke()
        py5.rect_mode(py5.CENTER) # retângulos pelo centro
        with py5.push_matrix():
            py5.translate(x, y) # muda o 0, 0
            if m == -20:
                py5.fill(255)
                py5.square(0, 0, w)
                return
            elif m ==-10:
                py5.fill(0)
                py5.square(0, 0, w)
                return    
            else:
                py5.fill(255)
                py5.square(0, 0, w)
                py5.fill(0)
                py5.rotate(m * py5.radians(90))
                py5.triangle(w / 2, -w / 2,
                         w / 2,  w / 2,
                        -w / 2,  w / 2)
            
def rot_pos(config):
    ultimo = config[-1],  #ja em forma de tupla
    return ultimo + config[:3]

def rot_module(m):
    if m < 0:
        return m
    return (m + 1) % 4

def rot_config(config):
    return tuple(rot_module(m) for m in rot_pos(config))

py5.run_sketch(block=False)

