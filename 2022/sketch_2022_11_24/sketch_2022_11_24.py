TEXT_SIZE = 30

imagens = {}

def setup():
    size(600,600)
    text_size(TEXT_SIZE)

def draw():
    background(0)
    balao(300, 300, 300, 
    texto='Para testar um balão é preciso de um tanto de texto.',
    rounding=True
    )
 
def balao(ox,oy,w,h=None,
    texto='',
    ponta=None,
    mode=CENTER,
    rounding=False,
    flip_h=False,
    flip_v=False
    ):
    push()
    texto_formatado = quebra_frase(texto,w - 10)
    h = h or TEXT_SIZE * (3 + texto_formatado.count('\n'))
    wbase = w / 4
    offset = w / 4
    if mode == CENTER:
        x,y = ox - w / 2.0,oy - h / 2.0
    else:
        x,y = ox,oy
    px,py = ponta or x + w,y + h * 1.5
    push_matrix()
    translate(ox,oy)
    if flip_v:
        scale(1,-1)
    if flip_h:
        scale(-1,1)
    if rounding:
        no_stroke()
        triangle(offset + x + w / 2 + wbase / 2 - ox,y + h * 0.9 - oy,
        px - ox,py - oy,
        offset + x + w / 2 - wbase / 2 - ox,y + h * 0.9 - oy)
        rect(x - ox - h / 4, y - oy, w + h / 2, h, h / 2)
    else:
        pts = [(x - ox,y - oy),(x + w - ox,y - oy),
        (x + w - ox,y + h - oy),
        (offset + x + w / 2 + wbase / 2 - ox,y + h - oy),
        (px - ox,py - oy), # (x + w / 2,y + h),
        (offset + x + w / 2 - wbase / 2 - ox,y + h - oy),
        (x - ox,y + h - oy)]
        draw_poly(pts)

    pop_matrix()
    fill(0)
    text(texto_formatado,x + 5,y + 5)
    pop()
    
    
def quebra_frase(frase, largura):
    resultado = ""
    parcial = ""
    for letra in frase:
        parcial += letra
        if text_width(parcial) > largura:
            ultimo_espaco = parcial.rfind(' ')
            resultado += '\n' + parcial[:ultimo_espaco]
            parcial = parcial[ultimo_espaco + 1:]
    resultado += '\n' + parcial
    return resultado    

def draw_poly(pts,closed=True):
    begin_shape()
    for x,y in pts:
        vertex(x,y)
    if closed:
        end_shape(CLOSE)
    else:
        end_shape()

