# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5

elements = []
new_elements = []
updates = False

def setup():
    py5.size(600, 600)
    py5.no_stroke()
            
def draw():
    py5.background(0)
    for e in elements:
        e.update()
    elements.extend(new_elements)
    new_elements.clear()
    print(py5.get_pixels(py5.mouse_x, py5.mouse_y))

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
    
    def __init__(self, x, y):
        self.pos = py5.Py5Vector(x, y)
        self.d = py5.random_int(5, 20)
        self.state = True
        
    def __bool__(self):
        return self.state
    
    def update(self):
        py5.fill(255, 100)
        py5.circle(*self.pos, self.d)
        if updates and self.state:
            for _ in  range(2):
                new_pos = py5.Py5Vector.random(2) * (self.d * 2) + self.pos
                if py5.get_pixels(int(new_pos.x), int(new_pos.y)) == py5.color(0):
                    n = Element(new_pos.x, new_pos.y)
                    new_elements.append(n)
            self.stae = False
        
py5.run_sketch(block=False)
        

