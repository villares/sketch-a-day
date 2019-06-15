
def intersecting(poly_points):
    ed = edges(poly_points)
    intersect = False
    for p1, p2 in ed[::-1]:
        for p3, p4 in ed[2::]:
            # test only non consecutive edges
            if (p1 != p3) and (p2 != p3) and (p1 != p4):
                if line_instersect(Line(p1, p2), Line(p3, p4)):
                    intersect = True
                    break
    return intersect
     
def is_inside(x, y, poly_points):   
    min_, max_ = min_max(poly_points)
    if x < min_.x or y < min_.y or x > max_.x or y > max_.y:
        return False
    
    a = PVector(x, min_.y)
    b = PVector(x, max_.y)
    v_lines = inter_lines(Line(a, b), poly_points)
    if not v_lines:
        return False
        
    a = PVector(min_.x, y)
    b = PVector(max_.x, y)
    h_lines = inter_lines(Line(a, b), poly_points)
    if not h_lines:
        return False
                
    for v in v_lines:
        for h in h_lines:
            if line_instersect(v, h):
                return True   
                         
    return False


def inter_lines(L, poly_points):
    inter_points = []
    for p1, p2 in edges(poly_points):
        inter = line_instersect(Line(p1, p2), L)
        if inter:
            inter_points.append(inter)
    if  not inter_points:
        return []
    inter_lines = []
    if len(inter_points) > 1:
        inter_points.sort()
        pairs = zip(inter_points[::2], inter_points[1::2])
        for p1, p2 in pairs:
            if p2:
                inter_lines.append(Line(PVector(p1.x, p1.y),
                                        PVector(p2.x, p2.y))) 
    return inter_lines

        
class Line():
    """ I should change this to a named tuple... """
    def __init__(self, p1, p2):
        self.p1 = PVector(*p1)
        self.p2 = PVector(*p2) 
    
    def __getitem__(self, i):
        return (self.p1, self.p2)[i]
        
    def plot(self):
        line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
    
    def lerp(self, other, t):
        p1 = PVector.lerp(self.p1, other.p1, t)
        p2 = PVector.lerp(self.p2, other.p2, t)
        return Line(p1, p2)
    
def line_instersect(line_a, line_b):     
    """
    code adapted from Bernardo Fontes 
    https://github.com/berinhard/sketches/
    """
    x1, y1 = line_a.p1.x, line_a.p1.y
    x2, y2 = line_a.p2.x, line_a.p2.y
    x3, y3 = line_b.p1.x, line_b.p1.y
    x4, y4 = line_b.p2.x, line_b.p2.y
    try:
        uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
        uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
    except ZeroDivisionError:
        return
    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return
    x = line_a.p1.x + uA * (line_a.p2.x - line_a.p1.x)
    y = line_a.p1.y + uA * (line_a.p2.y - line_a.p1.y)
        
    return PVector(x, y)
    # """
    # code adapted from 
    # https://stackoverflow.com/questions/27745972/test-if-polylines-intersects-using-python
    # """
    # xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    # ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    # def det(a, b):
    #     return a[0] * b[1] - a[1] * b[0]

    # div = det(xdiff, ydiff)
    # if div == 0:
    #    return None

    # d = (det(*line1), det(*line2))
    # x = det(d, xdiff) / div
    # y = det(d, ydiff) / div
    # return x, y
    # return PVector(x, y)


def edges(poly_points):
    return pairwise(poly_points) + [(poly_points[-1], poly_points[0])]   

def pairwise(iterable):
    import itertools
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b) 

def min_max(points):
        points = iter(points)
        try:
            p = points.next()
            min_x, min_y = max_x, max_y = p.x, p.y
        except StopIteration:
            raise ValueError, "min_max requires at least one point"
        for p in points:
            if p.x < min_x:
                min_x = p.x
            elif p.x > max_x:
                max_x = p.x
            if p.y < min_y:
                min_y = p.y
            elif p.y > max_y:
                max_y = p.y
        return (PVector(min_x, min_y),
                PVector(max_x, max_y))
        
def par_hatch(points, divisions, *sides):
        vectors = [PVector(p.x, p.y) for p in points]
        lines = []
        if not sides: sides = [0]
        for s in sides:
            a, b = vectors[-1 + s], vectors[+0 + s]
            d, c = vectors[-2 + s], vectors[-3 + s]
            for i in range(1, divisions):
                s0 = PVector.lerp(a, b, i/float(divisions))
                s1 = PVector.lerp(d, c, i/float(divisions))
                lines.append(Line(s0, s1)) 
        return lines
