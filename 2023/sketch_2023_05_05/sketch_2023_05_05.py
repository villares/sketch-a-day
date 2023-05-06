"""
Inspired by 'follow 3' code from Keith Peters in the Processing examples
you will need to install py5 http://py5coding.org and use the sketch runner
for this is the "imported mode" style.
"""

def setup():
    global first_seg
    size(500, 500)
    stroke_weight(9)
    color_mode(HSB)
    first_seg = seg = Segment(first=True)
    for _ in range(10):
        seg = Segment(link=(seg, 0.66))
        seg2 = Segment(link=(seg, 1))

def draw():
    background(240)
    first_seg.drag((mouse_x, mouse_y))
    if is_key_pressed:
        Segment.wind()
    Segment.update_all()

class Segment:
    
    segments = []
    
    def __init__(self, start=None, end=None, link=None, first=False):
        self.start = start if start else (0, 0)
        self.end = end if end else (0, 0)
        self.link = link
        self.length = 40
        self.segments.append(self)
        self.first = first
            
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

    @classmethod
    def wind(cls):
        for i, s in enumerate(cls.segments):
            if not s.first:
                x, y = s.end
                s.end = x - 1, y -1

def mouse_wheel(e):
    for s in Segment.segments:
        s.length += e.get_count() * 5
