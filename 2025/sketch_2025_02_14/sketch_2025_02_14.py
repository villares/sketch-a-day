import numpy as np

from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.spatial import ConvexHull
from scipy.spatial import Delaunay



import py5

dragged = None
mst_edges = []
nodes = []

def setup():
    py5.size(600, 600)
    py5.stroke_join(py5.ROUND)
    start()
    
def start():
    nodes[:] = [(py5.random(100, 500),
                 py5.random(100, 500))
                for _ in range(15)]
    update_viz()

def calculate_mst(nodes):
    distances = pdist(nodes)
    dist_matrix = squareform(distances)
    mst = minimum_spanning_tree(dist_matrix)
    mst_dense = mst.toarray()
    rows, cols = np.nonzero(mst_dense)    
    mask = rows < cols
    edges = np.column_stack((rows[mask], cols[mask]))
    return edges

def update_viz():
    global hull, tri
    hull = ConvexHull(nodes)
    tri = Delaunay(nodes)
    mst_edges[:] = calculate_mst(nodes)

def draw():
    py5.background(200)

    py5.no_fill()
    py5.stroke(0, 0, 200, 150)
    py5.stroke_weight(15)
    py5.lines((nodes[i][0], nodes[i][1], nodes[j][0], nodes[j][1])
          for i, j in mst_edges)

    py5.stroke(0, 200, 100)
    py5.stroke_weight(5)
    for ixs in tri.simplices:
        with py5.begin_closed_shape():
            py5.vertices(nodes[ixs])


    # Draw nodes
    py5.no_stroke()
    for x, y in nodes:
        py5.fill(0)
        if py5.dist(x, y, py5.mouse_x, py5.mouse_y) < 10:
            py5.fill(255, 0, 0)
        py5.circle(x, y, 10)

def mouse_dragged():
    global dragged
    for i, (x, y) in enumerate(nodes):
        if py5.dist(x, y, py5.mouse_x, py5.mouse_y) < 10:
            dragged = i
            break
    else:
        dragged = None
    
    if dragged is not None:
        x, y = nodes[dragged]
        dx = py5.mouse_x - py5.pmouse_x
        dy = py5.mouse_y - py5.pmouse_y
        new_x, new_y = x + dx, y + dy
        nodes[dragged] = new_x, new_y

def mouse_released():
    global dragged
    dragged = None
    update_viz()

def key_pressed():
    if py5.key == ' ':
        py5.save_frame('###.png')
        start()

py5.run_sketch(block=False)