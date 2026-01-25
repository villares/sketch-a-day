
from itertools import product

import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
import py5
import shapely

MARGIN = 50
N = 24
R = 10
dragged = None
results = []
edit = True
nodes = []

def setup():
    py5.size(600, 600)
    py5.stroke_join(py5.ROUND)
    py5.blend_mode(py5.MULTIPLY)
    
def start():
    global nodes, mst_edges
    w = (py5.width - MARGIN * 2) / N
    xs = [w / 2 + MARGIN + i * w + py5.random(-1, 1) * R
           for i in range(N)]
    ys = [w / 2 + MARGIN + i * w + py5.random(-1, 1) * R
       for i in range(N)]
    nodes = np.array(tuple(product(xs, ys)))
    update_tsp()

def path_distance(route, nodes):
    coords = nodes[route]
    coords_shifted = np.roll(coords, 1, axis=0)
    return np.sum(np.linalg.norm(coords - coords_shifted, axis=1))

def two_opt_swap(route, i, k):
    return np.concatenate((route[:i], route[k:i-1:-1], route[k+1:]))

def two_opt_tsp(nodes, improvement_threshold=0.3):
    route = np.arange(nodes.shape[0])
    improvement_factor = 1
    best_distance = path_distance(route, nodes)
    while improvement_factor > improvement_threshold:
        distance_to_beat = best_distance
        for swap_first in range(1, len(route)-2):
            for swap_last in range(swap_first+1, len(route)):
                new_route = two_opt_swap(route, swap_first, swap_last)
                new_distance = path_distance(new_route, nodes)
                if new_distance < best_distance:
                    route = new_route
                    best_distance = new_distance
        improvement_factor = 1 - best_distance / distance_to_beat
    return route

def update_tsp():
    # Update TSP
    idxs = two_opt_tsp(nodes)
    nodes[:] = nodes[idxs]
    

def draw():
    py5.background(200)
    # TSP tour
    if edit:
        py5.stroke(255)
        py5.stroke_weight(2)
        py5.no_fill()
        with py5.begin_closed_shape():
            py5.vertices(nodes)
    py5.fill(255, 32)
    py5.no_stroke()
    for c, vs in zip((
        py5.color(255, 0, 0),
        py5.color(0, 255, 0),
        py5.color(0, 0, 255),
        ), results):
        py5.fill(c, 128)
        with py5.begin_closed_shape():
            py5.vertices(vs)
    
    # Draw nodes
    py5.no_stroke()
    for x, y in nodes:
        if py5.dist(x, y, py5.mouse_x, py5.mouse_y) < 10:
            py5.fill(0, 255, 0)
            py5.circle(x, y, 10)

def mouse_dragged():
    global dragged
    for i, (x, y) in enumerate(nodes):
        if py5.dist(x, y, py5.mouse_x, py5.mouse_y) < 10:
            dragged = i
            break
    else:
        dragged = None
    
    if dragged is not None:
        x, y = nodes[dragged]
        dx = py5.mouse_x - py5.pmouse_x
        dy = py5.mouse_y - py5.pmouse_y
        new_x, new_y = x + dx, y + dy
        nodes[dragged] = new_x, new_y

def mouse_released():
    global dragged
    dragged = None
    update_tsp()

def key_pressed():
    global edit
    if py5.key == 's':
        py5.save_frame('###.png')
    elif py5.key == 'a' and nodes != []:
        results.append(nodes)
    elif py5.key == 'c':
        start()
        update_tsp()
        update_tsp()
        update_tsp()
    elif py5.key == 'e':
        edit = not edit
    elif py5.key == 'u' and nodes != []:
        update_tsp()
    elif py5.key == 'S':
        py5.save_pickle(results, 'out.pickle')
        py5.print('saved.')
    elif py5.key == 'L':
        results[:] = py5.load_pickle('out.pickle')
        print('loaded.')
        
        
py5.run_sketch(block=False)
