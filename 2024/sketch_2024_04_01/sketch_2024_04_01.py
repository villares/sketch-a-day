import py5_tools

A = 180
R = 200
s = 10

def setup():
    size(600, 600, P3D)
    py5_tools.animated_gif(
        'out.gif',
        frame_numbers=range(1, 361, 3),                       
        duration=0.2)

def draw():
    #ortho()
    background(240, 240, 220)
    translate(width / 5, height / 2, -height * 1.6) 
    rotate_y(radians(45))
    #rotate_y(radians(mouse_x))
    stroke_weight(3)
    stroke(0)
    no_fill()

    begin_shape()
    a = 0
    r = 0
    m = frame_count
    n = 3
    x, y = r * cos(a), r * sin(a)
    z = -A / 2 * s
    curve_vertex(x, y, z)
    for i in range(A):
        a = radians(i)
        r = R * sin(a) ** 2 * sqrt(n)
        z = -A / 2 * s + i * s 
        x, y = r * cos(a * m), r * sin(a * m)
        curve_vertex(x, y, z) 
    curve_vertex(x, y, z) 
    end_shape()
    if frame_count > 360:
        no_loop()

def key_pressed():
    exit_sketch()