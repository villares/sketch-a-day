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