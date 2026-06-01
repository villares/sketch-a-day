# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5
#from slider import Slider


def setup():
    global sa, sb
    py5.size(800, 800, py5.P3D)
    sa = Slider(0, 600, 200)
    sb = Slider(0, 600, 400)
    sb.position(25, 75)
    py5.color_mode(py5.HSB)
    py5.no_fill()
    py5.stroke_weight(2)

def draw():
    py5.background(0)
    py5.translate(400, 400)
    py5.rotate_x(py5.QUARTER_PI)
    py5.rotate_y(py5.QUARTER_PI + py5.frame_count / 30)
    py5.stroke(0, 255, 255)
    for _ in range(6):
        py5.circle(0, 0, sa.value)
        py5.rotate_x(py5.PI / 6)
    py5.rotate_y(py5.HALF_PI)
    py5.stroke(128, 255, 255)
    for _ in range(6):
        py5.circle(0, 0, sb.value)
        py5.rotate_x(py5.PI / 6)
    sa.update()
    sb.update()
  
def mouse_wheel(e):
    Slider.mouse_wheel(e)
    
def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    

class Slider:

    template = "{:.1f}"  # para formatar como mostra o valor
    label_align = py5.CENTER
    _sliders = []

    def __init__(self, low, high, default, label=''):
        """
        Slider needs range from low to high
        and and a default value. Label is optional.
        """
        self.low = low
        self.high = high
        self.value = default
        self.label = label
        self.w, self.h = 120, 20
        self.position(25, 25)  # Pos default
        self.IS_3D = py5.get_graphics().is3d()
        self._sliders.append(self)

    def position(self, x, y):
        """Define as coordenadas na tela, e calcula rectx, pos. do 'handle'"""
        self.x = x
        self.y = y
        # the position of the rect you slide:
        self.rectx = self.x + py5.remap(self.value, self.low, self.high, 0, self.w)

    def update(self):
        """Atualiza o slider e devolve o valor (self.value). Chama display()"""
        # is_mouse_pressed moves slider
        if py5.is_mouse_pressed and py5.dist(
            py5.mouse_x, py5.mouse_y, self.rectx, self.y) < self.h:
            self.rectx = py5.mouse_x
        # constrain rectangle
        self.rectx = py5.constrain(self.rectx, self.x, self.x + self.w)
        self.value = py5.remap(self.rectx,
                         self.x, self.x + self.w,
                         self.low, self.high)
        self.display()
        return self.value

    def display(self):
        """Desenha o slider na tela, usando coordenadas sem transformar"""
        py5.push()         # Combina pushMatrix() e pushStyle()
        py5.reset_matrix()  # push(), seguido de resetMatrix() e camera() permitem...
        if self.IS_3D:
            py5.camera()       # .maldino@fediscience.org.. desenhar o slider no sistema de coordenadas original
        py5.rect_mode(py5.CENTER)
        # Linha cinza sob o slider
        py5.stroke_weight(4)
        py5.stroke(200)
        py5.line(self.x, self.y, self.x + self.w, self.y)
        # O retângulo, elemento principal da interface do slider
        py5.stroke_weight(1)
        py5.stroke(0)
        py5.fill(255)
        if self.IS_3D:
            py5.translate(0, 0, 1)
        py5.rect(self.rectx, self.y, self.w / 12, self.h)
        # Mostra o valor (value) atual
        py5.fill(0)
        py5.text_size(10)
        py5.text_align(py5.CENTER, py5.CENTER)
        py5.text(self.template.format(self.value), self.rectx, self.y + self.h)
        # draw label
        if self.label_align == py5.LEFT:
            py5.text_align(self.label_align)
            py5.text(self.label, self.x, self.y - self.h)
        else:
            py5.text(self.label, self.x + self.w / 2, self.y - self.h)
        py5.pop()  # equivale a popStyle() and popMatrix()
        
    def process_wheel(self, wd):
        if py5.dist(
            py5.mouse_x, py5.mouse_y, self.rectx, self.y) < self.h:
            self.rectx += wd        

    @classmethod
    def mouse_wheel(cls, e):
        wd = e.get_count()
        for s in cls._sliders:
            s.process_wheel(wd)
                
                
py5.run_sketch(block=False)
