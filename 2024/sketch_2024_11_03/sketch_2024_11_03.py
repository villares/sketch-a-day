import py5

def setup():
    global slider_a, slider_b
    py5.size(400, 400)
    py5.color_mode(py5.HSB)
    slider_a = Slider(0, 255, 128, 'hue')
    slider_b = Slider(10, 400, 20, 'size')
    
def draw():
    py5.background(0)
    py5.fill(slider_a.value, 255, 255)
    py5.circle(200, 200, slider_b.value)
    py5.fill(255)
    Slider.update_all()
    
def key_pressed():
    py5.save_frame('out.png')

def mouse_wheel(e):
    Slider.mouse_wheel(e)

class Slider:
    sliders = []

    def __init__(self, low, high, default, label=''):
        self.low , self.high = low, high
        self.value = default
        self.label = label
        self.w, self.h = 120, 20
        self.set_default_position()
        self.sliders.append(self)
        self.is_3D = py5.get_graphics()._instance.is3D()

    def set_default_position(self):
        if not self.sliders:
            self.position(25, 25)  # default position
        else:
            last = self.sliders[-1]
            x = last.x + 150
            y = last.y
            if x + 120 > py5.width:
                x = 25
                y = last.y + 50
            self.position(x, y)

    def position(self, x, y):
        self.x, self.y = x, y
        self.rectx = self.x + py5.remap(self.value, self.low, self.high, 0, self.w)

    def update(self):
        if (py5.is_mouse_pressed and
            py5.dist(py5.mouse_x, py5.mouse_y,
                     self.rectx, self.y) < self.h):
            self.rectx = py5.mouse_x
        self.rectx = py5.constrain(self.rectx, self.x, self.x + self.w)
        self.value = py5.remap(self.rectx, self.x, self.x + self.w, self.low, self.high)
        self.display()
        return self.value
        
    def display(self):
        py5.push_matrix()  
        py5.reset_matrix()
        py5.push_style()
        if self.is_3D:
            py5.camera()
        py5.rect_mode(py5.CENTER)
        py5.stroke_weight(4)
        py5.stroke(200)
        py5.line(self.x, self.y, self.x + self.w, self.y)
        py5.stroke_weight(1)
        py5.stroke(0)
        py5.line(self.x + self.w / 24, self.y,
                 self.x + self.w - self.w / 24, self.y)
        py5.fill(255)
        py5.stroke(0)
        py5.rect(self.rectx, self.y, self.w / 12, self.h)
        py5.pop_style()
        py5.text_align(py5.CENTER, py5.CENTER)
        py5.text("{:.1f}".format(self.value), self.rectx, self.y + self.h)
        py5.text(self.label, self.x + self.w / 2, self.y - self.h)
        py5.pop_matrix()  
        
    @classmethod
    def mouse_wheel(cls, event):
        for s in cls.sliders:
            if (s.x < py5.mouse_x < s.x + s.w
                and s.y < py5.mouse_y < s.y + s.h):
                s.rectx += event.get_count()

    @classmethod
    def update_all(cls):
        for s in cls.sliders:
            s.update()
            
py5.run_sketch(block=False)