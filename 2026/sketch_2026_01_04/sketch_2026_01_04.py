import py5
import py5_tools


def setup():
    global osb
    py5.size(600, 600)
    f = py5.create_font('Tomorrow Bold', 600)
    osb = py5.create_graphics(600, 600)
    osb.begin_draw()
    osb.background(0)
    osb.fill(255)
    osb.text_font(f)
    osb.text_align(py5.CENTER, py5.CENTER)
    osb.text('G', 320, 300)
    osb.end_draw()

#def draw():
    py5.background(0)
    py5.no_fill() 
    py5.stroke_weight(2)
    py5.stroke(255)    
    num = 40
    R = py5.width / num
    largura = R * 1.5
    altura = R * py5.sqrt(3) 
    for fila in range(num):
        for coluna in range(num):  # 0, 1, ... 9
            x = int(coluna * largura)
            y = int(fila * altura
                    + (altura / 2 if coluna % 2 else 0))
            py5.fill(osb.get_pixels(x, y))
            poligono(x, y, R - 4)

    py5.save_frame('out.png')

def poligono(xc, yc, ra, pontos=6):
    ang = py5.TWO_PI / pontos
    with py5.begin_closed_shape():
        for i in range(pontos):
            x = xc + py5.cos(ang * i) * ra
            y = yc + py5.sin(ang * i) * ra
            py5.vertex(x, y)
     
py5.run_sketch(block=False)

