# Code on the left generating drawing on the right, black background, 13 different stars from yellow (17 pointed) to red (5 pointed)

def setup():
    size(700, 700)
    color_mode(HSB) # Hue (Matiz), Sat, Bri
    
def draw():
    background(0)
    a = TWO_PI / 13
    for i in range(13):
        fill(255 - i * 18, 200, 255)
        sx = cos(i * a) * 300
        sy = sin(i * a) * 300
        estrela(350 + sx, 350 + sy, 25, 50, 5 + i)

def estrela(x, y, raio_a, raio_b, num_pontas):
    passo = TWO_PI / num_pontas
    begin_shape()
    ang=0
    while ang < TWO_PI:  # enquanto o ângulo for menor que 2 * PI:
        sx = cos(ang) * raio_a
        sy = sin(ang) * raio_a
        vertex(x + sx, y + sy)
        sx = cos(ang + passo / 2.) * raio_b
        sy = sin(ang + passo / 2.) * raio_b
        vertex(x + sx, y + sy)
        ang += passo  # aumente o ângulo um passo
    end_shape(CLOSE)
    
    
    