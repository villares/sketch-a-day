from itertools import product

import py5
import networkx as nx

dragged = None
tsp = []
previous_solution = None

def setup():
    py5.size(600, 600)
    start()
    py5.launch_repeating_thread(update_tsp, name='update_tsp', time_delay=1)    
    
def start():
    global G
    nodes_dict = {i: (x + py5.random(-5, 5), y + py5.random(-25, 25))
                  for i, (x, y)
                  in enumerate(product(range(100, 501, 50), repeat=2))}
    G = nx.complete_graph(list(nodes_dict.keys()))        
    nx.set_node_attributes(G, nodes_dict, 'pos')
    for a, b in G.edges():
        G[a][b]['weight'] = py5.dist(*nodes_dict[a], *nodes_dict[b])    
    update_tsp()


def update_tsp():    
    tsp[:] = nx.approximation.traveling_salesman_problem(G)
        
        
def draw():
    py5.background(200)
     
    if py5.is_key_pressed and py5.key_code == py5.SHIFT: 
        py5.stroke(255)
        py5.lines(
            (G.nodes[a]['pos'][0],
             G.nodes[a]['pos'][1],
             G.nodes[b]['pos'][0],
             G.nodes[b]['pos'][1])
             for a, b in G.edges()
             )
    py5.no_fill()
    py5.stroke(0, 0, 100)
    with py5.begin_closed_shape():
        py5.vertices(G.nodes[node]['pos'] for node in tsp)

    py5.no_stroke()
    nodes_coords = nx.get_node_attributes(G, 'pos')  #  {'node': (x,y)}
    for node, (x, y) in nodes_coords.items():
        py5.fill(0)
        if py5.dist(x, y, py5.mouse_x, py5.mouse_y) < 10:
            py5.fill(255, 0, 0)
        py5.circle(x, y, 10)

    py5.window_title(str(py5.get_frame_rate()))

def mouse_pressed():
    global dragged
    nodes_coords = nx.get_node_attributes(G, 'pos')  #  {'node': (x,y)}
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
    #update_tsp()  # to use without the repeating thread...

def key_pressed():
    if py5.key == ' ':
        py5.save_frame('###.png')
        start()
    
py5.run_sketch(block=False)
