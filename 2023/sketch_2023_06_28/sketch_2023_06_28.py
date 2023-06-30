def setup():
    size(800, 800) #tamanho da área de desenho
    
def draw():
    background(50)
    #translate(250, 250)
    fill(255, 50, 100)
    xp, yp = frame_count / 2, 100
    lp, ap = 100, 200
    rect(xp, yp, lp, ap)  # x, y, largura, altura

    fill(200)
    quad(xp, yp + ap,
         xp + lp, yp + ap,
         width, height,
         0, height
        )
    # numero visivel
    fill(0)
    text(str(mouse_y), 50, 100)
    no_fill()
    for d in range(500):  # d vai de 0 até 299
        stroke(255, 255, 0, 200 - d * 0.3)
        circle(mouse_x, mouse_y, d)