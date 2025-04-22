from fractions import Fraction

import py5
import numpy as np

grid = {}
quads = []
margin = 50
N = 16

def setup():
    py5.size(700, 700)
    calc_grid()

def draw():
    py5.background(0)
    py5.stroke_weight(1)
    for q in quads.copy():
        vs = np.array(tuple(grid[vi] for vi in q))
        py5.random_seed(abs(hash(q)))
        py5.fill(0, 128, py5.random(255))
        with py5.begin_closed_shape(): 
            py5.vertices(vs)
            
        if poly_area(vs) > (cell_size ** 2) * 4:
             quads.remove(q)
             split_quad(q)
            
    py5.stroke_weight(5)
    py5.points(tuple(grid.values()))

def calc_grid():
    global cell_size
    cell_size = (py5.width - margin * 2) / N
    quads.clear()
    grid.clear()
    for i in range(N):
        x = margin + i * cell_size + cell_size / 2 
        for j in range(N):
            y = margin + j * cell_size + cell_size / 2
            grid[(i, j)] = np.array([x, y])
            if i > 0 and j > 0:
                quads.append((
                    (i-1, j-1), (i, j-1),
                    (i, j), (i-1, j)
                ))


def point_inside_poly(x, y, poly):
    # ray-casting algorithm based on
    # https://wrf.ecse.rpi.edu/Research/Short_Notes/pnpoly.html
    inside = False
    for i, p in enumerate(poly):
        pp = poly[i - 1]
        xi, yi = p
        xj, yj = pp
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
    return inside


def split_quad(quad):
    ai, bi, ci, di = quad
    av, bv, cv, dv = (grid[i] for i in quad)
    mi = average_tuples(ai, bi, ci, di)
    mv = (av + bv + cv + dv) / 4
    grid[mi] = mv
    abi = average_tuples(ai, bi)
    bci = average_tuples(bi, ci)
    cdi = average_tuples(ci, di)
    dai = average_tuples(di, ai)
    abv = (av + bv) / 2
    bcv = (bv + cv) / 2
    cdv = (cv + dv) / 2
    dav = (dv + av) / 2
    grid[abi] = abv
    grid[bci] = bcv
    grid[cdi] = cdv
    grid[dai] = dav
    quads.extend((
        (ai, abi, mi, dai),
        (bi, bci, mi, abi),
        (ci, cdi, mi, bci),
        (di, dai, mi, cdi)
        ))
        
def average_tuples(*args):
    xs, ys = zip(*args)
    return Fraction(sum(xs), len(args)), Fraction(sum(ys), len(args))
     
def poly_area(pts):
    ptsa = np.asarray(pts)
    xs = ptsa[:, 0]
    ys = ptsa[:, 1]
    return 0.5 * np.abs(np.dot(xs, np.roll(ys, 1)) - np.dot(ys, np.roll(xs, 1)))
    
def mouse_dragged():
    mouse_vector = np.array([py5.mouse_x, py5.mouse_y]) 
    grid_positions = np.array(list(grid.values()))
    d = grid_positions - mouse_vector # note the "broadcasting"
    d_mag = np.linalg.norm(d, axis=1, keepdims=True)
    d_scaled = d * (1 / (1 + d_mag))
    for i, vi in enumerate(grid.keys()):
        grid[vi] += d_scaled[i]

def mouse_clicked():
    for q in quads.copy():
        vs = tuple(grid[v] for v in q)
        if point_inside_poly(py5.mouse_x, py5.mouse_y, vs):
            split_quad(q)
            quads.remove(q)  # Remove the original quad
            break

def key_pressed():
    calc_grid()

py5.run_sketch(block=False)
               