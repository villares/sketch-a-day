"""
Sketch inspired by code from https://networkx.org/documentation/stable/auto_examples/
"""
from functools import cache

import py5
from py5_tools import animated_gif
import numpy as np
import networkx as nx

G = nx.balanced_tree(3, 5)

def setup():
    global pos0, pos1
    py5.size(800, 800)
    # patchwork neato circo dot twopi sfdp fdp
    pos0 = nx.nx_agraph.graphviz_layout(G, prog='twopi', args="")
    pos1 = nx.nx_agraph.graphviz_layout(G, prog='fdp', args="")
    pos0 = resize_layout(pos0, py5.height)
    pos1 = resize_layout(pos1, py5.height) * np.array([-1, 1])
    #animated_gif('out.gif', frame_numbers=range(1, 361, 18), duration=0.2, optimize=False)
    
def draw():
    py5.translate(py5.width / 2, py5.height / 2)
    t = 0.5 + 0.5 * np.sin(py5.radians(py5.frame_count))
    pos = pos0 + (pos1 - pos0) * t  # lerp
    py5.background(200, 200, 150)
    py5.stroke(0)
    py5.stroke_weight(1)
    py5.lines(np.concatenate((pos[a], pos[b])) for a, b in G.edges)  # draw edges
    py5.stroke(0, 0, 200)
    py5.stroke_weight(5)
    py5.points(pos[n] for n in G.nodes)  # draw nodes

def resize_layout(pos, ext, margin=50):
    """ Resize the positions dict layout to screen a and center on origin. """
    coords = np.array(list(pos.values()))
    coords_normalized = (coords - np.min(coords)) / (np.max(coords) - np.min(coords))
    return coords_normalized * (ext - margin * 2) + np.array([margin - ext / 2 , margin - ext / 2])
        
py5.run_sketch(block=False)
