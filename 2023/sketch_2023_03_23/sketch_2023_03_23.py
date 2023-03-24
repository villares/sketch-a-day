def setup():
    size(500, 500, P3D)
    frame_rate(2)
    no_fill()
    stroke_weight(1.5)
    stroke(0, 100)
    blend_mode(MULTIPLY)
    
def draw():
    background(200)
    translate(200, 0)
    rotate_y(QUARTER_PI)
    translate(0, 0, 100)
    for z in range(50, 450, 25):
        i = 0
        for y in range(50, 450, 25):
            for x in range(50, 450, 25):    
                limite = i / 5
                push_matrix()
                offset_x = random(-limite, limite) / 10
                offset_y = random(-limite, limite) / 10
                translate(x + offset_x, y + offset_y)
                rotate(radians(random(-limite, limite)))
                rect(-10, -10, 20, 20, 5)
                pop_matrix()
                i += 1
        translate(0, 0, -50)
        