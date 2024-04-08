
import skgeom as sg  # conda install scikit-geometry -c conda-forge
import py5

D_HANDLE = 30
pts = [(100, 100), (200, 200), (200, 100),(500, 100), (300, 500), (200, 400)]
drag = None

def setup():
    py5.size(600, 600)
    py5.text_size(18)
    
def draw():
    global poly
    py5.background(240)
    
    poly = sg.Polygon(pts)
    py5.no_fill()
    py5.stroke(0, 200, 0)
    with py5.begin_closed_shape():
        py5.vertices(poly.coords)

    if poly.is_simple():
        skel = sg.skeleton.create_interior_straight_skeleton(poly)
        draw_skeleton(skel)
    else:
        py5.text('Polygon is not simple', 100, 100)

    for i, (x, y) in enumerate(pts):  
        if py5.dist(py5.mouse_x, py5.mouse_y, x, y) < D_HANDLE / 2:
            py5.stroke(255)
            py5.circle(x, y, D_HANDLE)

def draw_skeleton(skeleton, show_time=True):
    for i, h in enumerate(skeleton.halfedges):
        if h.is_bisector:
            p1 = h.vertex.point
            p2 = h.opposite.vertex.point
            py5.stroke(200, 0, 0)
            py5.line(p1.x(), p1.y(), p2.x(), p2.y())
            py5.fill(0)
            py5.text(str(i), (p1.x() + p2.x()) / 2, (p1.y() + p2.y()) / 2)

    if show_time:
        for v in skeleton.vertices:
            py5.no_fill()
            py5.stroke(0, 0, 200)
            py5.circle(v.point.x(), v.point.y(), v.time)

def mouse_pressed():
    global drag
    for i, (x, y) in enumerate(pts):  
        if py5.dist(py5.mouse_x, py5.mouse_y, x, y) < D_HANDLE / 2: 
            drag = i
            break 

def mouse_released(): 
    global drag
    drag = None


def mouse_dragged(): 
    if drag is not None:
        x, y = pts[drag]
        x += py5.mouse_x - py5.pmouse_x
        y += py5.mouse_y - py5.pmouse_y
        pts[drag] = x, y
        
        
py5.run_sketch(block=False)

