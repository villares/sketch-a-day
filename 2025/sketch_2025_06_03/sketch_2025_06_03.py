bolas = []  # (x, y, d) tupla

def setup():
    size(800, 600)
    no_loop()
    
def draw():
    background(0)
    no_stroke()
    global gravando
    for _ in range(1_000_000):
        d = random_int(1, 25) * 4
        x = random(width) #int(random(width/d)) * d
        y = random(height) #int(random(height/d)) * d
        for xe, ye, de in bolas:
            if dist(x, y, xe, ye) < (d + de) / 2:
                break
        else:
            bolas.append((x, y, d))
    print(len(bolas))            
    for x, y, d in bolas:
        color_mode(HSB) # matiz, sat, bri
        fill(d * 2.5, 255, 255)
        circle(x, y, d)
        
def key_pressed():
    if key == ' ':
        redraw()
    if key == 's':
        save_frame('b###.png')
        