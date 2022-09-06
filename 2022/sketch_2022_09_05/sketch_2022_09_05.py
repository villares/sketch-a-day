from py5 import Sketch

class SketchySketch(Sketch):
    def __init__(self, title="", other=None):
        self.other = other
        self.title = title
        self.clicked = False
        super().__init__()        

    def settings(self):
        self.size(300, 200)

    def setup(self):
        self.window_resizable(True)
        if self.title:
            self.window_title(self.title)
        if self.other:
            self.other.other = self

    def draw(self): 
        if self.title == 'A':
            self.background(255)
            self.fill(0)
        else:
            self.background(0)
            self.fill(255)
        self.rect(self.mouse_x, self.mouse_y, 10, 10)
        
        if self.clicked:
            w, h = self.width, self.height
            self.fill(128, 128)
            self.circle(w / 2, h / 2, min(w, h) * 0.8)
            
    def mouse_pressed(self):
        self.clicked = not self.clicked
        if self.other:
            self.other.clicked = self.clicked

a = SketchySketch('A')
a.run_sketch(block=False)
b = SketchySketch('B', a)
b.run_sketch(block=False)


