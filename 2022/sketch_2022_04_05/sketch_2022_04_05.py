w, h = 100, 15
initial_v = 0.03

def setup():
    size(900, 900)
    no_stroke()
    color_mode(HSB)
    
def draw():
    background(240)
    cols = width // w
    rows = height // h
    n = 0.5
    v = initial_v
    for col in range(cols):
        for row in range(rows):
            x0, y0 = col * w, row * h
            third_x = x0 + w * n
            fill(col * 32 % 255, 200, 200)
            triangle(x0, y0, x0 + w, y0, third_x, y0 + h)
            fill((col + 32) * h % 255, 200, 100)
            triangle(x0, y0, x0, y0 + h, third_x, y0 + h)
            triangle(x0 + w, y0, x0 + w, y0 + h, third_x, y0 + h)
            
            
            n += v
            if not (0 <= n <= 1):
                v = -v
                
def key_pressed():
    global w, h, initial_v
    if key == CODED and key_code == UP:
        h += 1
    elif key == CODED and key_code == DOWN and h > 1:
        h -= 1
    elif key == CODED and key_code == RIGHT: 
        w += 1
    elif key == CODED and key_code == LEFT and w > 1:
        w -= 1
    elif key == 'a':
        initial_v += 0.01
    elif key == 'z':
        initial_v -= 0.011
    # if you omit the key == CODED check, '%&( will also activate

