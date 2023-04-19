grade = []


def modulo0(x, y, largura):
    no_fill()
    ml = largura / 2 # metade da largura
    arc(x - ml, y - ml, largura, largura, 0, PI / 2)
    arc(x + ml, y + ml, largura, largura, PI, 3 * PI / 2)


def modulo1(x, y, largura):
    no_stroke()
    rect_mode(CENTER)
    fill(0, 0, 200)
    ml = largura / 2 # metade da largura
    rect(x, y, largura, largura)
    fill(0)
    arc(x - ml, y - ml, largura, largura, 0, PI / 2)
    arc(x + ml, y + ml, largura, largura, PI, 3 * PI / 2)
    
def modulo2(x, y, largura):
    no_stroke()
    rect_mode(CENTER)
    fill(0)
    ml = largura / 2 # metade da largura
    rect(x, y, largura, largura)
    fill(0, 0, 200)
    arc(x - ml, y - ml, largura, largura, 0, PI / 2)
    arc(x + ml, y + ml, largura, largura, PI, 3 * PI / 2)


def setup():
    size(600, 600)
    largura = 60
    filas = colunas = 10
    for i in range(colunas):
        x = largura / 2 + i * largura
        for j in range(filas):
            y = largura / 2 + j * largura
            #celula = Celula(x, y, largura, [modulo2, modulo1])
            celula = Celula(x, y, largura, [modulo0])
            grade.append(celula)
    #modulo1(150, 150, 100)
    
def draw():
    background(200)
    for celula in grade:
        celula.desenha()

def mouse_clicked():
    for celula in grade:
        if celula.sob_mouse(mouse_x, mouse_y):
            if is_key_pressed and key_code == SHIFT:
                celula.muda_desenho()
            elif is_key_pressed and key_code == CONTROL:
                celula.espelha()
            else:
                celula.gira()

def key_pressed():
    for celula in grade:
        if key == 'm' and random(100) < 50:
            celula.muda_desenho()
        if key == 'r' and random(100) < 50:
            celula.gira()


class Celula:
    
    def __init__(self, x, y, largura, funcs):
        self.x, self.y = x, y
        self.largura = largura
        self.funcs = funcs
        self.func_ativa = 0
        self.rot = 0
        self.espelhada = False
    
    def desenha(self):
        push_matrix()
        translate(self.x, self.y)
        if self.espelhada:
            scale(-1, 1)
        rotate(HALF_PI * self.rot)
        funcao_desenho = self.funcs[self.func_ativa]
        funcao_desenho(0, 0, self.largura)
        pop_matrix()
 
    def sob_mouse(self, x, y):
        return (self.x - self.largura / 2 < x < self.x + self.largura / 2 and
                self.y - self.largura / 2 < y < self.y + self.largura / 2)
         
    def gira(self):
        self.rot = (self.rot + 1) % 4

    def muda_desenho(self):
        self.func_ativa = (self.func_ativa + 1) % len(self.funcs)
        
    def espelha(self):
        self.espelhada = not self.espelhada
    
        

