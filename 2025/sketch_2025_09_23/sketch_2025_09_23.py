
from itertools import product, permutations
from pathlib import Path

import py5
from shapely import Polygon, Point, unary_union

data_file = 'tris.data'
N = 14 # columns
current_combo = 0

def setup():
    global combos, tris
    py5.size(14 * 60, 14 * 60)
    py5.color_mode(py5.HSB)
    py5.stroke_join(py5.ROUND)
    grid = list(product((-1, 0, 1), repeat=2))
    if Path(data_file).is_file():
        combos = py5.load_pickle(data_file)
        combos = [Combo(c._combo) for c in combos]
    else:
        combos = set() 
        for a, b, c, d, e, f, g, h, i in permutations(grid, 9):
           if not (t0 := Polygon((a, b, c))).area:
               continue
           if not (t1 := Polygon((d, e, f))).area:
               continue
           if not (t2 := Polygon((g, h, i))).area:
               continue
           combos.add(Combo((t0, t1, t2)))
        combos = sorted(combos)
        py5.save_pickle(combos, data_file)
    print(len(combos))
    clear_board()
#     board = combos[:10] + [Combo([Polygon((grid[0], grid[2], grid[4]))])]
#     board = {(r, c): combo for (r, c), combo in
#              zip(product(range(N), range(N)), combos + [Combo([Polygon()])]) }
    
def clear_board():
    global board
    board = {(r, c): Combo([Polygon()]) for r, c in product(range(N), range(N))}
    
def draw():
    py5.background(0)
    py5.fill(255, 200)
    s = py5.width / N
    w = s / 2
    for r in range(N):
        for c in range(N):
            x = s / 2 + s * c
            y = s / 2 + s * r
            if combo := board.get((r, c)):
                combo.draw(x, y, w)
            if py5.dist(py5.mouse_x, py5.mouse_y, x, y) < w:
                nbs = get_nbs(r, c)
                combos[current_combo].draw(x, y, w, nbs=nbs)
                if py5.is_mouse_pressed:
                    #print(combos[current_combo])
                    board[r, c] = combos[current_combo]
                    
def get_nbs(r, c):
    return {
        'LN': board.get((c - 1, r)),
        'RN': board.get((c + 1, r)),
        'TN': board.get((c, r - 1)),
        'BN': board.get((c, r + 1))
    }
 
class Combo:
    """
    a — b — c
    |       |
    d       e
    |       |
    f — g — h
    """
    ab = Point(-0.5, -1.0)
    bc = Point( 0.5, -1.0)
    ad = Point(-1.0, -0.5)
    df = Point(-1.0,  0.5)
    ce = Point( 1.0, -0.5)
    eh = Point( 1.0,  0.5)
    fg = Point(-0.5,  1.0)
    gh = Point( 0.5,  1.0)
    edge_pts = (ab, bc, ce, eh, gh, fg, df, ad)

    def __init__(self, combo):
        self._combo = combo
        self.area = sum(map(lambda p:p.area, combo))
        self.coords = frozenset(self.tri_coords(tri) for tri in combo)
        self.find_edges()
        
    def __repr__(self):
        return f'Combo({self._combo}) # {self.L} {self.R} {self.T} {self.B}'
        
    def find_edges(self):
        self.edges = {}
        union = unary_union(self._combo)
        for pt in self.edge_pts:
            self.edges[pt] =  pt.intersects(union)
        self.L = self.edges[self.ad], self.edges[self.df]
        self.R = self.edges[self.ce], self.edges[self.eh]
        self.T = self.edges[self.ab], self.edges[self.bc]
        self.B = self.edges[self.fg], self.edges[self.gh]
      
    def __bool__(self):
        return bool(self.area)
      
    def __len__(self):
        return len(self._combo)
    
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
    
    def __lt__(self, other):
        return self.area < other.area
        
    def __hash__(self):
        c = self.coords
        h = hash(c)
#         for _ in range(3):
#             c = self.rot_coords(c)
#             rh = hash(c)
#             h = min(h, rh)
        return h
    
    def check_nbs(self, nbs):
        if not nbs:
            return False    
        if (LN := nbs['LN']) and LN.R != self.L:
            return False
        if (RN := nbs['RN']) and RN.L != self.R:
            return False
        if (TN := nbs['TN']) and TN.B != self.T:
            return False
        if (BN := nbs['BN']) and BN.T != self.B:
            return False        
        return True
    
    def draw(self, x, y, w, nbs=None):            
        with py5.push_matrix():
            py5.translate(x, y)
            py5.scale(w)
            py5.stroke_weight(1 / w)
            for poly in self._combo:
                py5.fill(255, 100)
                py5.shape(py5.convert_cached_shape(poly))
            py5.stroke_weight(6 / w)
            for pt in self.edge_pts:
                edge_present =  self.edges[pt]
                py5.stroke(100 * edge_present, 255, 255)
                py5.shape(pt)
            if not self.check_nbs(nbs):
                py5.stroke('orange')
                py5.shape(Point(0, 0))




    @staticmethod
    def tri_coords(tri):
        return frozenset((x, y) for x, y in tri.exterior.coords[:3])

    @staticmethod
    def rot_coords(coords):
        return frozenset(frozenset((-y, x) for x, y in c)
                         for c in coords)

def key_pressed():
    if py5.key == 's':
        py5.save('out.png')
    elif py5.key == 'c':
        clear_board()

def mouse_wheel(e):
    global current_combo
    current_combo = (current_combo + e.get_count()) % len(combos)
    print(current_combo)

py5.run_sketch(block=False)
