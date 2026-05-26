# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5

elements = []
new_elements = []
updates = False

def setup():
    global b
    py5.size(600, 600)
    py5.no_stroke()
    py5.color_mode(py5.CMAP, 'viridis', 15)
    py5.background('black')
        
def draw():
    global b
    b = py5.get_graphics().copy()
    py5.background('black')
    for e in elements:
        e.update()
    elements.extend(new_elements)
    new_elements.clear()
    

def key_pressed():
    global updates
    
    if py5.key == 's':
        py5.save_frame('###.png')                                    
    elif py5.key == 'c':
        if elements:
            elements.clear()
        else:
            elements.append(Element(300, 300))
    elif py5.key == ' ':
        updates = not updates


class Element:
    
    def __init__(self, x=0, y=0):
        self.pos = py5.Py5Vector(x, y)
        self.d = py5.random_int(5, 20)
        self.state = True
        
    def __bool__(self):
        return self.state
    
    def update(self):
        py5.fill(self.d - 5)
        py5.circle(*self.pos, self.d)
        if updates and self.state:
            for _ in  range(py5.random_int(1, 2)):
                v = py5.Py5Vector.random(2)
                new_pos = (v * self.d * 0.55) + self.pos
                c = b.get_pixels(int(new_pos.x), int(new_pos.y))
                if c == py5.color('black'):
                    n = Element()
                    n.pos = self.pos + v * (self.d / 2 +  n.d /2)
                    new_elements.append(n)
            self.stae = False
        
py5.run_sketch(block=False)
        

