from itertools import product

import py5
import numpy as np

W = 50
N = 8

def setup():
    py5.size(600, 610)
    py5.no_fill()
    py5.text_font(py5.create_font('Inconsolata', 14))
    py5.text_size(14)
    py5.stroke_join(py5.ROUND)
    make_nodes()

def make_nodes():
    global nodes
    #nodes = np.random.randint(0, W, size=(N, 2))
    grid = list(product(range(5, W-5, 10), repeat=2))
    sample = py5.random_sample(range(len(grid)), N, replace=False)
    nodes = np.array(grid)[sample]

def draw():
    py5.no_loop()
    py5.background(180)
    paths = []
    for x, y in product(range(5, 600, 60), repeat=2):
        p = py5.random_permutation(range(N))
        d = path_distance(nodes[p])
        py5.stroke(255)
        py5.square(x, y, W)
        py5.text(d, x, y + W + 10)
        py5.stroke(0)
        with py5.push_matrix():
            py5.translate(x, y)
            with py5.begin_closed_shape():
                py5.vertices(nodes[p])
        paths.append((p, x, y, d))
        
def path_distance(p):
    p_shifted = np.roll(p, 1, axis=0)
    return np.sum(np.linalg.norm(p - p_shifted, axis=1))

def key_pressed():
    if py5.key == 's':
        py5.save_frame('out.png')
    elif py5.key == ' ':
        py5.redraw()
    elif py5.key == 'n':
        make_nodes()

py5.run_sketch(block=False)


