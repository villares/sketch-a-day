bolas = []  # (x, y, d) tupla

def setup():
    size(800, 600)
    no_loop()
    
def draw():
    background(255)
    no_stroke()
    fill(0)
    m = millis()
    for _ in range(300_000):
        d = random_int(1, 10) * 5
        x = int(random(1, width / d - 1)) * d
        y = int(random(1, height / d - 1)) * d
        for xe, ye, de in bolas:
            if (x - xe) ** 2 + (y - ye) ** 2 < (d + de) ** 2 / 4:
            #if dist(x, y, xe, ye) < (d + de) / 2:
                break
        else:
            circle(x, y, d)
            bolas.append((x, y, d))
    print(millis() - m)    
    print(len(bolas))
        
def key_pressed():
    if key == ' ':
        redraw()
    if key == 's':
        save_frame('b###.png')
        