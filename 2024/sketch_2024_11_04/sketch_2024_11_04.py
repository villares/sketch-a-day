import py5

def setup():
    py5.size(600, 600, py5.P3D)
    py5.color_mode(py5.HSB)
    Slider.DEFAULT_W = 150
    Slider(0, 255, 128, 'hue')
    Slider(10, 400, 20, 'size')
    Slider(0, 360, 45, 'rotation')
#     Slider(0, 360, 45, 'rotation') # to test duplicated label
#     Slider(0, 360, 45, '')
#     Slider(0, 360, 45, '')

def draw():
    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_y(py5.radians(Slider.values['rotation']))
    py5.fill(Slider.values['hue'], 255, 255)  # new way of getting values
    py5.box(Slider.values['size'])
    py5.fill(255)
    Slider.update_all()
    
def key_pressed():
    py5.save_frame('out.png')

def mouse_wheel(e):
    Slider.mouse_wheel(e)

class Slider:
    
    DEFAULT_W, DEFAULT_H = 120, 20
    sliders = []
    values = {}   # using labels as keys or obj. reference if label is ''

    def __init__(self, low, high, default, label=''):
        self.low , self.high = low, high
        self.value = default
        self.label = label
        existing_labels = [s.label for s in self.sliders]
        if label and label in existing_labels:
            self.label += str(len(existing_labels))
            print(f'Warning: You already had a slider with label "{label}",')
            print(f'so it was changed to "{self.label}".')
        self.values[self.label or self] = self.value
        
        self.w, self.h = self.DEFAULT_W, self.DEFAULT_H
        self.set_default_position()
        self.sliders.append(self)
        self.is_3D = py5.get_graphics()._instance.is3D()

    def set_default_position(self):
        if not self.sliders:  # default initial position
            self.position(self.DEFAULT_H * 1.25, self.DEFAULT_H * 1.25) 
        else:
            last = self.sliders[-1]
            x = last.x + self.DEFAULT_W * 1.25
            y = last.y
            if x + self.DEFAULT_W > py5.width:
                x = self.DEFAULT_H * 1.25
                y = last.y + self.DEFAULT_H * 2.5
            self.position(x, y)

    def position(self, x, y):
        self.x, self.y = x, y
        self.rectx = self.x + py5.remap(self.value,
                                        self.low, self.high,
                                        0, self.w)

    def update(self):
        if (py5.is_mouse_pressed and
            py5.dist(py5.mouse_x, py5.mouse_y,
                     self.rectx, self.y) < self.h):
            self.rectx = py5.mouse_x
        self.rectx = py5.constrain(self.rectx, self.x, self.x + self.w)
        self.value = py5.remap(self.rectx,
                               self.x, self.x + self.w,
                               self.low, self.high)
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
        if self.is_3D:
            py5.translate(0, 0, 1)
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
                and s.y - s.h / 2 < py5.mouse_y < s.y + s.h / 2):
                s.rectx += event.get_count()

    @classmethod
    def update_all(cls):
        values = {(s.label or s): s.update() for s in cls.sliders}
        cls.values.update(values)
        return values
    
    
py5.run_sketch(block=False)