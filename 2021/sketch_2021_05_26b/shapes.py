from villares import line_geometry

from random import choice

class Shape:
    
    shapes = set()
    
    def __init__(self, *args):
        self.points = args
        self.area = line_geometry.poly_area(self.points)
        self.centroid = self.get_centroid()
        self.shapes.add(self)
        
    def display(self):
        colorMode(HSB)
        h = 15 + (frameCount + self.centroid[0] * 32) % 240
        fill(64 + h / 3, 255, 64 + h)
        # h = 15 + (self.centroid[0] * 32) % 240
        # fill(64 + h / 3, 255, 64 + h)
        beginShape()
        for x, y in self.points:
            vertex(x, y)
        endShape(CLOSE)
        fill(0)
        textAlign(CENTER, CENTER)
        # text("{:.0f} {} {:.0f}".format(self.area, len(self.points) - 2, h),
        #      self.centroid[0], self.centroid[1])
        
    # def mouse_over(self):
    #     cx, cy = self.centroid
    #     if dist(mouseX, mouseY, cx, cy) < 50:
    #         fill(0, 200, 0)
    #         textAlign(CENTER, CENTER)
    #         text("{:.0f}".format(self.area), cx, cy)
    #         self.subdivide()
        
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
                        self.mqpr,
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
        e = self.midpoint(a, c, 0.3)
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
        p = self.midpoint(o, n, 0.6)
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
    def midpoint(a, b, t=0.5):
        return (lerp(a[0], b[0], t),
                lerp(a[1], b[1], t))
           
    @classmethod
    def update_all(cls, divide=False):
        for s in list(cls.shapes):
            s.display()
            # s.mouse_over()
            if divide and random(200) > s.area / 1000.0 or s.area > 10e4:
                    s.subdivide()
        
