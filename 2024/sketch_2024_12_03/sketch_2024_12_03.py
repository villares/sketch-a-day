escala_noise = 0.02
z = 0
tam = 6

def setup():
    size(1200, 600)
    no_stroke()

def draw():
    background(60, 0, 150)
    cols =  int(width / tam)
    rows =  int(width / tam)
    translate(width / 2, height / 2)
    for c in range(cols // 2):
        for r in range(rows // 2):
            n = os_noise(
                (mouse_x + c) * escala_noise,
                (mouse_y + r) * escala_noise,
                 z * escala_noise
                )
            
            f = 1.2
            d = (tam * f - abs(sin(-1 + n * PI)) * tam)
            if n > 0.1:
                fill(240, 240, 100)
            else:
                fill(20, 0, 100)
                #fill(200, 0, 0, 100)
#                d = max(0, tam - tam * abs(10 * n)) * f
            circle(tam / 2 + c * tam,
                   tam / 2 + r * tam, d)
            circle(-tam / 2 - c * tam,
                   tam / 2 + r * tam, d)
            circle(-tam / 2 - c * tam,
                   -tam / 2 - r * tam, d)
            circle(tam / 2 + c * tam,
                   -tam / 2 -r * tam, d)
        
def key_pressed():
    global z
    if key_code == UP:
        z += 1
    if key_code == DOWN:
        z -= 1


