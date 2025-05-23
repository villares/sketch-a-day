# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s296"  # 20181021
OUTPUT = ".gif"

NUM = 10 
BORDER = 50
SPACING = 10

def setup():
    global poly
    size(500, 500)
    frameRate(5 )
    poly = create_points(non_intersecting=True)
    
def create_points(non_intersecting=True):
    background(200)
    done = False
    while not done:
        poly_points = [PVector(random(BORDER, width - BORDER),
                               random(BORDER, height - BORDER)
                               )
                       for _ in range(NUM)]
        ed = edges(poly_points)
        done = True
        if non_intersecting:
            for p1, p2 in ed[::-1]:
                for p3, p4 in ed[2::]:
                    # test only non consecutive edges
                    if (p1 != p3) and (p2 != p3) and (p1 != p4):
                        if line_instersect(Line(p1, p2), Line(p3, p4)):
                            done = False
                            break
    return poly_points
    

def draw():
    background(200)
    SPACING = 10 + frameCount % 20
    
    stroke(200, 0, 0)
    strokeWeight(3) 
    for p1, p2 in edges(poly):
        line(p1.x, p1.y, p2.x, p2.y)   
       
    fill(0, 0, 200)
    for x in range(0, width, SPACING):
        for y in range(0, height, SPACING):
            if is_inside(x, y, poly):
                ellipse(x, y, SPACING/2, SPACING/2)
                    
    if SPACING > 10:
        saveFrame("a##.png")    
   
   
def is_inside(x, y, poly_points):   
    min_, max_ = min_max(poly_points)
    strokeWeight(0.5)
    stroke(0)
    line(x, min_.y, x, max_.y)
    line(min_.x, y, max_.x, y)
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

    
def keyPressed():
    global poly
    if key == " ": 
        poly = create_points(True)
    if key == "s": saveFrame("###.png")
        
        
class Line():
    """ I should change this to a named tuple... """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    
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

# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
