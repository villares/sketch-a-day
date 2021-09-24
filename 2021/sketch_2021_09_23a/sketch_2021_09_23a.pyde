def setup():
    size(200, 200)
    global lado1, lado0
    lado1 = loadImage('lado1.png')
    lado0 = loadImage('lado0.png')
    noLoop()  # para o draw()
    
def draw():
    x = y = 0
    t = 50 # tamanho
    for _ in range(16):
        s = int(random(2))  # 1 ou 0
        # print(s)
        if s == 0:
            image(lado0, x, y, t, t)
        else:
            image(lado1, x, y, t, t)
        x = x + t
        if x == 4 * t:
            x = 0
            y = y + t
            
def keyPressed():
    redraw()  # novo sortei
