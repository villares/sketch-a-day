# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5


drag = None
pts = [
    (200, 100),
    (100, 100),
    ]

num_points = 12

def setup():
    py5.size(600, 600)
    py5.stroke_join(py5.ROUND)

def draw():
    global num_points
    py5.background(200)
    
    py5.stroke_weight(5) 
    py5.no_fill()
    py5.stroke(0, 0, 200, 200)
    py5.ellipse(300, 300, pts[0][0] * pts[0][1]/100 * 2, pts[0][0] * 2)
    py5.ellipse(300, 300, pts[1][0] * pts[1][1]/100 * 2, pts[1][0] * 2)
    py5.stroke(200, 0, 0, 200)
    star(
        300, 300,
        pts[0][0], pts[1][0],
        num_points,
        w_a=pts[0][1]/100, w_b=pts[1][1]/100) 
    py5.fill(200, 0, 0)
    py5.no_stroke()
    for x, y in pts: 
        py5.circle(x, y, 15)       

def star(x, y, radius_a, radius_b, n_points, rot=0, w_a=1, w_b=1):
    from py5 import TWO_PI, sin, cos, vertex, quadratic_vertex
    step = TWO_PI / n_points
    with py5.begin_shape():
        for i in range(n_points + 1):
            ang = i * step + rot
            sx = cos(ang) * radius_a * w_a
            sy = sin(ang) * radius_a
            cx = cos(ang + step / 2.0) * radius_b * w_b
            cy = sin(ang + step / 2.0) * radius_b
            if i == 0:
                vertex(x + cx, y + cy)
            else:
                quadratic_vertex(x + sx, y + sy, x + cx, y + cy)
           
def mouse_pressed():
    global drag
    for i, (x, y) in enumerate(pts):
        if py5.dist(py5.mouse_x, py5.mouse_y, x, y) < 10:
            drag = i
            break

def mouse_dragged():
    if drag is not None:
        pts[drag] = (py5.mouse_x, py5.mouse_y)

def mouse_released():
    global drag
    drag = None
    
def key_pressed():
    py5.save_frame('out.png')

py5.run_sketch(block=False)


