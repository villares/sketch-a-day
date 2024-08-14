"""
Sketch adapting code from https://networkx.org/documentation/stable/auto_examples/graphviz_layout/plot_circular_tree.html
Note: -"This example needs Graphviz and PyGraphviz"
      - Requires scipy

I had trouble at first pip installing graphviz and pygraphviz but managed
to install, via pacman, on Manjaro, python-graphviz and python-pygraphviz
and then installed in my local env with pip
"""
from functools import cache

import py5

import networkx as nx


margin = 50
G = nx.balanced_tree(4, 5)

def setup():
    global pos
    py5.size(800, 800, py5.P3D)
    pos = nx.spring_layout(G, dim=3, seed=100)
    #pos = nx.spiral_layout(G, dim=3)
    pos = resize_layout(pos)
    
def draw():
    py5.push_matrix()
    py5.translate(py5.width / 2, py5.height / 2, -py5.height / 2)
    py5.rotate_y(py5.mouse_x / 20)
    py5.background(200, 200, 150)
    py5.stroke(0)
    py5.stroke_weight(1)
    for a, b in G.edges:
        xa, ya, za = pos[a]
        xb, yb, zb = pos[b]
        py5.line(xa, ya, za, xb, yb, zb)
    py5.stroke(0, 0, 200)
    py5.stroke_weight(4)
    for n in G.nodes:
        py5.point(*pos[n])
    py5.pop_matrix()
    py5.fill(255)
    py5.text_size(margin / 2)
    py5.text('nx.spring_layout(G, dim=3, seed=1)', margin, margin)



def resize_layout(pos):
    """ Resize the positions dict layout to screen a and center on origin. """
    # I should do this with numpy...
    layout = pos.copy()
    xs, ys, zs = [], [], []
    for x, y, z in layout.values():
        xs.append(x)
        ys.append(y)
        zs.append(z)
    min_x = min(xs)
    min_y = min(ys)
    min_z = min(zs)
    max_x = max(xs) 
    max_y = max(ys)
    max_z = max(zs)
    w, h = py5.width, py5.height
    for n, (x, y, z) in layout.items():
        nx = py5.remap(x, min_x, max_x, margin, w - margin)
        ny = py5.remap(y, min_y, max_y, margin, h - margin)
        nz = py5.remap(z, min_z, max_z, margin, h - margin)
        layout[n] = nx - w / 2, ny - h / 2 , nz - h / 2  
    return layout

def key_pressed():
    global pos, a_mode
    if py5.key == ' ':
        a_mode = (a_mode + 1) % len(MODES)
        print(MODES[a_mode])
        pos = calc_layout(MODES[a_mode])
    elif py5.key == 'p':
        py5.save_frame(MODES[a_mode] + '.png')

py5.run_sketch(block=False)