from itertools import product, permutations

import numpy as np
from scipy.spatial.distance import pdist, squareform
import py5

dragged = None
tsp = []
previous_solution = None

def setup():
    py5.size(600, 600)
    start()
    #py5.launch_repeating_thread(update_tsp, name='update_tsp', time_delay=1)    
    
def start():
    global nodes
    nodes = np.array(
        [(x + py5.random(-5, 5), y + py5.random(-25, 25))
         for i, (x, y) in enumerate(product(range(100, 501, 50), repeat=2))]
        )
    update_tsp()

def update_tsp():
    global total_distance
    idxs, total_distance = nearest_neighbor_tsp(nodes)
    nodes[:] = nodes[idxs]
        
def nearest_neighbor_tsp(coordinates):
    # pairwise distances between all points
    tour_distance = 0
    distances = squareform(pdist(coordinates))
    unvisited = set(range(1, len(coordinates)))
    current = 0
    tour = [current]
    while unvisited:
        next_node = min(unvisited, key=lambda x: distances[current][x])
        tour_distance += distances[current][next_node]
        current = next_node
        tour.append(current)
        unvisited.remove(current)
    return tour, tour_distance
   
         
def draw():
    py5.fill(200, py5.random(16, 32))
    py5.rect(0, 0, py5.width, py5.height)
     
    py5.no_fill()
    py5.stroke(0, 0, 100)
    with py5.begin_closed_shape():
        py5.vertices(nodes)

    py5.no_stroke()
    for x, y in nodes:
        py5.fill(0)
        if py5.dist(x, y, py5.mouse_x, py5.mouse_y) < 10:
            py5.fill(255, 0, 0)
        py5.circle(x, y, 10)

    py5.text_size(20)
    py5.text(total_distance, 10, 20)
    py5.window_title(str(py5.get_frame_rate()))

    
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
    update_tsp() # to use during dragg



def mouse_released():
    global dragged
    dragged = None
    #update_tsp()  # to use without the repeating...

def key_pressed():
    if py5.key == ' ':
        py5.save_frame('###.png')
        start()
    
py5.run_sketch(block=False)
