n = 6

def setup():
    global slider_altura, slider_largura
    size(700, 700)
    slider_largura = Slider(0, 200, 50, 'W')  # min, max, ini, "nome"
    slider_altura = Slider(0, 200, 50, 'H')  # min, max, ini, "nome"
    slider_largura.position(25, 25)
    slider_altura.position(170, 25)

def draw():
    largura = slider_largura.update()
    altura = slider_altura.update()
    background(altura % 255, largura % 255, 128)
    translate(width / 2, height / 2)
    for _ in range(n):
        rotate(TWO_PI / n)
        if largura >= 10 and altura >= 10:
            rect(20, 20, largura, altura)
    slider_largura.display()
    slider_altura.display()
    
    
def key_pressed():
    global n
    if key_code == UP:
        n += 1
    if key_code == DOWN and n > 5:
        n -= 1

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