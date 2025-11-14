def setup():
    size(500, 500)
    no_loop()
    
def draw():
    background(240, 240, 200)
    quadrado_molnar(100, 100, 100)
    quadrado_molnar(200, 100, 100)
    quadrado_molnar(300, 100, 100)
    quadrado_molnar(100, 200, 100)
    quadrado_molnar(200, 200, 100)
    quadrado_molnar(300, 200, 100)
    quadrado_molnar(100, 300, 100)
    quadrado_molnar(200, 300, 100)
    quadrado_molnar(300, 300, 100)
   
def key_pressed():
    save_frame('###.png')
    redraw()
   
def quadrado_molnar(x, y, tamanho):
    no_fill()  # desliga o preenchimento
    for n in range(10): # n = 0, 1, 2, ... 4
        lado = random(tamanho)
        b = 2 # fator de bagunça
        quad(x - lado / 2 + random(-b,b),
             y - lado / 2 + random(-b,b), # xa, ya
             x + lado / 2 + random(-b,b),
             y - lado / 2 + random(-b,b), # xb, yb
             x + lado / 2 + random(-b,b),
             y + lado / 2 + random(-b,b), # xc, yc
             x - lado / 2 + random(-b,b),
             y + lado / 2 + random(-b,b),# xd, yd         
         )
         