# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5


def setup():
    global sa, sb, sc
    py5.size(800, 800, py5.P3D)
    sa = Slider(0, 800, 200, label='A')
    sb = Slider(0, 800, 400, label='B')
    sc = Slider(1, 20, 6, T=int, label='C')
    py5.no_fill()
    py5.stroke_weight(2)
    #py5.hint(py5.ENABLE_DEPTH_SORT)

def draw():
    py5.background(100, 100, 0)
    py5.translate(400, 400)
    py5.rotate_x(py5.QUARTER_PI)
    py5.rotate_y(py5.QUARTER_PI + py5.frame_count / 30)
    py5.stroke(0, 0, 255)
    for _ in range(sc.value):
        py5.circle(0, 0, sa.value)
        py5.rotate_x(py5.PI / sc.value)
    py5.rotate_y(py5.HALF_PI)
    py5.stroke(255, 255, 0)
    for _ in range(sc.value):
        py5.circle(0, 0, sb.value)
        py5.rotate_x(py5.PI / sc.value)
    Slider.update_all()
  
def mouse_wheel(e):
    Slider.mouse_wheel(e)
    
def key_pressed():
    if py5.key == 's':
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

