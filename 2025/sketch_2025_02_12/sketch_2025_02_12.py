from itertools import product
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
import py5

dragged = None
mst_edges = []

def setup():
    py5.size(600, 600)
    py5.stroke_join(py5.ROUND)
    start()
    
def start():
    global nodes, mst_edges
    nodes = np.array(
        [(x + py5.random(-5, 5), y + py5.random(-25, 25))
         for i, (x, y) in enumerate(product(range(100, 501, 25), repeat=2))]
    )
    update_viz()

def calculate_mst(nodes):
    distances = pdist(nodes)
    dist_matrix = squareform(distances)
    mst = minimum_spanning_tree(dist_matrix)
    mst_dense = mst.toarray()
    rows, cols = np.nonzero(mst_dense)    
    mask = rows < cols
    edges = np.column_stack((rows[mask], cols[mask]))
    return edges

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

def nearest_neighbor_tsp(coordinates):
    distances = squareform(pdist(coordinates))
    unvisited = set(range(1, len(coordinates)))
    current = 0
    tour = [current]
    while unvisited:
        next_node = min(unvisited, key=lambda x: distances[current][x])
        current = next_node
        tour.append(current)
        unvisited.remove(current)
    return tour


def update_viz():
    # Update TSP
#     idxs = nearest_neighbor_tsp(nodes)
#     np.roll(idxs, len(idxs)//2)
#     nodes[:] = nodes[idxs]  
    idxs = two_opt_tsp(nodes)
    nodes[:] = nodes[idxs]
    
    
    # Update MST
#    mst_edges[:] = calculate_mst(nodes)

def draw():
    py5.fill(200, py5.random(16, 32))
    py5.rect(0, 0, py5.width, py5.height)


#     # MST edges
#     py5.no_fill()
#     py5.stroke(0, 0, 200, 16)
#     py5.stroke_weight(15)
#     py5.lines((nodes[i][0], nodes[i][1], nodes[j][0], nodes[j][1])
#           for i, j in mst_edges)
    # TSP tour
    py5.stroke(200, 100, 0, 100)
    py5.stroke_weight(10)
    py5.fill(255, 100)
    with py5.begin_closed_shape():
        py5.vertices(nodes)


    # Draw nodes
    py5.no_stroke()
    for x, y in nodes:
        py5.fill(0)
        if py5.dist(x, y, py5.mouse_x, py5.mouse_y) < 10:
            py5.fill(255, 0, 0)
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
    update_viz()

def key_pressed():
    if py5.key == ' ':
        py5.save_frame('###.png')
        start()

py5.run_sketch(block=False)