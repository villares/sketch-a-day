import py5
import networkx as nx

dragging = None

def setup():
    py5.size(600, 600)
    start()
    
def start():
    global nodes_dict, G, mst
    nodes_dict = {i: (py5.random_choice(range(100, 501, 25)),
                      py5.random_choice(range(100, 501, 25)))
                for i in range(50)}
    G = nx.complete_graph(list(nodes_dict.keys()))    
    nx.set_node_attributes(G, nodes_dict, 'pos')
    for a, b in G.edges():
        G[a][b]['weight'] = py5.dist(*nodes_dict[a], *nodes_dict[b])    
    
def predraw_update():
    global mst
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
        if py5.dist(x, y, py5.mouse_x, py5.mouse_y) < 10:
            py5.fill(255, 0, 0)
        py5.circle(x, y, 10)


def mouse_pressed():
    global dragged
    nodes_coords = nx.get_node_attributes(mst, 'pos')  #  {'node': (x,y)}
    for node, (x, y) in nodes_coords.items():
        if py5.dist(x, y, py5.mouse_x, py5.mouse_y) < 10:
            dragged = node
            break
    
def mouse_dragged():
    if dragged is not None:
        x, y = G.nodes[dragged]['pos']
        dx = py5.mouse_x - py5.pmouse_x
        dy = py5.mouse_y - py5.pmouse_y
        new_x, new_y = x + dx, y + dy
        G.nodes[dragged]['pos'] = new_x, new_y   
    # one could move this to mouse_released() if it is too slow...
    for neighbor in G.neighbors(dragged):
        neighbor_x, neighbor_y = G.nodes[neighbor]['pos']
        distance = py5.dist(new_x, new_y,neighbor_x, neighbor_y) 
        G[dragged][neighbor]['weight'] = distance 

def mouse_released():
    global dragged
    dragged = None

def key_pressed():
    py5.save_frame('###.png')
    start()
    
py5.run_sketch(block=False)
