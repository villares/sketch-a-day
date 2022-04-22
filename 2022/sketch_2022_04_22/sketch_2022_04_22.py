"""
Inspired by 'follow 3' code from Keith Peters in the Processing examples
you will need http://py5.pixora.io's sketch runner for imported mode
"""

def setup():
    global first_seg
    size(500, 500)
    stroke_weight(9)
    color_mode(HSB)
    first_seg = seg = Segment()
    for _ in range(20):
        seg = Segment(link=(seg, 0.5))

def draw():
    background(240)
    first_seg.drag((mouse_x, mouse_y))
    Segment.update_all()

class Segment:
    
    segments = []
    
    def __init__(self, start=None, end=None, link=None):
        self.start = start if start else (0, 0)
        self.end = end if end else (0, 0)
        self.link = link
        self.length = 40
        self.segments.append(self)
            
    def drag(self, new_start=None):
        if new_start is None and self.link is not None:
            link_obj, amt = self.link
            (xs, ys), (xe, ye) = link_obj.start, link_obj.end
            new_start = lerp(xs, xe, amt), lerp(ys, ye, amt)
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
