import py5

from py5 import Py5Vector as Vector
  
SQRT2 = py5.sqrt(2)

def setup():
    global current_pos, heading
    py5.size(500, 500)
    py5.background(0, 0, 200)
    py5.translate(200, 200)
    py5.stroke_weight(2)
    py5.no_fill()
    current_pos = Vector(0, 0)
    heading = 0
    segment_size = 30
    star = [current_pos]
    for i in range(15):
        if i % 2 == 0:
            turn(-45)
        else:
            turn(90)
        foward(segment_size)
        star.append(current_pos.copy)
    draw_poly(star)
    
    foward(segment_size + segment_size * SQRT2)
    #py5.circle(*current_pos, 5)
    octagon_side = segment_size * 2 + segment_size * SQRT2
    set_heading(0)
    octagon = [current_pos.copy]
    for i in range(7):
        foward(octagon_side)
        turn(360 / 8)
        octagon.append(current_pos)
    draw_poly(octagon)
    
    py5.stroke(255)
    for i, (xa, ya) in enumerate(star[1::2]):
        xb, yb = octagon[i]
        py5.line(xa, ya, xb, yb)
        xc, yc = octagon[(i + 1) % 8]
        py5.line(xa, ya, xc, yc)

    py5.save(__file__[:-3] + '.png')
   
def foward(d):
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
    

py5.run_sketch(block=False)

