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

G = nx.balanced_tree(3, 5)

def setup():
    global pos
    py5.size(800, 750)
    pos = calc_layout(MODES[a_mode])

def draw():
    py5.background(200, 200, 150)
    for a, b in G.edges:
        xa, ya = pos[a]
        xb, yb = pos[b]
        py5.line(xa, ya, xb, yb)
    py5.fill(0, 0, 200)
    for n in G.nodes:
        py5.circle(*pos[n], 4)
        
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
    dx = max(xs) - min_x
    dy = max(ys) - min_y
    scale_factor = 1
    if dx > py5.width:
        scale_factor = py5.width / dx
    elif dx < py5.width:
        scale_factor = dx / py5.width
    if dy * scale_factor > py5.height:
         scale_factor = py5.height / (dy * scale_factor)
    for n, (nx, ny) in layout.items():
        layout[n] = (nx - min_x) * scale_factor , (ny - min_y) * scale_factor
    return layout


def key_pressed():
    global pos, a_mode
    a_mode = (a_mode + 1) % len(MODES)
    print(MODES[a_mode])
    pos = calc_layout(MODES[a_mode])

py5.run_sketch(block=False)