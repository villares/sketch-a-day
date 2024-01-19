def setup():
    size(800, 800)
    translate(400, 400)
    s = 100
    for _ in range(6):
        for x in range(-800, 800, s):
            line(x, -800, x, 800)
            line(x + s/6, -800, x + s/6, 800)
            line(x - s/6, -800, x - s/6, 800)
        rotate(radians(30))
    save(__file__[:-2] + '.png')