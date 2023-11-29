def setup():
    size(500, 500)
    rect_mode(CENTER)
    no_fill()
    no_loop()
    translate(250, 250)
    for _ in range(8):
        rotate(QUARTER_PI)
        with push_matrix():
            translate(-250, -250)
            for _ in range(10):
                square(110, 110, 50)
                scale(1.1)
    
    save(__file__[:-2] + 'png')