# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5

regras_a = {
    'X': 'X+[-FX]-[+FX]+FX',
    'F': 'FF',
}
axioma_a = 'X'
pos_a = [400, 700]

def setup():
    global frase_a, frase_b, sa, sb
    py5.size(800, 800)
    
    frase_a = gerar_frase(regras_a, axioma_a, 6)  # num de interações

    sa = Slider(0, 360, 15, label='ângulo')
    sb = Slider(0, 100, 50, label='passo')

def gerar_frase(regras, axioma, num_iteracoes):
    frase_inicial = axioma
    for i in range(num_iteracoes):
        frase_resultado = ''
        for simbolo in frase_inicial:
            frase_resultado = frase_resultado + regras.get(simbolo, simbolo)
        frase_inicial = frase_resultado
    return frase_resultado
    
def draw():
    py5.background(250, 250, 220)
    desenha_frase(*pos_a, frase_a,
                  angulo=sa.value,
                  passo=sb.value / 10)

    Slider.update_all()
  
def mouse_wheel(e):
    Slider.mouse_wheel(e)

def mouse_dragged():
    dx = py5.mouse_x - py5.pmouse_x
    dy = py5.mouse_y - py5.pmouse_y
    ax, ay = pos_a
    pos_a[:] = ax + dx, ay + dy
    
def desenha_frase(x, y, frase, angulo, passo):
    py5.push_matrix()
    py5.translate(x, y)
    for simbolo in frase:
        if simbolo == 'F':
            py5.line(0, 0, 0, -passo)
            py5.translate(0, -passo)
        elif simbolo == '-':
            py5.rotate(py5.radians(angulo))
        elif simbolo == '+':
            py5.rotate(py5.radians(-angulo))
        elif simbolo == '[':
            py5.push_matrix()  # põe na pilha a posição e o ângulo da caneta
        elif simbolo == ']':
            py5.pop_matrix()   # restaura o último estado salvo na pilha
    py5.pop_matrix()

def key_pressed():
    py5.save_frame('###.png')


class Slider:

    template = "{:.1f}"  # para formatar como mostra o valor
    _sliders = []

    def __init__(self, low, high, default, label='', T=float):
        """
        Slider needs range from low to high
        and and a default value. Label is optional.
        """
        self.low = low
        self.high = high
        self.label = label
        self.type = T
        self.value = T(default)
        self.w, self.h = 120, 30
        if not self._sliders:
            self.position(25, 25)  # Pos default
        else:
            ls = self._sliders[-1]
            self.position(ls.x, ls.y + 50)
        self.IS_3D = py5.get_graphics().is3d()
        self._sliders.append(self)

    def position(self, x, y):
        """Define as coordenadas na tela, e calcula w_value, pos. do 'handle'"""
        self.x = x
        self.y = y
        # the position of the rect you slide:
        self.w_value = self.x + py5.remap(
            self.value, self.low, self.high, 0, self.w)

    def update(self):
        """Atualiza o slider e devolve o valor (self.value). Chama display()"""
        # is_mouse_pressed moves slider
        if py5.is_mouse_pressed and self.mouse_over():
            self.w_value = py5.mouse_x - self.x
        # constrain rectangle
        self.w_value = py5.constrain(self.w_value, 0, self.w)
        self.value = self.type(py5.remap(
            self.w_value,
            0, self.w,
            self.low, self.high
        ))
        self.display()
        return self.value

    def mouse_over(self):
        return (self.x < py5.mouse_x < self.x + self.w and
                self.y < py5.mouse_y < self.y + self.h)

    def display(self):
        """Desenha o slider na tela, usando coordenadas sem transformar"""
        py5.push()  # combina push_matrix() e push_style()
        # seguido de reset_matrix() e camera() se em 3D permite
        # desenhar o slider no sistema de coordenadas original
        py5.reset_matrix()  
        if self.IS_3D:
            py5.camera()       
        py5.stroke_weight(1)
        if self.mouse_over():
            py5.stroke(200)
        else:
            py5.stroke(100)
        py5.fill(0, 100)
        py5.rect(self.x - 2, self.y - 2, self.w + 4, self.h + 4)
        # O retângulo, elemento principal da interface do slider
        py5.no_stroke()
        py5.fill(100)
        if self.IS_3D:
            py5.translate(0, 0, 1)
        py5.rect(self.x, self.y, self.w_value, self.h)
        # Mostra o valor (value) atual
        py5.fill(200)
        py5.text_size(14)
        py5.text_align(py5.RIGHT, py5.CENTER)
        py5.text(self.template.format(self.value) if self.type == float else self.value,
                 self.x + self.w - 4, self.y + self.h / 2)
        # draw label
        py5.text_align(py5.LEFT, py5.CENTER)
        py5.text(self.label, self.x + 4, self.y + self.h / 2)
        
        py5.pop()  # equivale a pop_style() and pop_matrix()
    
    
    def process_wheel(self, wd):
        if self.mouse_over():
            self.w_value += wd        

    @classmethod
    def mouse_wheel(cls, e):
        wd = e.get_count()
        for s in cls._sliders:
            s.process_wheel(wd)
                
    @classmethod
    def update_all(cls):
        for s in cls._sliders:
            s.update()


py5.run_sketch(block=False)