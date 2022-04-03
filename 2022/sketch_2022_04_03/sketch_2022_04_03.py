H = 30
W = 90

def setup():
    size(900, 900)
    no_stroke()
    fill(0)
    
def draw():
    background(240)
    cols = width // W
    rows = height // H
    for row in range(rows):
        for col in range(cols):
            x0, y0 = col * W, row * H
            n = 0.5 + (0.25 * sin(degrees(col) / (1 + mouse_x)) +
                       0.25 * sin(degrees(row) / (1 + mouse_y)))
            third_x = x0 + W * n
            triangle(x0, y0, x0 + W, y0, third_x, y0 + H)
            