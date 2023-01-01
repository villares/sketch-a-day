# Genuary 1 - using py5 (py5coding.org)

def setup():
    size(600, 600)
    blend_mode(ADD)
    no_stroke()
    
def draw():
    background(0)
    xc = yc = 300
    r = 250
    for i in range(6):
        m = cos(radians(frame_count / 2)) ** 2
        a = radians(frame_count / 2 + 60 * i)
        x = xc + r * cos(a)
        y = yc + r * sin(a)
        fill(0, 0, 255)
        circle(x, y, 50)
        x = xc + r * cos(a * m)
        y = yc + r * sin(a * m)
        fill(0, 255, 0)
        circle(x, y, 50)
        x = xc + r * cos(a * -m)
        y = yc + r * sin(a * -m)
        fill(255, 0, 0)
        circle(x, y, 50)
        
# Salvei os frames ímpares até 360 e repeti algumas vezes o 360