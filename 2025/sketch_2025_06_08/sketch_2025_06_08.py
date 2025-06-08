import py5
from py5 import Py5Vector as V
from py5 import sin, cos, PI
import py5_tools


def setup():
    py5.size(400, 400)
    py5.stroke_weight(1)
    py5.no_cursor()  # desativa a setinha do mouse

def draw():
    py5.background(150)
    mx, my = py5.mouse_x, py5.mouse_y
    w = 20
    n = int(py5.width / w)
    py5.no_stroke()
    py5.fill(255)
    py5.circle(mx, my, w * 3)
    py5.stroke(0)
    for i in range(n):
        x = w / 2 + i * w
        for j in range(n):
            y = w / 2 + j * w
            d = py5.dist(x, y, mx, my)
            ang = py5.atan2(y - my, x - mx)
            v = V.from_heading(ang) * 100000 / (d + w) ** 2
            if  d > 1:
                seta_vetor(v, (x, y), 10)
    
    
def seta_vetor(v, origin=(0, 0), head_size=10):
    """
    Desenhe uma seta representando um vetor `v`, partindo da origem (0, 0)
    ou na posição informada com o argumentos opcional `origin`.
    """
    from py5 import Py5Vector as V
    from py5 import sin, cos, PI
    sg = py5.get_graphics()
    current_stroke = sg._instance.strokeColor
    v = V(*v)
    body = v.mag
    head_size = min(head_size, body / 2)
    xo, yo = origin
    xh = xo + v.x
    yh = yo + v.y
    ang = v.heading
    xha = xh + cos(ang + PI / 8 + PI) * head_size
    yha = yh + sin(ang + PI / 8 + PI) * head_size
    xhb = xh + cos(ang - PI / 8 + PI) * head_size
    yhb = yh + sin(ang - PI / 8 + PI) * head_size
    py5.line(xo, yo, xh, yh)  # corpo com tamanho fixo
    with py5.push():  # preserva os atributos gráficos atuais
        py5.stroke_join(py5.SQUARE)
        py5.fill(current_stroke)  # usa a cor de traço como preenchimento!
        py5.no_stroke()
        with py5.begin_closed_shape():
            py5.vertex(xha, yha)
            py5.vertex(xh, yh)
            py5.vertex(xhb, yhb)
            py5.end_shape(py5.CLOSE)
            
def key_pressed():
    py5_tools.animated_gif('out.gif', count=100, period=1/30, duration=1/15)


py5.run_sketch(block=False)