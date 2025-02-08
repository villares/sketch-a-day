import py5
import networkx as nx

def setup():
    py5.size(600, 600)
    start()
    
def start():
    global nodes_dict, G, mst
    nodes_dict = {i: (py5.random_choice(range(100, 501, 50)),
                      py5.random_choice(range(100, 501, 50)))
                for i in range(10)}
    G = nx.complete_graph(list(nodes_dict.keys()))    
    nx.set_node_attributes(G, nodes_dict, 'pos')
    for a, b in G.edges():
        G[a][b]['weight'] = py5.dist(*nodes_dict[a], *nodes_dict[b])    
    mst = nx.minimum_spanning_tree(G)
    
def draw():
    py5.background(200)

    py5.stroke(0)
    py5.stroke_weight(2)
    for a, b in mst.edges():
        xa, ya = mst.nodes[a]['pos']
        xb, yb = mst.nodes[b]['pos']
        py5.line(xa, ya, xb, yb)

    py5.no_stroke()
    nodes_coords = nx.get_node_attributes(mst, 'pos')  #  {'node': (x,y)}
    for node, (x, y) in nodes_coords.items():
        py5.fill(255)
        py5.circle(x, y, 10)
#         py5.fill(255, 0, 0)
#         py5.text(node, x + 10, y + 10)

def key_pressed():
    py5.save_frame('###.png')
    start()
    

py5.run_sketch(block=False)
