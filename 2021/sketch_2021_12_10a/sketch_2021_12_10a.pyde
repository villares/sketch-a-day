# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need Processing 3.5.4 + Python mode, instructions at: 
# https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/index-EN.html

"""
Combinations of 3 triangles on hexagon vertices (removing equivalent rotations): 192
"""

from itertools import product, combinations, permutations

space, border = 50, 50

def setup():
    size(100 + 16 * 50, 100 + 12* 50)
    global hex_coords
    hex_coords = calc_hex_points(0, 0, 1)
    points = list(range(6)) # an index to the hex_coords list...
    triangles = list(combinations(points, 3))
    tri_combos = set(map(TriCombo, combinations(triangles, 3)))
    tri_combos = sorted(tri_combos,
                        key=lambda c: sum(map(tri_on_hex_area, c)),
                        reverse=True
                        )
    W = (width - border * 2) // space
    H = (height - border * 2) // space
    println("Number of triangle combinations: {}".format(len(tri_combos)))
    println("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))
    
    background(200)
    for y in range(H):
        for x in range(W):
            if len(tri_combos):
                pushMatrix()
                translate(border / 2 + space + space * x,
                          border / 2 + space + space * y)
                tri_combos.pop().draw()
                popMatrix()

    saveFrame('combos.png')

def calc_hex_points(x, y, radius):
    return [(x + radius * cos(PI / 180 * 60 * i),
             y + radius * sin(PI / 180 * 60 * i))
            for i in range(6)]    
    
def tri_on_hex_area(t):
    """
    From a collection of 3 hexagon points represented as integers,
    get the coordinates and calculate the triangle area.
    """
    a, b, c = t
    ax, ay = hex_coords[a]
    bx, by = hex_coords[b]
    cx, cy = hex_coords[c]
    return abs(bx * (cy - ay) +
              cx * (ay - by) +
              ax * (by - cy))
                
class TriCombo:

    colors = (
        color(0, 200, 0),
        color(0, 0, 200, 128),
        color(200, 0,0, 128),
        )
    
    def __init__(self, triangles):
        self.triangles = tuple(sorted(tuple(sorted(tri)) for tri in triangles))
    
    def __getitem__(self, i):
        return self.triangles[i]
    
    def __iter__(self):
        return iter(self.triangles)
    
    def draw(self):
        noStroke()
        strokeJoin(ROUND)    
        siz = space / 2.5
        for tri, c in zip(self.triangles, self.colors):
            fill(c)
            p0, p1, p2 = tri
            (x0, y0) = hex_coords[p0]
            (x1, y1) = hex_coords[p1]
            (x2, y2) = hex_coords[p2]
            triangle(x0 * siz, y0 * siz,
                    x1 * siz, y1 * siz,
                    x2 * siz, y2 * siz)
            
    def __eq__(self, other):
        return hash(self) == hash(other)
            
    def __hash__(self):
        r = self
        h = hash(self.triangles)        
        for _ in range(5):
            r = r.rotated()
            rh = hash(r.triangles)
            h = min(h, rh)
        return h
    
    def rotated(self):
        return TriCombo(((a + 1) % 6, (b + 1) % 6, (c + 1) % 6)
                        for a, b, c in self)
