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
        new_seg = Segment(link=(anchor_seg, random(0.4, 0.6)))
        new_seg.length = anchor_seg.length * 0.90
                
def draw():
    background(200)
    if is_key_pressed and key == ' ':
        Segment.adjust_all()
    Segment.update_all()

def mouse_dragged():
    first_seg.drag(lerp_tuple(first_seg.start, (mouse_x, mouse_y), 0.5))

def mouse_wheel(e):
    for s in Segment.segments:
        s.length *= (1 + 0.05 * e.get_count())


class Segment:
    
    segments = []
    
    def __init__(self, start=None, end=None, link=None, first=False):
        self.start = start if start else (0, 0)
        self.end = end if end else (0, 0)
        self.link = link
        self.length = 60
        self.segments.append(self)
        self.first = first
        
    def __iter__(self):
        return iter((self.start, self.end))
            
    def drag(self, new_start=None):
        if new_start is None and self.link is not None:
            link_obj, amt = self.link
            start, end = link_obj
            new_start = lerp_tuple(start, end, amt)
        if new_start:                            
            xs, ys = self.start = new_start
            xe, ye = self.end
            angle = atan2(ys - ye, xs - xe)        
            xe = xs - cos(angle) * self.length
            ye = ys - sin(angle) * self.length
            self.end = xe, ye
        
    def draw(self):
        line(*self.start, *self.end)        
        #points(self.points_at_distance(self.length))
 
    def points_at_distance(self, R):
        (xa, ya), (xb, yb) = self
        xm = (xa + xb) / 2
        ym = (ya + yb) / 2
        if xb == xa:
            m_perp = 0
            xp1 = xm + R
            xp2 = xm - R
            yp1 = ym
            yp2 = ym
        else:
            m = (yb - ya) / (xb - xa)
            m_perp = -1 / m
            a = 1 + 1 / m_perp**2
            b = -2 * ym * (1 + 1 / m_perp**2)
            c = ym**2 * (1 + 1 / m_perp**2) - R**2
            yp1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
            yp2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
            xp1 = (yp1 - ym) / m_perp + xm
            xp2 = (yp2 - ym) / m_perp + xm
        return ((xp1, yp1), (xp2, yp2))

    def adjust(self):
        if self.link is not None:
            link_obj, amt = self.link
            pa, pb = link_obj.points_at_distance(link_obj.length)
            cp = self.closer(self.end, pa, pb)
#            self.end = lerp_tuple(self.end, cp, 0.5)
            self.end = lerp_tuple(self.end, cp, 0.25)

    @staticmethod
    def closer(po, pa, pb):
        x, y = po
        xa, ya = pa
        xb, yb = pb
        if (x - xa) ** 2 + (y - ya) ** 2 > (x - xb) ** 2 + (y - yb) ** 2:
            return pb
        else:
            return pa

    @classmethod
    def update_all(cls):
        for i, s in enumerate(cls.segments):
            s.drag()
            stroke((i * 10) % 255, 200, 200, 150)
            s.draw()

    @classmethod
    def adjust_all(cls):
        for s in cls.segments:
            s.adjust()

def lerp_tuple(a, b, t):   
    return tuple(lerp_tuple(ca, cb, t) if isinstance(ca, tuple)
                 else lerp(ca, cb, t)             
                 for ca, cb in zip(a, b))
