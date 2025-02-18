from functools import partial

import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.spatial import ConvexHull
from scipy.spatial import Delaunay
import py5

dragged = None

def setup():
    global draw_handle
    py5.size(600, 600, py5.P3D)
    py5.stroke_join(py5.ROUND)
    #py5.hint(py5.ENABLE_DEPTH_SORT)
    py5.hint(py5.ENABLE_STROKE_PERSPECTIVE)
    start()
    handle_shape = hexahedron(10)
    draw_handle = partial(shape3D, handle_shape)
    
def start():
    global nodes, y_rotation
    nodes= np.array([(py5.random_choice(range(-200, 201, 100)),
                      py5.random_choice(range(-200, 201, 100)),
                      py5.random_choice(range(-200, 201, 100)))
                      for _ in range(20)])
    y_rotation = 0
    update_viz()


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
    to_tour = two_opt_tsp(nodes)

def draw():
    #py5.ortho()
    py5.background(200)
    py5.translate(py5.width / 2, py5.height / 2, -py5.height / 2)
    py5.rotate_y(py5.radians(y_rotation))
    py5.no_fill()


#     py5.stroke(255, 150)
#     py5.stroke_weight(2)
#     for ixs in tri.simplices:
#         with py5.begin_closed_shape():
#             py5.vertices(nodes[ixs])

    py5.stroke(0, 200, 200)
    py5.stroke_weight(6)
    with py5.begin_closed_shape():
            py5.vertices(nodes[to_tour])


    # nodes
    py5.no_stroke()
    for x, y, z in nodes:
        py5.fill(0)
        sx = py5.screen_x(x, y, z)
        sy = py5.screen_y(x, y, z) 
        if py5.dist(sx, sy, py5.mouse_x, py5.mouse_y) < 10:
            py5.fill(0, 255, 0)
        draw_handle(x, y, z)

def mouse_pressed():
    global dragged
    for i, (x, y, z) in enumerate(nodes):
        sx = py5.screen_x(x, y, z)
        sy = py5.screen_y(x, y, z) 
        if py5.dist(sx, sy, py5.mouse_x, py5.mouse_y) < 10:
            dragged = i
            break
    else:
        dragged = None

def mouse_dragged():    
    if dragged is not None:
        x, y, z = nodes[dragged]
        dx = py5.mouse_x - py5.pmouse_x
        dy = py5.mouse_y - py5.pmouse_y
        new_x, new_y = x + dx, y + dy
        nodes[dragged] = new_x, new_y, z
        # ho ho ho
        update_viz()

def mouse_released():
    global dragged
    dragged = None

def key_pressed():
    if py5.key == ' ':
        py5.save_frame('###.png')
        start()
        
        
def mouse_wheel(e):
    global y_rotation
    y_rotation += e.get_count() * 5

def shape3D(shp, x, y, z):
    with py5.push_matrix():
        py5.translate(x, y, z)
        py5.shape(shp)

def hexahedron(radius):
    a = radius / py5.sqrt(3)  # half the side
    vs = np.array([
        (-a, -a,  a), (-a,  a,  a), (a,  a,  a), (a, -a,  a),
        (-a, -a, -a), (-a,  a, -a), (a,  a, -a), (a, -a, -a),
        ])
    sequence = np.array([0, 1, 2, 3, 4, 5, 6, 7,
                         0, 1, 5, 4, 2, 3, 7, 6,
                         0, 4, 7, 3, 1, 5, 6, 2])
    cube = py5.create_shape()
    with cube.begin_shape(py5.QUADS):
        cube.vertices(vs[sequence])
    cube.disable_style()
    return cube



py5.run_sketch(block=False)