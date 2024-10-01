# ideas... 6 possible modules, 2 x 2 -> 6 ** 4 -> 1296
# But how to sort by "partitions" when same-color regions merge?

from itertools import product, combinations
from copy import copy

import py5  # check out https://github.com/py5coding 

def setup():
    py5.size(600, 600)
    py5.stroke_join(py5.ROUND)

def draw():
    py5.background(200)    
    Region.grid(4)
    r = Region([(0, 1), (1, 1), (1, 0)])
    r.draw()
    
def key_pressed():
    py5.save_frame('###.png')
    
class Region:
    
    S = 150 # scale
    M = 75 # margin
    
    def __init__(self, vs, c=0):
        self.vs = vs
        self.edges = Region.to_edges(vs)
        self.color = c
        
    def __iter__(self):
        return iter(self.vs)
    
    def draw(self):
        with py5.push(), py5.begin_closed_shape():
            py5.scale(self.S)
            py5.no_fill()
            py5.stroke(255)
            py5.stroke_weight(3 / self.S)
            py5.vertices(self.vs)
    
    @staticmethod
    def to_edges(vs):
        return set(frozenset((v, vs[i-1])) for i, v in enumerate(vs))

    @staticmethod
    def from_edges(edges):
        edge_list = list(edges)
        vs = list(edge_list.pop())
        while len(edge_list):
            a = vs[-1]
            edge = edge_list.pop(0)
            b, c = edge
            if a == b:
                vs.append(c)
                a = c
            elif a == c:
                vs.append(b)
            else:
                edge_list.append(edge)
        return vs[:-1]       

    @classmethod
    def grid(cls, n, m=None):
        cls.GRID = list(product(range(n), range(m or n)))
        py5.translate(cls.M, cls.M)
        py5.stroke(0)
        py5.stroke_weight(5)
        py5.points((x * cls.S, y * cls.S)
                   for x, y in cls.GRID)


py5.run_sketch(block=False)
        
        




