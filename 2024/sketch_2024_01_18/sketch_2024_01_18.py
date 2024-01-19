def setup():
    size(800, 800, P3D)
    no_fill()
    ortho()
    stroke_weight(3)
    stroke(255)
    translate(400, 400)
    s = 100
    for _ in range(2):
        rotate_x(radians(45))
        rotate_y(radians(45))
        box(500, 300, 200)
    save(__file__[:-2] + '.png')
