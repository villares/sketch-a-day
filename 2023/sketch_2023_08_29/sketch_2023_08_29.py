

def setup():
    size(500, 500)
    f = create_font('Inconsolata Bold', 20)
    text_font(f)
    
def draw():
    background(200)
    balao_poly(250, 100, 200, 50, desloca=250/20)
    balao_poly(250, 250, 200, 50)
    desloca=mouse_x - width/2
    balao_poly(250, 400, 200, 50, desloca=desloca)
    text(desloca, 50, 450)

def  balao_poly(x, y, w, h, texto='Olá mundo!', desloca=0):
    stroke_join(ROUND)
    desloca = max(min(desloca, w * 0.45), -w * 0.45)
    fill(255)
    begin_shape()
    vertex(x - w / 2, y - h / 2)
    vertex(x + w / 2, y - h / 2)
    vertex(x + w / 2, y + h / 2)
    vertex(x + w / 20 + desloca, y + h / 2)
    vertex(x, y + 3 * h / 2)
    vertex(x - w / 20 + desloca, y + h / 2)
    vertex(x - w / 2, y + h / 2)
    end_shape(CLOSE)
    fill(0)
    text_size(h / 2)
    text_align(CENTER, CENTER)
    text(texto, x, y)
    
