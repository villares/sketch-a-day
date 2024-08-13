"""
Sketch adapting code from https://networkx.org/documentation/stable/auto_examples/graphviz_layout/plot_circular_tree.html
Note: "This example needs Graphviz and PyGraphviz"

I had trouble at first pip installing graphviz and pygraphviz but managed
to install, via pacman, on Manjaro, python-graphviz and python-pygraphviz
and then installed in my local env with pip
"""
import py5

import networkx as nx


G = nx.balanced_tree(3, 5)
pos = nx.nx_agraph.graphviz_layout(G, prog="twopi", args="")
def setup():
    py5.size(800, 750)
    
def draw():
    py5.background(200, 200, 150)
    for a, b in G.edges:
        xa, ya = pos[a]
        xb, yb = pos[b]
        py5.line(xa, ya, xb, yb)
    py5.fill(0, 0, 200)
    for n in G.nodes:
        py5.circle(*pos[n], 4)

py5.run_sketch(block=False)