from villares.helpers import lerp_tuple

a = [100, 100, 200, 100, 300, 200]
b = [150, 150, 500, 150, 350, 500]


def setup():
    global lerp_slider #, slider_largura 
    size(600, 600)
    lerp_slider = Slider(0, 1, 0.5, 'lerp')
#     slider_largura = Slider(100, 500, 200, 'largura')
#     slider_largura.position(300, 25)
#     
def draw():
    #background(200, 0, 0)
    t = lerp_slider.update()
#     largura = slider_largura.update()
    c = lerp_tuple(a, b, t)
    triangle(*c)



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
        #camera()
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
