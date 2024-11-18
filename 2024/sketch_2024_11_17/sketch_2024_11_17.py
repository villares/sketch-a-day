import py5

from py5 import Py5Vector as Vector
  
SQRT2 = py5.sqrt(2)

shapes = []

def setup():
    global current_pos, heading
    py5.size(500, 500)
    py5.background(0, 0, 200)
    py5.translate(250, 250)
    py5.stroke_weight(2)
    py5.no_fill()
    current_pos = Vector(0, 0)
    heading = 0
    star_side = 30
    octagon_side = star_side * 2 + star_side * SQRT2
    forward(-star_side * SQRT2 / 2)
    turn(-90)
    forward(octagon_side / 2)
    set_heading(0)
    star = []
    for i in range(16):
        star.append(current_pos)
        if i % 2 == 0:
            turn(-45)
        else:
            shapes.append(square_pts(octagon_side / SQRT2))
            turn(90)
            shapes.append(square_pts(star_side))
        forward(star_side)
    shapes.append(star)
    forward(-star_side)
    turn(-90)
    forward(octagon_side / SQRT2)
    
    set_heading(0)
    octagon = []
    for i in range(8):
        forward(octagon_side)
        turn(360 / 8)
        octagon.append(current_pos)
    draw_poly(octagon)
    
    for i, shp in enumerate(shapes):
        py5.fill(255 - i * 16, 100)
        draw_poly(shp)

    py5.save(__file__[:-3] + '.png')
   
def forward(d):
    global current_pos
    current_pos = current_pos.copy + (Vector.from_heading(heading) * d)

def set_heading(deg):
    global heading
    heading = py5.radians(deg)

def turn(deg):
    global heading
    heading += py5.radians(deg)

def draw_poly(pts):
    with py5.begin_closed_shape():
        py5.vertices(pts)
    
def square_pts(d):
    pts = []
    for _ in range(4):
        pts.append(current_pos)
        forward(d)
        turn(90)
    return pts

    

py5.run_sketch(block=False)

