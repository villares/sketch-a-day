from math import sqrt, sin, cos, pi
import py5

TWO_PI = pi * 2
HALF_PI = pi / 2
W = 105                # largura do hexágono
H = sqrt(3) / 2 * W    # altura do hexágono
OX, OY = W / 2, H / 2  # deslocamento (offset)

def setup():
    py5.size(500, 500)
    for i in range(6):
        for j in range(5):
            if i % 2 == 0:
                y = j * H  + OY
            else:
                y = j * H + H / 2 + OY
            x = i * W * 3 / 4 + OX
            poligono_regular(x, y, W / 2, 6)

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