escala_noise = 0.01
z = 0
tam = 8

def setup():
    size(1200, 600)
    no_stroke()

def draw():
    background(50, 0, 150)
    cols =  int(width / tam)
    rows =  int(width / tam)
    translate(width / 2, height / 2)
    for c in range(cols // 2):
        for r in range(rows // 2):
            on = os_noise(
                (mouse_x + c) * escala_noise,
                (mouse_y + r) * escala_noise,
                 z * escala_noise
                )
            n = 1 + sin(on * 3)
            #n = (((nn + 1) * 2) % 2) / 2 - 1
            if n > 0.02:
                d = tam - tam * n
            else:
                d = max(0, tam - tam * abs(10 * n))
                fill(240, 240, 100, 200)
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


