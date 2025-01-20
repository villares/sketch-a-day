import py5

from py5 import radians, sin, cos, TAU

def setup():
    global pts
    py5.size(600, 600, py5.P3D)
    #py5.frame_rate(30)
    pts = py5.create_shape()
    r = 300
    with pts.begin_shape(py5.LINES):
        pts.stroke('white')
        for a in range(0, 360, 6):
            x = r * cos(radians(a))
            y = r * sin(radians(a)) 
            pts.vertex(x, y)
            pts.vertex(x, -y)
        
def draw():
    py5.background('black')
    py5.translate(py5.width / 2, py5.height / 2, -py5.height / 2)
    py5.rotate_x(radians(py5.frame_count))
    for _ in range(50):
        py5.rotate_y(TAU / 50)
        py5.shape(pts)    

def key_pressed():
    print(py5.get_frame_rate())

py5.run_sketch()