"""
Sketch adapting code from https://networkx.org/documentation/stable/auto_examples/graphviz_layout/plot_circular_tree.html
Note: "This example needs Graphviz and PyGraphviz"

I had trouble at first pip installing graphviz and pygraphviz but managed
to install, via pacman, on Manjaro, python-graphviz and python-pygraphviz
and then installed in my local env with pip
"""
from functools import cache

import py5

import networkx as nx

# tred acyclic osage ccomps gvcolor gc nop
# gvpr unflatten sccmap - probably need arguments I don't understand
MODES = ('patchwork neato circo dot twopi sfdp fdp').split()
a_mode = 0
margin = 50
G = nx.balanced_tree(3, 5)

def setup():
    global pos
    py5.size(800, 800)
    pos = calc_layout(MODES[a_mode])

def draw():
    py5.background(200, 200, 150)
    py5.fill(255)
    py5.text_size(margin / 3)
    py5.text(MODES[a_mode], margin, margin / 2)
    py5.stroke(0)
    for a, b in G.edges:
        xa, ya = pos[a]
        xb, yb = pos[b]
        py5.line(xa, ya, xb, yb)
    py5.fill(0, 0, 200)
    py5.no_stroke()
    for n in G.nodes:
        py5.circle(*pos[n], 5)
        
@cache
def calc_layout(mode):
    import networkx as nx
    layout = nx.nx_agraph.graphviz_layout(G, prog=mode, args="")
    xs, ys = [], []
    for x, y in layout.values():
        xs.append(x)
        ys.append(y)
    min_x = min(xs)
    min_y = min(ys)
    max_x = max(xs) 
    max_y = max(ys)
    for n, (x, y) in layout.items():
        nx = py5.remap(x, min_x, max_x, margin, py5.width - margin)
        ny = py5.remap(y, min_y, max_y, margin, py5.height - margin)
        layout[n] = nx, ny
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