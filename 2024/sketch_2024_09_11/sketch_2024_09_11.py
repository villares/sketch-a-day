import py5

def setup():
    py5.size(600, 600)
    py5.rect_mode(py5.CENTER)
    py5.no_fill()
    for angle in range(0, 180, 15):
        rotated_rect(200, 200, 300, 200, py5.radians(angle))
        rotated_rect(300, 300, 300, 200, py5.radians(angle))
    py5.save('out.png')

def rotated_rect(x, y, w, h, a):
    with py5.push_matrix():  # no contexto de novo sistema de coords
        py5.translate(x, y)  # muda a origem ou altera o 0,0
        py5.rotate(a)        # gira o sistema de coordenadas
        py5.rect(0, 0, w, h) # x, y, largura, altura
    # restaura o sistema de coordenadas anterior        

py5.run_sketch()