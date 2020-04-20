estado_inicial = True

def setup():
    global b1, b2
    size(400, 400)
    b1 = Botao(100, 125, 200, 50, "clique aqui")
    b2 = Botao(100, 225, 200, 50, "de novo!")

def draw():
    if estado_inicial:
        background(200)
    else:
        background(10)
        
    global estado_inicial
    resultado1 = b1.display()
    resultado2 = b2.display()
    if resultado1 or resultado2:
            print('clique')
            estado_inicial = not estado_inicial
            

class Botao():

    def __init__(self, x, y, w, h, t):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.t = t
        self.pressed = False

    def mouse_over(self):
        return (self.x < mouseX < self.x + self.w and
                self.y < mouseY < self.y + self.h)

    def display(self):
        mouse_over = self.mouse_over()
        if mouse_over:
            fill(140)
        else:
            fill(240)
        rectMode(CORNER)
        rect(self.x, self.y, self.w, self.h, 5)
        fill(0)
        textAlign(CENTER, CENTER)
        text(self.t,
             self.x + self.w / 2,
             self.y + self.h / 2)

        if mouse_over and self.pressed and not mousePressed:
            self.pressed = False
            return True

        if mouse_over and mousePressed:
            self.pressed = True
        else:
            self.pressed = False

        return False
