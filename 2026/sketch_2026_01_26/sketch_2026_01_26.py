from random import choice

def setup():
    global ds
    size(1024, 1024)
    Shape((0, 0), (width, 0), (width, height), (0, height))
    no_loop()
    stroke_weight(0.5)
    
    
def draw():
    background(0)
    Shape.update_all()

def key_pressed():
    if key == ' ':
        Shape.update_all(divide=True)
    elif key == 'r':
        Shape.shapes.clear()
        Shape((0, 0), (width, 0), (width, height), (0, height))
    elif key == 's':
        save_frame('###.png')
    redraw()


class Shape:
    
    shapes = set()
    
    def __init__(self, *args):
        self.points = args
        self.area = self.poly_area(self.points)
        self.centroid = self.get_centroid()
        self.shapes.add(self)
        
    def display(self):
        color_mode(HSB)
        # no_stroke()
        h = 32 + (self.centroid[1] * 32) % 223
        fill(64 + h / 3, 255, 64 + h)
        # h = 15 + (self.centroid[0] * 32) % 240
        # fill(64 + h / 3, 255, 64 + h)
        with begin_closed_shape():
            vertices(self.points)
        # fill(0)
        # text_align(CENTER, CENTER)
        # text("{:.0f} {} {:.0f}".format(self.area, len(self.points) - 2, h),
        #      self.centroid[0], self.centroid[1])
        
        
    def get_centroid(self):
        if len(self.points) == 4:
            a, _, c, _ = self.points
            return self.midpoint(a, c)
        else:
            o, m, n = self.points
            return ((o[0] + m[0] + n[0]) / 3.0,    
                    (o[1] + m[1] + n[1]) / 3.0) 
           
    def subdivide(self, mode=None):
        if self.area > 64:
            if len(self.points) == 4:
                choice((self.cda_abc,
                        self.dab_bcd,
                        self.afei,
                        self.ifgh,
                        ))()
            elif len(self.points) == 3:
                choice((self.opm_npm,
                        self.mqpr,
                        #self.mqpr,
                        ))()
            self.shapes.remove(self)    
            
    def ifgh(self): 
        a, b, c, d = self.points
        e = self.midpoint(a, c)
        f = self.midpoint(a, b)
        g = self.midpoint(b, c)
        h = self.midpoint(d, c)
        i = self.midpoint(d, a)
        Shape(i, f, g, h)
        Shape(i, a, f)
        Shape(f, b, g)
        Shape(g, c, h)
        Shape(h, d, i)
            
    def afei(self): 
        a, b, c, d = self.points
        e = self.midpoint(a, c)
        f = self.midpoint(a, b)
        g = self.midpoint(b, c)
        h = self.midpoint(d, c)
        i = self.midpoint(d, a)
        Shape(a, f, e, i)
        Shape(f, b, g, e)
        Shape(e, g, c, h)
        Shape(i, e, h, d)
                        
    def opm_npm(self): 
        o, m, n = self.points
        p = self.midpoint(o, n)
        Shape(o, p, m)
        Shape(n, p, m)

    def mqpr(self):
        o, m, n = self.points
        p = self.midpoint(o, n)
        q = self.midpoint(m, n)
        r = self.midpoint(o, m)
        Shape(m, q, p, r)
        Shape(o, r, p)
        Shape(p, q, n)
            
    def dab_bcd(self):
        a, b, c, d = self.points
        Shape(d, a, b)
        Shape(b, c, d)

    def cda_abc(self):
        a, b, c, d = self.points
        Shape(c, d, a)
        Shape(a, b, c)
                    
                                        
    @staticmethod
    def midpoint(a, b):
        return ((a[0] + b[0]) / 2.0,
                (a[1] + b[1]) / 2.0)
    
    @staticmethod
    def poly_area(pts):
        pts = list(pts)
        area = 0.0
        for (ax, ay), (bx, by) in zip(pts, pts[1:] + [pts[0]]):
            area += ax * by
            area -= bx * ay
        return abs(area) / 2.0


    @classmethod
    def update_all(cls, divide=False):
        for s in list(cls.shapes):
            s.display()
            # s.mouse_over()
            if divide and random(200) > s.area / 1000.0 or s.area > 10e4:
                    s.subdivide()
        