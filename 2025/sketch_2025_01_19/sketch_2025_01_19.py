import py5
from py5 import radians, sin, cos, TAU
from py5_tools import animated_gif

def setup():
    global c_lines
    py5.size(600, 600, py5.P3D)
    py5.frame_rate(30)
    py5.stroke_weight(2)
    c_lines = py5.create_shape()
    r = 300
    with c_lines.begin_shape(py5.LINES):
        c_lines.stroke('white')
        for a in range(0, 360, 10):
            x = r * cos(radians(a))
            y = r * sin(radians(a)) 
            c_lines.vertex(x, y)
            c_lines.vertex(x, -y)
            
    animated_gif('out.gif',
                 duration=0.1,
                 frame_numbers=range(1, 181, 2),
                 optimize=False)

def draw():
    py5.background('black')
    py5.translate(py5.width / 2, py5.height / 2, -py5.height / 2)
    py5.rotate_x(radians(py5.frame_count))
    for _ in range(36):
        py5.rotate_y(TAU / 36)
        py5.shape(c_lines)    


py5.run_sketch()