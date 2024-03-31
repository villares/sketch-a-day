def setup():
    size(400, 300)
    background(100)
    stroke_weight(3)
    stroke(0)
    no_fill()

    begin_shape()
    vertex(100, 50)            # 0: vértice âncora
    bezier_vertex(150, 150,    # 1: ponto de controle
                  250, 150,    # 2: ponto de controle
                  200, 200),   # 3: vértice
    bezier_vertex(150, 250,    # 4: ponto de controle
                  50, 200,     # 5: ponto de controle
                  50, 100)     # 6: vértice
    end_shape()

    pontos = [
        (100, 50),   # 0 
        (150, 150),  # 1
        (250, 150),  # 2
        (200, 200),  # 3
        (150, 250),  # 4
        (50, 200),   # 5
        (50, 100),   # 6
        ]
    stroke_weight(1)
    for i, ponto in enumerate(pontos):
        x, y = ponto
        fill(255)
        circle(x, y, 5)
        t="{}: {:3}, {:3}".format(i, x, y)
        text(t, x+5, y-5)
    save('out.png')