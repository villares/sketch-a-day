from fractions import Fraction

import py5
import numpy as np

grid = {}
regions = []
margin = 50
N = 16

def setup():
    py5.size(700, 700)
    calc_grid()

def draw():
    py5.background(0)
    py5.stroke_weight(1)
    for region in regions.copy():
        vs = np.array(tuple(grid[vi] for vi in region))
        py5.random_seed(abs(hash(region)))
        py5.fill(0, 128, py5.random(255))
        with py5.begin_closed_shape(): 
            py5.vertices(vs)
            
        if poly_area(vs) > (cell_size ** 2) * 4:
             regions.remove(region)
             split_region(region)
            
    py5.stroke_weight(5)
    py5.points(tuple(grid.values()))

def calc_grid():
    global cell_size
    cell_size = (py5.width - margin * 2) / N
    regions.clear()
    grid.clear()
    for i in range(N):
        x = margin + i * cell_size + cell_size / 2 
        for j in range(N):
            y = margin + j * cell_size + cell_size / 2
            grid[(i, j)] = np.array([x, y])
            if i > 0 and j > 0:
                a = (i-1, j-1)
                b = (i, j-1)
                c = (i, j)
                d = (i-1, j)
                # sub_quad() returns quad with mid-points of edges
                # there are new vertices added to grid as a side effect!
                regions.append(sub_quad(a, b, c, d))


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

def sub_quad(ai, bi, ci, di):
    av, bv, cv, dv = (grid[i] for i in (ai, bi, ci, di))
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
    return (ai, abi, bi, bci, ci, cdi, di, dai)

def split_region(region):
    ai, abi, bi, bci, ci, cdi, di, dai = region
    av, abv, bv, bcv, cv, cdv, dv, dav = (grid[i] for i in region)
    mi = average_tuples(*region) #(ai, bi, ci, di)
    mv = sum((av, abv, bv, bcv, cv, cdv, dv, dav)) / 8 #(av + bv + cv + dv) / 4
    grid[mi] = mv
    regions.extend((
        sub_quad(ai, abi, mi, dai),
        sub_quad(bi, bci, mi, abi),
        sub_quad(ci, cdi, mi, bci),
        sub_quad(di, dai, mi, cdi)
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
    added_mag = np.linalg.norm(d, axis=1, keepdims=True) + 0.1 # adding to avoid zero division
    displacement = d * (1 / added_mag)
    for i, vi in enumerate(grid.keys()):
        grid[vi] += displacement[i]

def mouse_clicked():
    for q in regions.copy():
        vs = tuple(grid[v] for v in q)
        if point_inside_poly(py5.mouse_x, py5.mouse_y, vs):
            split_region(q)
            regions.remove(q)  # Remove the original region
            break

def key_pressed():
    calc_grid()

py5.run_sketch(block=False)
               