import numpy as np

from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.spatial import ConvexHull
from scipy.spatial import Delaunay


import py5

dragged = None

def setup():
    py5.size(600, 600)
    py5.stroke_join(py5.ROUND)
    start()
    
def start():
    global nodes
    nodes= np.array([(py5.random(100, 500),
                     py5.random(100, 500))
                      for _ in range(15)])
    update_viz()

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
    return np.array(tour)


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


def update_viz():
    global nn_tour, to_tour, tri
    tri = Delaunay(nodes)
    nn_tour = nearest_neighbor_tsp(nodes)
    to_tour = two_opt_tsp(nodes)

def draw():
    py5.background(200)
    py5.no_fill()


            
    py5.stroke(200, 0, 200, 50)
    py5.stroke_weight(12)
    with py5.begin_closed_shape():
            py5.vertices(nodes[nn_tour])
    py5.stroke(0, 200, 200)
    py5.stroke_weight(6)
    with py5.begin_closed_shape():
            py5.vertices(nodes[to_tour])

    py5.stroke(255, 150)
    py5.stroke_weight(2)
    for ixs in tri.simplices:
        with py5.begin_closed_shape():
            py5.vertices(nodes[ixs])

    # nodes
    py5.no_stroke()
    for x, y in nodes:
        py5.fill(0)
        if py5.dist(x, y, py5.mouse_x, py5.mouse_y) < 10:
            py5.fill(255, 255, 0)
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
        # ho ho ho
        update_viz()

def mouse_released():
    global dragged
    dragged = None

def key_pressed():
    if py5.key == ' ':
        py5.save_frame('###.png')
        start()

py5.run_sketch(block=False)