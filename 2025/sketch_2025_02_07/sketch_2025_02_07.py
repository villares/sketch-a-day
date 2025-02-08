from itertools import combinations

import py5
import networkx as nx

def setup():
    py5.size(600, 600)
    start()
    
def start():
    global nodes, edges, G, minimum_edges
    nodes = {i: (py5.random_choice(range(100, 501, 50)),
                 py5.random_choice(range(100, 501, 50)))
                for i in range(10)}
    edges = list(combinations(nodes, 2))
    G = weighted_graph(nodes, edges) 
    mst = nx.minimum_spanning_tree(G)
    #nodes_coords = nx.get_node_attributes(mst, 'pos')  #  {'node': (x,y)}
    minimum_edges = list(mst.edges())  # [(node1, node2), ...]
    

def draw():
    py5.background(200)

    py5.stroke(0)
    py5.stroke_weight(2)
    for a, b in minimum_edges:
        xa, ya = nodes[a]
        xb, yb = nodes[b]
        py5.line(xa, ya, xb, yb)

    py5.fill(255)
    py5.no_stroke()
    for nome, (x, y) in nodes.items():
        py5.circle(x, y, 10)
        #py5.text(nome, x + 5, y)


def key_pressed():
    py5.save_frame('###.png')
    start()
    

def weighted_graph(nodes_dict, edges_list):
    G = nx.Graph()    
    for node, coords in nodes_dict.items():
        G.add_node(node, pos=coords)   
    for node1, node2 in edges_list:
        weight = py5.dist(*nodes_dict[node1], *nodes_dict[node2])
        G.add_edge(node1, node2, weight=weight)
    return G

py5.run_sketch(block=False)
