squares = []

def setup():
    size(500, 500)
    generate()
    
def generate():
    squares.clear()
    for _ in range(10):
        w = random_int(2, 5) * 30
        x = random(w, width - w)
        y = random(w, height - w)
        squares.append((x, y, w))
    
def draw():
    background(255)
    no_stroke()
    fill(0)
    for _ in range(20):
        for x, y, w in squares:
            square(x, y, w)
        translate(-2, -2)
        apply_filter(BLUR, 2)

def key_pressed():
    if key == 's':
        save_frame('###.png')
    elif key == ' ':
        generate()
