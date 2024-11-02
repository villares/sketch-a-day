
ox_imagem = 0  # deslocamento do início da leitura dos pixels
oy_imagem = 0  # offset em y para início da leitura da imagem

salvar_pdf = False

def setup():
    global img
    size(800, 600)
    img = load_image('foto-ba.jpg')
    global slider_escala, slider_tam
    slider_escala = Slider(0.1, 20, 2, 'escala')
    slider_escala.position(100, height - 20)
    slider_tam = Slider(2, 50, 10, 'tamanho')
    slider_tam.position(300, height - 20)
    
    
def draw():
    
    tam = slider_tam.value
    escala = 1 / slider_escala.value
    
    global salvar_pdf # para poder desligar a bandeirinha
    if salvar_pdf:
        begin_record(PDF, 'reticula.pdf')

    background(0)
    rect_mode(CENTER)
    num_colunas = int(width / tam)
    num_filas = int(height / tam)
    for coluna in range(num_colunas): # 0, 1 ... 
        x_tela = coluna * tam + tam / 2
        for fila in range(num_filas):
            y_tela = fila * tam + tam / 2
            x_imagem = int(ox_imagem + x_tela * escala)
            y_imagem = int(oy_imagem + y_tela * escala)
            cor = img.get_pixels(x_imagem, y_imagem)
            matiz = hue(cor)
            bri = brightness(cor) # 0 a 255
            color_mode(HSB)
            fill(matiz, 255, 255) # fill(255) para PB
            square(x_tela, y_tela, bri / 255 * tam)
    
    if salvar_pdf:
        end_record()
        print('terminando de salvar o PDF')
        salvar_pdf = False
    
    rect_mode(CORNER)
    color_mode(RGB)
    fill(0, 100)
    rect(0, height - 30, width, 30)
    slider_tam.update()
    slider_escala.update()
      
def key_pressed():
    global salvar_pdf
    if key == 'p':
        salvar_pdf = True
        

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