from villares import line_geometry

class Shape:
    
    shapes = []
    
    def __init__(self, points):
        self.points = points[:]
        self.area = line_geometry.poly_area(self.points)
        self.centroid = self.get_centroid()
        self.shapes.append(self)
        
    def display(self):
        colorMode(HSB)
        fill(self.area % 255, 200, 200)
        beginShape()
        for x, y in self.points:
            vertex(x, y)
        endShape(CLOSE)
        
    def mouse_over(self):
        cx, cy = self.centroid
        if dist(mouseX, mouseY, cx, cy) < 50:
            fill(0, 200, 0)
            textAlign(CENTER, CENTER)
            text("{:.0f}".format(self.area), cx, cy)
            self.subdivide()
        
    def get_centroid(self):
        if len(self.points) == 4:
            a, _, c, _ = self.points
            return self.midpoint(a, c)
        else:
            o, m, n = self.points
            return ((o[0] + m[0] + n[0]) / 3.0,    
                    (o[1] + m[1] + n[1]) / 3.0) 
           
    def subdivide(self, mode=None):
        if self.area > 200:
            if len(self.points) == 4:
                a, b, c, d = self.points
                # e = seld.midpoint(a, c)
                Shape((c, d, a))
                Shape((a, b, c))
                self.shapes.remove(self)
            elif len(self.points) == 3:
                o, m, n = self.points
                p = self.midpoint(o, n)
                q = self.midpoint(m, n)
                r = self.midpoint(o, m)
                Shape((m, q, p, r))
                Shape((o, r, p))
                Shape((p, q, n))
                self.shapes.remove(self)
                    
    @staticmethod
    def midpoint(a, b):
        return ((a[0] + b[0]) / 2.0,
                (a[1] + b[1]) / 2.0)
           
    @classmethod
    def update_all(cls):
        for s in cls.shapes:
            s.display()
            s.mouse_over()
        
