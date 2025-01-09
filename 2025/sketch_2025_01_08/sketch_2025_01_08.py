import py5

def setup():
    global pts
    py5.size(1000, 1000, py5.P3D)
    py5.background(0)
    py5.stroke(255)

    pts = py5.create_shape()
    with pts.begin_shape(py5.POINTS):
        for _ in range(4 * 1000):
            v = py5.Py5Vector.random(3)
            v.mag = py5.random(650)
            pts.vertex(*v)    
    
def draw():
    py5.background(0)
    py5.translate(500, 500, -500)
    #py5.rotate_x(py5.mouse_y / 10)
    for _ in range(250):
        py5.rotate_y(py5.TAU / 250)
        py5.shape(pts)
    
def key_pressed():
    py5.save_frame('out.png')

py5.run_sketch()