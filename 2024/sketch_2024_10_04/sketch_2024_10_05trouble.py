# ideas... 6 possible modules, 2 x 2 -> 6 ** 4 -> 1296
# But how to sort by "partitions" when same-color regions merge?

from itertools import product, combinations

import py5  # check out https://github.com/py5coding 

def setup():
    py5.size(600, 600)
    py5.stroke_join(py5.ROUND)
    py5.color_mode(py5.HSB)
    Region.elements = {
        Region([(0, 1), (1, 1), (1, 2)], color=0),
        Region([(2, 0), (3, 0), (3, 1), (3, 2),
                (2, 3), (2, 2), (2, 1)], color=0),

        Region([(2, 3), (3, 2), (3, 3)], color=255),
        }
    problem =  Region([(2, 3), (1, 3), (0, 3), (0, 2),
                (0, 1), (1, 1), (1, 2), (0, 1),
                (0, 0), (1, 0), (2, 0), (2, 1),
                (2, 2)], color=255)
    print(problem.vs)
    
    
def start():
    Region.elements = set()
    for i, j in product(range(3), repeat=2):
        t = py5.random_choice((0, 1))
        ca = py5.random_choice((0, 255))
        cb = py5.random_choice((0, 255))
        if t == 1:
            ra = Region([(i, j), (i + 1, j), (i + 1, j + 1)], color=ca)
            rb = Region([(i, j), (i, j + 1), (i + 1, j + 1)], color=cb)
        else:
            ra = Region([(i, j), (i + 1, j), (i, j + 1)], color=ca)
            rb = Region([(i, j + 1), (i + 1, j), (i + 1, j + 1)], color=cb)           
        Region.elements.update((ra, rb))
    Region.merge_regions()
    print(f'# set of {len(Region.elements)} Regions')
    for region in sorted(Region.elements, key= lambda e: e.vs):
        print(region)

    
def draw():
#     py5.background(200)    
#     Region.grid(4)
#     #py5.translate(-4, -4) 
#     for i, r in enumerate(sorted(Region.elements)):
#         #py5.translate(2, 2) # debug!
#         r.draw(i)
    py5.translate(10, 10)        
    vs =  [(2, 3), (1, 3), (0, 3), (0, 2),
       (0, 0.9), (1, 1), (1, 2), (0, 1),
       (0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    with py5.begin_closed_shape():
        for i, (x, y) in enumerate(vs):
            py5.fill(255, 100)
            py5.vertex(x * 150, y * 150)
            
    for i, (x, y) in enumerate(vs):
        py5.fill(0)
        py5.text(str((x, y)), x * 150, y * 150)


def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    elif py5.key == ' ':
        start()


            
#@functools.total_ordering
class Region:
    
    S = 150 # scale
    M = 75 # margin
    elements = {}
    
    def __init__(self, vs, color=0):
        self.vs = vs
        self.edges = self.to_edges()
        self.color = color
        self.area = self.calc_area()
        self.centroid = self.calc_centroid()
        
    def __repr__(self):
        return f'Region({self.vs}, color={self.color})' 
        
#     def __iter__(self):
#         return iter(self.vs)
    
    def __eq__(self, other):
        return self.area == other.area
    
    def __gt__(self, other):
        return self.area > other.area
    
    def __hash__(self):
        return hash(self.edges)
    
    def __add__(self, other):
        if self.color == other.color and self.isadjacent(other):
            new_edges = self.edges ^ other.edges
            return self.__class__(self.to_vertices(new_edges), self.color)
        else:
            raise TypeError
    
    def isadjacent(self, other):
        return not self.edges.isdisjoint(other.edges)
 
    def draw(self, i=None):
        with py5.push():
            py5.scale(self.S)
            py5.fill(self.color, 100)
            if i is not None:
                py5.fill(i * 24, 200, 128 + 64 * (i % 2))
            with py5.begin_closed_shape():
                py5.stroke_weight(1 / self.S)
                py5.vertices(self.vs)
            py5.fill(self.color)
            py5.circle(*self.centroid, 1/4)
        
    def calc_area(self):
        vs = self.vs
        area = 0.0
        for (ax, ay), (bx, by) in zip(vs, vs[1:] + [vs[0]]):
            area += ax * by
            area -= bx * ay
        return abs(area) / 2.0

    def to_edges(self, vs=None):
        vs = vs or self.vs
        return frozenset(
            frozenset((v, vs[i-1]))
            for i, v in enumerate(vs)
                )

    def to_vertices(self, edges=None):
        edge_list = list(edges or self.edges)
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
    
    def calc_centroid(self):
        sample = self.vs[:2] + self.vs[-1:]
        xs, ys = tuple(zip(*sample))
        return sum(xs) / len(xs), sum(ys) / len(ys)
    
    @classmethod
    def grid(cls, n, m=None):
        cls.GRID = list(product(range(n), range(m or n)))
        py5.translate(cls.M, cls.M)
        py5.stroke(0)
        py5.stroke_weight(5)
        py5.points((x * cls.S, y * cls.S)
                   for x, y in cls.GRID)

    @classmethod
    def merge_regions(cls):
        els = cls.elements
        num_els = 0
        while num_els !=  len(els):
            num_els = len(els) 
            for a, b in combinations(els, 2):
                if (a in els and b in els and
                    a.isadjacent(b) and a.color == b.color):
                    c = a + b
                    els.remove(a)
                    els.remove(b)
                    els.add(c)


py5.run_sketch(block=False)
        
        





