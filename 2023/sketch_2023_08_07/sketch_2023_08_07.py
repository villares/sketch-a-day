
drag = None
pts = [
    (200, 100),
    (100, 100),
    ]

num_points = 12

def setup():
    size(600, 600)

def draw():
    global num_points
    background(200)
    
    stroke(0)
    stroke_weight(5) 
    fill(255)
    star(300, 300, pts[0][0], pts[0][1], num_points, w_a=pts[1][0]/100, w_b=pts[1][1]/100) 
    fill(200, 0, 0)
    no_stroke()
    for x, y in pts: 
        circle(x, y, 15)       

def star(x, y, radius_a, radius_b, n_points, rot=0, w_a=1, w_b=1):
    step = TWO_PI / n_points
    begin_shape()
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
    end_shape()
           
def mouse_pressed():
    global drag
    for i, (x, y) in enumerate(pts):
        if dist(mouse_x, mouse_y, x, y) < 10:
            drag = i
            break

def mouse_dragged():
    if drag is not None:
        pts[drag] = (mouse_x, mouse_y)

def mouse_released():
    global drag
    drag = None
    
