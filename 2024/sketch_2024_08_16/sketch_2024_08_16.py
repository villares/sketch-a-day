"""
Sketch inspired by code from https://networkx.org/documentation/stable/auto_examples/
"""
from functools import cache

import py5
from py5_tools import animated_gif

import networkx as nx

margin = 50
s = 100 # seed
G = nx.balanced_tree(4, 5)

def setup():
    global pos
    py5.size(800, 800)
    #pos = nx.spring_layout(G, dim=2, seed=s)
    #pos = nx.arf_layout(G, max_iter=10)
    #pos = nx.bfs_layout(G, 100)
    pos = nx.kamada_kawai_layout(G)
    pos = resize_layout(pos)
    #animated_gif('out.gif', frame_numbers=range(1, 361, 10), duration=0.2, optimize=False)
    
def draw():
#     py5.push_matrix()
    py5.translate(py5.width / 2, py5.height / 2)
#     py5.rotate_y(py5.radians(py5.frame_count))
    py5.background(200, 200, 150)
    py5.stroke(0)
    py5.stroke_weight(1)
    py5.lines(pos[a] + pos[b] for a, b in G.edges)  # draw edges
    py5.stroke(0, 0, 200)
    py5.stroke_weight(5)
    py5.points(pos[n] for n in G.nodes)  # draw nodes
#    py5.pop_matrix()
#     py5.fill(255)
#     py5.text_size(margin / 2)
#     py5.text(f'G = nx.balanced_tree(4, 5)\npos = nx.spring_layout(G, dim=3, seed={s})', margin, margin)

def resize_layout(pos):
    """ Resize the positions dict layout to screen a and center on origin. """
    # I should do this with numpy...
    layout = pos.copy()
    xs, ys = [], []
    for x, y in layout.values():
        xs.append(x)
        ys.append(y)
#         zs.append(z)
    min_x = min(xs)
    min_y = min(ys)
#     min_z = min(zs)
    max_x = max(xs) 
    max_y = max(ys)
#     max_z = max(zs)
    w, h = py5.width, py5.height
    for n, (x, y) in layout.items():
        nx = py5.remap(x, min_x, max_x, margin, w - margin)
        ny = py5.remap(y, min_y, max_y, margin, h - margin)
#         nz = py5.remap(z, min_z, max_z, margin, h - margin)
        layout[n] = nx - w / 2, ny - h / 2 #, nz - h / 2  
    return layout

py5.run_sketch(block=False)

# coords_normalized = (coords - np.min(coords)) / (np.max(coords) - np.min(coords))
# lerp_coords = (1 - t) * start_coords + t * end_coords
# lerp_coords = start_coords + (end_coords - start_coords) * t

