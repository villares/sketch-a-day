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
    for i in range(100):
        anchor_seg = random_choice(Segment.segments[i // 4:])
        new_seg = Segment(link=(anchor_seg, 0.5))
        new_seg.length = anchor_seg.length * 0.90
        
        
def draw():
    background(200)
    if not is_mouse_pressed:
        first_seg.drag((mouse_x, mouse_y))
    if is_key_pressed and key == ' ':
        Segment.shake()
    Segment.update_all()


class Segment:
    
    segments = []
    
    def __init__(self, start=None, end=None, link=None, first=False):
        self.start = start if start else (0, 0)
        self.end = end if end else (0, 0)
        self.link = link
        self.length = 60
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
            stroke((i * 10) % 255, 200, 200, 150)
            s.draw()

    @classmethod
    def shake(cls):
        for i, s in enumerate(cls.segments):
            x, y = s.end
            s.end = x + random(-3, 3), y + random(-3, 3)

def mouse_wheel(e):
    for s in Segment.segments:
        s.length *= (1 + 0.05 * e.get_count())
