from itertools import product, combinations
from pathlib import Path

import py5
from shapely import Polygon

def setup():
    global combos, tris, good_pairs, nonoverlapping
    py5.size(83 * 22, 9 * 22)
    py5.color_mode(py5.HSB)
    py5.stroke_join(py5.ROUND)
    grid = list(product((-1, 0, 1), repeat=2))
    tris = [Polygon(t) for t in combinations(grid, 3) if Polygon(t).area]
    # get all the 23903 nonoverlapping combinations of triangles
    # some will fill the grid, others will have gaps, I'll filter later
    if Path(f'nonoverlapping.data').is_file():
        nonoverlapping = py5.load_pickle(f'nonoverlapping.data')
    else:
        m = py5.millis()
        nonoverlapping_pairs = [(a, b) for a, b in combinations(tris, 2)
          if not (a.overlaps(b)
          or a.contains(b)
          or b.contains(a))
          ]
        good_pairs = set(nonoverlapping_pairs)
        good_pairs.update((b, a) for a, b in nonoverlapping_pairs)
        nonoverlapping = set(nonoverlapping_pairs)
        starter = nonoverlapping_pairs
        for i in range(6):
            new_combos = []
            for combo in starter:
                for tri in tris:
                    for item in combo:
                        if (tri, item) not in good_pairs:
                            break
                    else:
                        new_combo = combo + (tri,)
                        nonoverlapping.add(frozenset(new_combo))            
                        new_combos.append(new_combo)
            starter = new_combos
        py5.save_pickle(nonoverlapping, f'nonoverlapping.data')
        print(f'{len(nonoverlapping)} nonoverlapping combos {py5.millis()-m}')
    # Filter out combinations that do not fill the entire grid
    combos = [combo for combo in nonoverlapping
              if sum(map(lambda p:p.area, combo)) == 4]
    combos.sort(key=len) # sort by number of triangles
    print(len(combos))  # 747
    
def draw():
    py5.background(0)
    py5.fill(255, 200)
    N = 83 # columns
    i = 0 # py5.frame_count * N * N
    s = py5.width / N
    w = s / 2 - 1
    for r in range(N):
        for c in range(N):
            x = s / 2 + s * c
            y = s / 2 + s * r
            draw_combo(i, x, y, w)
            i += 1
            
def draw_combo(ci, x, y, w):
    if ci < len(combos): 
        with py5.push_matrix():
            py5.translate(x, y)
            py5.scale(w)
            py5.stroke_weight(0.5 / w)
            combo = combos[ci]
            for poly in combo:
                py5.fill(poly.area * 100, 250, 200)
                py5.shape(py5.convert_cached_shape(poly))

def key_pressed():
    py5.save('out.png')

py5.run_sketch(block=False)

