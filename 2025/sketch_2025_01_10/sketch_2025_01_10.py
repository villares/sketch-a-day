import py5

from py5 import TAU

u = int(TAU / TAU)
d = u + u
t = u + u + u
tt = int(TAU * TAU * TAU)

def setup():
    global pts
    py5.size(tt * t, tt * t, py5.P3D)
    pts = py5.create_shape()
    with pts.begin_shape(py5.POINTS):
        for _ in range(py5.height):
            v = py5.Py5Vector.random(t)
            v.mag = py5.random(py5.height)
            pts.stroke(py5.random_choice(
                ('red', 'blue','green')))
            pts.vertex(*v)    
    py5.background('black')
    py5.translate(py5.width / d, py5.height / d, -py5.height / d)
    #py5.rotate_x(py5.mouse_y / 10)
    for _ in range(tt):
        py5.rotate_y(TAU / tt)
        py5.shape(pts)    
    py5.save_frame('out.png')

py5.run_sketch()