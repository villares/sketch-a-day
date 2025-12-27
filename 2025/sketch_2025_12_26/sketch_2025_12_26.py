from itertools import product
import py5

drag = None
W, H = 50, 25
PTS = [
    (400 - W, 400 - H),     
    (400 + W, 400 - H),     
    (400 + W, 400 + H),     
    (400 - W, 400 + H),     
]

def setup():
    py5.size(800, 800)
 
def draw():
    py5.background(0)
    py5.no_fill() 
    py5.stroke_weight(2)
    py5.stroke(255)
    for i, j in product((-1, 0, 1), repeat=2):
        with py5.push_matrix():
            py5.translate(i * W * 4, j * H * 4)
            with py5.begin_closed_shape(): 
                py5.vertices(PTS)
    py5.stroke_weight(10)
    for x, y in PTS:
        if py5.dist(x, y, py5.mouse_x, py5.mouse_y) < 10:
            py5.stroke(200, 200, 0)
        else:
            py5.stroke(0, 200, 200)
        py5.point(x, y)
     
def mouse_pressed():
    global drag
    if drag is None:
        for i, (x, y) in enumerate(PTS):
            if py5.dist(x, y, py5.mouse_x, py5.mouse_y) < 10:
                drag = i
                break
            
def mouse_dragged():
    if drag is not None:
        PTS[drag] = (py5.mouse_x, py5.mouse_y)
    
def mouse_released():
    global drag
    drag = None
     
py5.run_sketch(block=False)
