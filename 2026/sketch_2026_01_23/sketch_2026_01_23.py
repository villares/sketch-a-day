
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

def setup():
    py5.size(600, 600)
    py5.stroke_join(py5.ROUND)
    start()
    
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

def two_opt_tsp(nodes, improvement_threshold=0.2):
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
    global c_nodes
    py5.fill(0, py5.random(16, 32))
    py5.rect(0, 0, py5.width, py5.height)
    # TSP tour
    if edit:
        py5.stroke(255)
        py5.stroke_weight(2)
        py5.no_fill()
        c_nodes = list(nodes[-2:]) + list(nodes) + list(nodes[:2])
        with py5.begin_closed_shape():
            py5.curve_vertices(c_nodes)
    py5.fill(255, 32)
    py5.no_stroke()
    for cvs in results:    
        with py5.begin_closed_shape():
            py5.curve_vertices(cvs)
    
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
    elif py5.key == 'n':
        results.append(c_nodes)
        start()
    elif py5.key == 'e':
        edit = not edit
    elif py5.key == 'u':
        update_tsp()
        
py5.run_sketch(block=False)
