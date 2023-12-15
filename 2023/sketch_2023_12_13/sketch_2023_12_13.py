# module mode
import py5
# 0. textura (acertar o lance do UV)
# 1. Py5Shape (tem como agrupar um texto)
# 2. função
nomes = ['uva', 'banana', 'maçã', 'kiwi'] * 8
h = 40


def setup():
    py5.size(800, 800, py5.P3D)
    #py5.text_mode(py5.MODEL)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.rect_mode(py5.CENTER)

def draw():
    global r
    py5.background(200)
    py5.translate(400, 400, -100)
    ro = py5.mouse_y / 20  
    n = len(nomes)
    r = 300
    angle = py5.TAU / n
    for i, nome in enumerate(nomes):
        py5.push_matrix()
        py5.rotate_x(angle * i + ro)
        py5.translate(0, 0, r)
        py5.text_size(h)
        w = py5.text_width(nome)
        placa_texto(nome, w + 10, h + 10)    
        py5.pop_matrix()
    py5.no_fill()
    py5.stroke(255, 0, 0)
    py5.stroke_weight(3)
    py5.translate(0, 0, r + 2)
    py5.rect(0, 0, 400, h)
    


def placa_texto(texto, w, h):
    py5.fill(255)
    py5.no_stroke()
    with py5.begin_closed_shape():
        py5.vertex(-w/2, -h/2)
        py5.vertex(+w/2, -h/2)
        py5.vertex(+w/2, +h/2)
        py5.vertex(-w/2, +h/2)
    py5.translate(0, 0, 1)
    py5.fill(0)
    py5.text(texto, 0, -h/8)
    
    
    

py5.run_sketch()  