from math import sqrt, sin, cos, pi
import py5

TWO_PI = pi * 2
HALF_PI = pi / 2
H = 105              # largura do hexágono
W = sqrt(3) / 2 * H  # altura do hexágono

def setup():
    py5.size(500, 500)
    deslocamento_x, deslocamento_y = H / 2, W / 2
    for i in range(5):
        for j in range(6):
            if j % 2 == 0:
                x = i * W  + deslocamento_y
            else:
                x = i * W + W / 2 + deslocamento_y
            y = j * H * 3 / 4 + deslocamento_x
            poligono_regular(x, y, H / 2, 6, HALF_PI)

def poligono_regular(x_centro, y_centro, r, lados, rot=0):
    """
    Desenha um polígono regular cujos vértices estariam em um
    círculo com centro em x_centro, y_centro e raio `r`
    """
    py5.begin_shape() # começa a desenhar a forma
    for i in range(lados):
        ang = i * TWO_PI / lados + rot
        x = x_centro + cos(ang) * r
        y = y_centro + sin(ang) * r
        py5.vertex(x, y)
    py5.end_shape(py5.CLOSE) # encerra uma forma fechada
    
py5.run_sketch()