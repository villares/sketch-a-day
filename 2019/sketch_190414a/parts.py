

class Face:

    def __init__(self, points, thickness, orientation = (0, 0, 0)):
        self.points = points
        self.thickness = thickness
        self.o = orientation    
        
    def draw_2D(self):
        draw_poly(self.points)

    def draw_3D(self, rot):
        S = 35.28

        t = self.thickness
        pts = self.points
        with pushMatrix():
            translate(0, height/2)
            rotateX(self.o[0] * 0 + rot)
            translate(0, -height/2)
            translate(0, 0, -t/2)
            fill(230)
            draw_poly(pts)
            translate(0, 0, t)
            fill(170)
            draw_poly(pts)
            fill(250)
            for p1, p2 in pairwise(tuple(pts) + (pts[0],)):
                # print((p1, p2))
                beginShape(QUAD_STRIP)
                vertex(p1[0]*S, p1[1]*S, 0)
                vertex(p1[0]*S, p1[1]*S, -t)
                vertex(p2[0]*S, p2[1]*S, 0)
                vertex(p2[0]*S, p2[1]*S, -t)
                endShape()
    
    def edges(self):
         return pairwise(tuple(self.points) + (self.points[0],))
     
def draw_poly(points, closed=True):
        S = 35.28
        beginShape()
        for p in points:
            vertex(p[0]*S, p[1]*S, 0)                    
        if closed:
            endShape(CLOSE)
        else:
            endShape()
            

def pairwise(iterable):
    import itertools
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)     
            
