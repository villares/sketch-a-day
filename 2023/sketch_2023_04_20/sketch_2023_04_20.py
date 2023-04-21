from itertools import product

lado = 40
filas = 40
colunas = 30

def setup():
    size(1200, 800)
    stroke_weight(3)
    for coluna in range(colunas):
        for fila in range(filas):
            celula = Celula(coluna, fila, lado, [modulo2, modulo1])
            
def draw():
    background(200)
    for celula in Celula.grade.values():
        celula.desenha()

def mouse_clicked():
    for celula in Celula.grade.values():
        if celula.sob_mouse(mouse_x, mouse_y):
            if is_key_pressed and key_code == SHIFT:
                celula.muda_desenho()
            else:
                celula.gira()

def key_pressed():
    for i, j in product(range(colunas), range(filas)):
        celula = Celula.grade[i, j]
        if key == 'm' and random(100) < 50:
            celula.muda_desenho()
        elif key == 'r' and random(100) < 50:
            celula.gira()
        elif key == ' ':
            celula.arruma_cor()


def modulo1(x, y, lado):
    no_stroke()
    rect_mode(CENTER)
    fill(0, 0, 200)
    ml = lado / 2 # metade da lado
    rect(x, y, lado, lado)
    fill(0)
    arc(x - ml, y - ml, lado, lado, 0, PI / 2)
    arc(x + ml, y + ml, lado, lado, PI, 3 * PI / 2)
    
def modulo2(x, y, lado):
    no_stroke()
    rect_mode(CENTER)
    fill(0)
    ml = lado / 2 # metade da lado
    rect(x, y, lado, lado)
    fill(0, 0, 200)
    arc(x - ml, y - ml, lado, lado, 0, PI / 2)
    arc(x + ml, y + ml, lado, lado, PI, 3 * PI / 2)

class Celula:
    grade = {}
    
    def __init__(self, i, j, lado, funcs):
        self.coluna = self.i = i
        self.fila = self.j = j
        self.x = lado / 2 + i * lado
        self.y = lado / 2 + j * lado
        self.lado = lado
        self.funcs = funcs
        self.func_ativa = 0
        self.rot = 0
        Celula.grade[i, j] = self
    
    def desenha(self):
        push_matrix()
        translate(self.x, self.y)
        rotate(HALF_PI * self.rot)
        funcao_desenho = self.funcs[self.func_ativa]
        funcao_desenho(0, 0, self.lado)
        pop_matrix()
 
    def sob_mouse(self, x, y):
        return (self.x - self.lado / 2 < x < self.x + self.lado / 2 and
                self.y - self.lado / 2 < y < self.y + self.lado / 2)
         
    def gira(self, rot=None):
        if rot is None:
            self.rot = not self.rot 
        else:
            self.rot = rot

    def muda_desenho(self, i=None):
        if i is None:
            self.func_ativa = not self.func_ativa
        else:
            self.func_ativa = i
            
    def arruma_cor(self):
        """
        Baseado em "Processing: Creative Coding and Generative Art in Processing 2"
        by Ira Greenberg, Dianna Xu, Deepak Kumar
        """
        i, j = self.i, self.j
        if i > 0 and j == 0:   # first tile of a row, starting from the 2nd row
            # same rot as tile directly above
            if Celula.grade[i-1, 0].rot == self.grade[i, 0].rot:
                # set to opposite coloring of my neighbor above
                self.grade[i, 0].func_ativa = not self.grade[i-1, 0].func_ativa
            else:
                # set to same coloring of my neighbor above
                self.grade[i, 0].func_ativa = self.grade[i-1, 0].func_ativa
        if j > 0:  # subsequent grade in a row, including the first
            # same rot as tile to the left
            if self.grade[i, j-1].rot == self.grade[i, j].rot:
                # set to opposite coloring of my neighbor to the left
                self.grade[i, j].func_ativa = not self.grade[i, j-1].func_ativa
            else:
                # set to same coloring of my neighbor to the left
                self.grade[i, j].func_ativa = self.grade[i, j-1].func_ativa        

