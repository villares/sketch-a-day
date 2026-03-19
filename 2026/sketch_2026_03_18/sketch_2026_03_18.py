# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

from itertools import combinations, product
from collections import Counter

import py5
from shapely import Polygon

W = 20  # combo width
M = 20  # spacing
COLS = 23
ROWS = 14
vs = Counter()


def setup():
    py5.size((W + M) * COLS + M, (W + M) * ROWS + M)
    py5.color_mode(py5.CMAP, 'tab20b', py5.dist(W, W, 0, 0))
    py5.stroke_weight(3)
    generate_combos()


def draw():
    py5.background('black')
    x = 0
    y = 0
    for combo in combos:
        with py5.push_matrix():
            py5.translate(M + x + W / 2, M + y + W / 2)
            for i, ((xa, ya), (xb, yb)) in enumerate(combo):
                py5.stroke(py5.dist(xa, ya, xb, yb))
                py5.line(xa, ya, xb, yb)
        x += W + M
        if x > py5.width - W - M:
            x = 0
            y += W + M


def key_pressed():
    py5.save_frame('###.png')


def generate_combos():
    global combos
    grid = list(product((-W / 2, 0, W / 2), repeat=2))  # the 3x3 grid
    pairs = list(combinations(grid, 2))  # all possible segments
    N = 3
    all_combos = list(combinations(pairs, N))  # all N-segment combos
    combos = {
        Combo(combo) for combo in all_combos
        if good_combo(combo)  # connected but not aligned
    }
    combos = sorted(combos, key=sum_seg_len)
    print(len(all_combos), len(combos))  # 7140 322


def good_combo(combo):
    vs.clear()
    for seg in combo:
        vs.update(seg)
    v_count = vs.most_common()
    if v_count[0][1] > 1:
        return False  # connected
#     if v_count[-3][1] == 1:
#         return False  # not all connected
#     for va, vb in combo:
#         if vs[va] + vs[vb] == 2:
#             return False  # isolated segment
#     for sa, sb in combinations(combo, 2):
#         if not valid_segments(sa, sb):
#             return False  # neither disjoint nor validly connected
    return True


def valid_segments(a, b):
    unique_vs = set(a) | set(b)
    if len(unique_vs) == 4:
        return True
    return Polygon(unique_vs).area != 0


def sum_seg_len(combo):
    return sum(py5.dist(xa, ya, xb, yb) for (xa, ya), (xb, yb) in combo)


class Combo:
    
    def __init__(self, segs):
        self.segs = frozenset(
            frozenset(seg) for seg in segs
        )
        
    def __iter__(self):
        return iter(self.segs)
        
    def __eq__(self, other):
        return hash(self) == hash(other)
    
    def __hash__(self):
        segs = self.segs
        h = hash(segs)
        for i in range(3):
            segs = frozenset(
                frozenset((y, -x) for x, y in seg) for seg in segs)  
            h = min(h, hash(segs))
        return h
          
       
py5.run_sketch(block=False)

    




