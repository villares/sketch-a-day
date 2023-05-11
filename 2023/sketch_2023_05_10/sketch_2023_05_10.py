"""
Inspired by 'follow 3' code from Keith Peters in the Processing examples
you will need to install py5 http://py5coding.org and use the sketch runner
for this is the "imported mode" style.
"""

anchor_pos = 1
adjust_pos = 1

def setup():
    size(500, 500)
    stroke_weight(9)
    color_mode(HSB)
    init_segments()
    
def init_segments():
    Segment.segments = []
    seg = Segment()
    seg.drag((width / 2, width / 2))
    for i in range(100):
        anchor_seg = random_choice(Segment.segments[i//4:])
        new_seg = Segment(link=(anchor_seg, anchor_pos))
        new_seg.length = anchor_seg.length * 0.80
    
                
def draw():
    background(200)
    Segment.update_all()

def mouse_dragged():
    current_mouse = mouse_x, mouse_y
    new_pos = lerp_tuple(Segment.first_seg.start, current_mouse, 0.25)
    Segment.first_seg.drag(new_pos)

def mouse_wheel(e):
    for s in Segment.segments:
        s.length *= (1 + 0.05 * e.get_count())
        s.drag()

def key_pressed():
    if key == ' ':
        init_segments()



class Segment:
    
    segments = []
    first_seg = None
    
    def __init__(self, start=None, end=None, link=None):
        self.start = start if start else (0, 0)
        self.end = end if end else (1, 1)
        self.link = link
        self.length = 60
        if not self.segments:
            self.__class__.first_seg = self
        self.segments.append(self)
        
    def __iter__(self):
        return iter((self.start, self.end))
            
    def drag(self, new_start=None):
        if new_start is None:
            if self.link is None:
                new_start = self.start         
            else:
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
        stroke((self.length * 2) % 255, 200, 128, 128)
        line(*self.start, *self.end)
#         if self.link:
#             points(self.points_at_distance(self.link[0].length, 1.33))
 
    def points_at_distance(self, R, amt):
        xm, ym = lerp_tuple(self.start, self.end, amt)
        (xa, ya), (xb, yb) = self
        d = dist(xa, ya, xb, yb)
        nx, ny = -(ya - yb) / d, (xa - xb) / d
        px, py = nx * R, ny * R 
        xp1 = xm + px
        yp1 = ym + py
        xp2 = xm - px
        yp2 = ym - py
        return ((xp1, yp1), (xp2, yp2))


    def adjust(self):
        if self.link is not None:
            link_obj, amt = self.link
            pa, pb = link_obj.points_at_distance(link_obj.length, adjust_pos)
            random_seed(int(id(self)) + int(self.start[0]/100))
            cp = random_choice((pa, pb))
            self.end = lerp_tuple(self.end, cp, 0.25)

    @staticmethod
    def dist_sorted(po, pa, pb):
        x, y = po
        xa, ya = pa
        xb, yb = pb
        if (x - xa) ** 2 + (y - ya) ** 2 > (x - xb) ** 2 + (y - yb) ** 2:
            return pb, pa
        else:
            return pa, pb

    @classmethod
    def update_all(cls):
        for i, s in enumerate(cls.segments):
            s.adjust()
            s.drag()
            s.draw()

    @classmethod
    def adjust_all(cls):
        for s in cls.segments:
            s.adjust()

def lerp_tuple(a, b, t):   
    return tuple(lerp_tuple(ca, cb, t) if isinstance(ca, tuple)
                 else lerp(ca, cb, t)             
                 for ca, cb in zip(a, b))



