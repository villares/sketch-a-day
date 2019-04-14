

class Face:

    def __init__(self, points, thickness, orientation = (1, 0, 0)):
        self.points = points
        self.thickness = thickness
        self.o = orientation    
        
    def draw_2D(self):
        fill(100, 100, 200)
        draw_poly(self.points)

    def draw_3D(self, rot):
        S = 35.28

        t = self.thickness
        pts = self.points
        with pushMatrix():
            translate(width/2, height/2)
            rotateX(self.o[0] * HALF_PI + rot)
               # self.o[1] * HALF_PI,
               # self.o[2] * HALF_PI)
            translate(0, 0, -t/2)
            fill(100, 200, 100)
            draw_poly(pts)
            translate(0, 0, t)
            fill(100, 100, 200)
            draw_poly(pts)
            fill(200, 100, 100)
            for p1, p2 in pairwise(tuple(pts) + (pts[0],)):
                # print((p1, p2))
                beginShape(QUAD_STRIP)
                vertex(p1[0]*S, p1[1]*S, 0)
                vertex(p1[0]*S, p1[1]*S, -t)
                vertex(p2[0]*S, p2[1]*S, 0)
                vertex(p2[0]*S, p2[1]*S, -t)
                endShape()
    
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
            
