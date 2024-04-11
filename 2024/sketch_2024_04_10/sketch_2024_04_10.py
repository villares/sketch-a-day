
import py5
import shapely


D_HANDLE = 30
pts = [(100, 100), (200, 200), (200, 100),(500, 100), (300, 500), (200, 400)]
drag = None

def setup():
    py5.size(600, 600)
    py5.text_size(18)
    
def draw():
    global poly
    py5.background(240)
    py5.no_fill()
    
    poly = shapely.Polygon(pts)
    py5.stroke(0)
    py5.shape(py5.convert_shape(poly), 0, 0)
    poly = poly.buffer(0)
    
    if poly.is_valid:
        for bo in range(40, -41, -10):
            py5.fill(0, 200, 0)
            shp = poly.buffer(bo, join_style='mitre', mitre_limit=1)
            py5.shape(py5.convert_shape(shp), 0, 0)
            py5.fill(0, 0, 200)
            shp = poly.buffer(bo, join_style='round')
            py5.shape(py5.convert_shape(shp), 0, 0)

    else:
        py5.text('Polygon is not simple', 100, 100)

    for i, (x, y) in enumerate(pts):
        py5.fill(0)
        py5.no_stroke()
        py5.circle(x, y, 3)
        py5.no_fill()
        py5.stroke(255, 0, 0)
        if py5.dist(py5.mouse_x, py5.mouse_y, x, y) < D_HANDLE / 2:
            py5.no_fill()
            py5.circle(x, y, D_HANDLE)

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

