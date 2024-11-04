from itertools import product
import numpy as np

salvar_png = salvar_pdf = False

def setup():
    global screen_grid, noise_space_grid, len_grid
    global slider_escala, slider_tam

    size(400, 400)
    color_mode(HSB)
    stroke_cap(PROJECT) 
    stroke_weight(5)
    slider_escala = Slider(0.1, 5, 1, 'escala')
    slider_escala.position(100, height - 20)
    slider_tam = Slider(2, 100, 20, 'tamanho')
    slider_tam.position(300, height - 20)
    
def draw():
    noise_seed(1)
    
    grid = list(product(range(0, height, 5), range(0, width, 5)))
    len_grid = len(grid)
    screen_grid = np.array((grid))
    
    tam = slider_tam.value
    step_scale = 1 / slider_escala.value
    
    global salvar_pdf, salvar_png# para poder desligar a bandeirinha
    if salvar_pdf:
        begin_record(PDF, 'reticula.pdf')

    background(0)
    rect_mode(CENTER)
    offset = np.array((-mouse_x * 10, -mouse_y * 10))
    t = frame_count * 10 * step_scale
    noise_space_grid = (screen_grid + offset) * step_scale
    noise_values = os_noise(
        noise_space_grid[:,0],
        noise_space_grid[:,1],
        np.full(len_grid, t)
    )
    remapped_values = (noise_values + 1) / 2 * 255  # could have been remap()
    colored_points(screen_grid[:,0], screen_grid[:,1], remapped_values)
    
    if salvar_pdf:
        end_record()
        print('terminando de salvar o PDF')
        salvar_pdf = False
    
    if salvar_png:
        salvar_png = False
        save_frame('out.png')
    else:
        rect_mode(CORNER)
        color_mode(RGB)
        fill(0, 100)
        no_stroke()
        rect(0, height - 30, width, 30)
        slider_tam.update()
        slider_escala.update()
      
def key_pressed():
    global salvar_pdf, salvar_png
    if key == 'p':
        salvar_pdf = True
    if key == 's':
        salvar_png = True


@np.vectorize
def colored_points(x, y, n):
    stroke(n, 255, 255)
    point(x, y)
# at some point I should try a Py5Shape with py5.begin_shape(py5.POINTS)
# & vertices() & set_strokes() but I'm tired
 

class Slider:

    def __init__(self, low, high, default, label=''):
        self.low , self.high = low, high
        self.value = default
        self.label = label
        self.w, self.h = 120, 20
        self.position(25, 25)  # default position

    def position(self, x, y):
        self.x, self.y = x, y
        self.rectx = self.x + remap(self.value, self.low, self.high, 0, self.w)

    def update(self):
        if is_mouse_pressed and dist(mouse_x, mouse_y, self.rectx, self.y) < self.h:
            self.rectx = mouse_x
        self.rectx = constrain(self.rectx, self.x, self.x + self.w)
        self.value = remap(self.rectx, self.x, self.x + self.w, self.low, self.high)
        self.display()
        return self.value
        
    def display(self):
        push()  # combina pushMatrix() and pushStyle()
        reset_matrix()
        camera()
        rect_mode(CENTER)
        stroke_weight(4)
        stroke(200)
        line(self.x, self.y, self.x + self.w, self.y)
        stroke_weight(1)
        stroke(0)
        line(self.x + self.w / 24, self.y, self.x + self.w - self.w / 24, self.y)
        fill(255)
        stroke(0)
        rect(self.rectx, self.y, self.w / 12, self.h)
        fill(0)
        text_align(CENTER, CENTER)
        text("{:.1f}".format(self.value), self.rectx, self.y + self.h)
        text(self.label, self.x + self.w / 2, self.y - self.h)
        pop()  # popStyle() and popMatrix