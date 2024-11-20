import py5

from py5 import Py5Vector as Vector
  
SQRT2 = py5.sqrt(2)

shapes = []

star_side = 20.2


def setup():
    global current_pos, heading
    py5.size(500, 500)
    py5.background(0)
    py5.no_stroke()
    py5.color_mode(py5.HSB)
    
    current_pos = Vector(0, 0)
    heading = 0
    octagon_side = star_side * 2 + star_side * SQRT2
    
    forward(-star_side * SQRT2 / 2)
    turn(-90)
    forward(octagon_side / 2)
    set_heading(0)
    #star = []
    for i in range(16):
        #star.append(current_pos)
        if i % 2 == 0:
            turn(-45)
            shapes.append(square_pts(star_side))
        else:
            turn(90)
            shapes.append(triangle_pts(octagon_side / SQRT2))
        forward(star_side)
    #shapes.insert(0, star)
    forward(-star_side)
    turn(-90)
    forward(octagon_side / SQRT2)

    ow = octagon_side + 2 * octagon_side / SQRT2
    for i in range(4):
        x = i * ow
        for j in range(4):
            y = j * ow
            with py5.push_matrix():
                py5.translate(x, y)
                for i, shp in enumerate(shapes):
                    #py5.fill((255 - i * 32) % 255, 200, 200)
                    py5.fill((i * 8) % 255, 200, 200)
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

def triangle_pts(d):
    s = (d * SQRT2) / (2 + SQRT2) 
    pts = []
    pts.append(current_pos)
    turn(-90)
    forward(d)
    pts.append(current_pos)
    turn(-90-45)
    forward(s)
    pts.append(current_pos)
    turn(-45)
    forward(s)
    pts.append(current_pos)
    turn(90)
    forward(s)
    pts.append(current_pos)
    turn(-45)
    forward(s)
    pts.append(current_pos)
    turn(-90-45)
    forward(d)
    return pts

def square_pts(d):
    pts = []
    for _ in range(4):
        pts.append(current_pos)
        forward(d)
        turn(90)
    return pts

py5.run_sketch(block=False)

