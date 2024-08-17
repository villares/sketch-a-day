"""
Sketch inspired by code from https://networkx.org/documentation/stable/auto_examples/
"""
from functools import cache

import py5
from py5_tools import animated_gif
import numpy as np
import networkx as nx

margin = 50
s = 100 # seed
G = nx.balanced_tree(4, 5)
t = 0.5

def setup():
    global pos0, pos1
    py5.size(800, 800)
    pos0 = nx.spring_layout(G, dim=2, seed=s)
    pos1 = nx.spring_layout(G, dim=2, seed=s+1)

    pos0 = resize_layout(pos0)
    pos1 = resize_layout(pos1)

    #animated_gif('out.gif', frame_numbers=range(1, 361, 10), duration=0.2, optimize=False)
    
def draw():
    py5.translate(py5.width / 2, py5.height / 2)
    pos = pos0 + (pos1 - pos0) * t
    py5.background(200, 200, 150)
    py5.stroke(0)
    py5.stroke_weight(1)
    py5.lines(np.concatenate((pos[a], pos[b])) for a, b in G.edges)  # draw edges
    py5.stroke(0, 0, 200)
    py5.stroke_weight(5)
    py5.points(pos[n] for n in G.nodes)  # draw nodes

def resize_layout(pos):
    """ Resize the positions dict layout to screen a and center on origin. """
    coords = np.array(list(pos.values()))
    coords_normalized = (coords - np.min(coords)) / (np.max(coords) - np.min(coords))
    return coords_normalized * (py5.height - margin * 2) + np.array([margin - py5.height / 2 ,
                                                                     margin - py5.height / 2])


def key_pressed():
    global t
    if py5.key_code == py5.UP:
        t += 0.1
    elif py5.key_code == py5.DOWN:
        t -= 0.1
    if py5.key == 's':
        py5.save_frame('####.png')
        

py5.run_sketch(block=False)

# coords_normalized = (coords - np.min(coords)) / (np.max(coords) - np.min(coords))
# lerp_coords = (1 - t) * start_coords + t * end_coords
# lerp_coords = start_coords + (end_coords - start_coords) * t

