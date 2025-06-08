def setup():
    size(400, 400)
    stroke_weight(2)
    no_cursor()  # desativa a setinha do mouse

def draw():
    background(200)
    w = 20
    n = int(width / w)
    for i in range(n):
        x = w / 2 + i * w
        for j in range(n):
            y = w / 2 + j * w
            d = dist(x, y, mouse_x, mouse_y)
            ang = atan2(y - mouse_y, x - mouse_x) + PI
            v = Py5Vector.from_heading(ang) * 100000 / (d + 1) ** 2
            if  d > w * 2:
                seta_vetor(v, (x, y), 10)
    
    
def seta_vetor(v, origin=(0, 0), head_size=10):
    """
    Desenhe uma seta representando um vetor `v`, partindo da origem (0, 0)
    ou na posição informada com o argumentos opcional `origin`.
    """
    sg = get_graphics()
    current_stroke = sg._instance.strokeColor
    v = Py5Vector(*v)
    body = v.mag
    head_size = min(head_size, body / 2)
    xo, yo = origin
    xh = xo + v.x
    yh = yo + v.y
    ang = v.heading
    xha = xh + cos(ang + QUARTER_PI / 2 + PI) * head_size
    yha = yh + sin(ang + QUARTER_PI / 2 + PI) * head_size
    xhb = xh + cos(ang - QUARTER_PI / 2 + PI) * head_size
    yhb = yh + sin(ang - QUARTER_PI / 2 + PI) * head_size
    line(xo, yo, xh, yh)  # corpo com tamanho fixo
    with push():  # preserva os atributos gráficos atuais
        fill(current_stroke)  # usa a cor de traço como preenchimento!
        no_stroke()
        with begin_closed_shape():
            vertex(xha, yha)
            vertex(xh, yh)
            vertex(xhb, yhb)
            end_shape(CLOSE)
