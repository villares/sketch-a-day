from itertools import product, combinations
from functools import cache
from random import sample

from shapely import LineString, line_merge, unary_union, MultiLineString

MARGIN = 64
SPACING = 64
N = 128

def setup():
    global grid, pairs
    size(512+128, 512+128)
    no_stroke()
    grid = list(product(range(MARGIN, width, SPACING), repeat=2))
    print(len(grid))
    pairs = [(a, b) for a, b in list(combinations(grid, 2))
             if dist(*a, *b) <= 1.5 * SPACING]
    start()
    
def start():
    global config
    config = tuple(sample(pairs, N))

def draw():
    background(0)
    merged_lines = cached_merge(config)
    for i in range(12, -1, -1):
        fill(255 if i % 2 else 0)
        shp = convert_cached_shape(
            merged_lines
            #.buffer(1,quad_segs=0)
            .buffer(2 + i * 4,
                         cap_style='round',
                         join_style='mitre',
                         quad_segs=2,
                         )
            )
        shape(shp, 0, 0)
        
@cache
def cached_merge(ls):
    return MultiLineString([LineString((a, b)) for a, b in ls])

 

def key_pressed():
    if key == 's':
        save_frame('#####.png')
    else:
        start()
 

def lerp_along_points(amt, pts):
    # Based on LerpVectorsExample by Jeremy Douglass
    amt = constrain(amt, 0, 1)  # let's play safe
    if len(pts) == 1:
        return pts[0]
    cunit = 1.0 / (len(pts) - 1)
    return lerp(pts[floor(amt / cunit)],
                pts[ceil(amt / cunit)],
                amt % cunit / cunit)

