def setup():
    size(500, 500)
    frame_rate(2)
    
    
def draw():
    background(200)
    fill(0)
    i = 0
    for y in range(50, 450, 25):
        for x in range(50, 450, 25):    
            limite = i / 5
            push_matrix()
            offset_x = random(-limite, limite) / 25
            offset_y = random(-limite, limite) / 25
            translate(x + offset_x, y + offset_y)
            rotate(radians(random(-limite, limite)))
            rect(-10, -10, 20, 20, 5)
            pop_matrix()
            i += 1
