"""
Inspired by 'follow 3' code from Keith Peters in the Processing examples
you will need http://py5.pixora.io's sketch runner for imported mode
"""

def setup():
    global first_seg
    size(500, 500)
    stroke_weight(9)
    color_mode(HSB)
    seg = Segment()
    for _ in range(20):
        seg = Segment(link=seg)
        
def draw():
    background(240)
    Segment.segments[0].drag((mouse_x, mouse_y))    
    Segment.update_all()

class Segment:
    
    segments = []
    
    def __init__(self, start=None, end=None, link=None):
        self.start = start if start else (0, 0)
        self.end = end if end else (0, 0)
        self.link = link
        self.length = int(random(2, 5)) * 10
        self.segments.append(self)
            
    def drag(self, new_start=None):
        if new_start is None and self.link is not None:
            new_start = self.link.end
        if new_start:                            
            xs, ys = self.start = new_start
            xe, ye = self.end
            angle = atan2(ys - ye, xs - xe)        
            xe = xs - cos(angle) * self.length
            ye = ys - sin(angle) * self.length
            self.end = xe, ye
 
    def draw(self):
        line(*self.start, *self.end)
        
    @classmethod
    def update_all(cls):
        for i, s in enumerate(cls.segments):
            s.drag()
            stroke((i * 10) % 255, 200, 100, 150)
            s.draw()
        
def mouse_wheel(e):
    for s in Segment.segments:
        s.length += e.getCount() * 5