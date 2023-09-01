"""
9 balões de fala desenhados com programação,
contendo os números de 1 a 9 e as pontas variando
de inclinação da esquerda para a direita.
"""

def setup():
    size(600, 600)
    f = create_font('Inconsolata Bold', 20)
    text_font(f)
    
def draw():
    background(100, 200, 100)
    stroke_weight(1.5)
    for i in range(1, 10):
        y = i * 60
        balao_poly(width / 2, y, 200, 30, (i + frame_count) % 360, desloca=80 * sin(radians(frame_count + y)))
    if frame_count % 18 == 0 and frame_count <= 360:
        save_frame(__file__[:-3] + '###.png')

def  balao_poly(x, y, w, h, texto='', desloca=0):
    stroke_join(ROUND)
    desloca = max(min(desloca, w * 0.45), -w * 0.45)
    fill(255)
    begin_shape()
    vertex(x - w / 2, y - h / 2)
    vertex(x + w / 2, y - h / 2)
    vertex(x + w / 2, y + h / 2)
    vertex(x + w / 20 + desloca, y + h / 2)
    vertex(x + desloca / 2, y + 3 * h / 2)
    vertex(x - w / 20 + desloca, y + h / 2)
    vertex(x - w / 2, y + h / 2)
    end_shape(CLOSE)
    fill(0)
    text_size(h / 2)
    text_align(CENTER, CENTER)
    text(texto, x, y)
    
