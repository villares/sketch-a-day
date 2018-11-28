
# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s334"  # 20181128
OUTPUT = ".png"
NUM = 5
BORDER = 50

#add_library('pdf')
# add_library('gifAnimation')
# from gif_exporter import gif_export

def setup():
    size(500, 500)
    smooth(8)
    init_points(NUM, BORDER)
    background(200)
    #print edges(points)
    #beginRecord(PDF, SKETCH_NAME + ".pdf")
    
def draw():
    #background(200)
    stroke(0, 100)
    strokeWeight(0.1)
    for pair in edges(points):
        l = Line(*pair)
        l.plot()
    strokeWeight(0.5)
    noFill()
    for p in points:
        pass
        #ellipse(p.x, p.y, 7, 7)    
    
        
def keyPressed():
    if key == "n" or key == CODED:
        init_points(NUM, BORDER)
        background(200)
        #saveFrame("###.png")
    if key == "s": saveFrame(SKETCH_NAME + ".png")
    if key == "z":
        new_points = [] 
        for pair in edges(points):
            p = PVector.lerp(pair[0], pair[1], random(0, 1))
            new_points.append(p)
            # l = Line(*pair)
            # l.plot()
            points[:] = new_points
                       

def init_points(grid_size, border=0):
    global points
    #points = create_points(grid_size, border) 
    points = [PVector(random(border, width - border), 
                      random(border, height - border))
              for _ in range(grid_size)]

class Line():
    """ I should change this to a named tuple... """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def plot(self):
        line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
    
    def lerp(self, other, t):
        p1 = PVector.lerp(self.p1, other.p1, t)
        p2 = PVector.lerp(self.p2, other.p2, t)
        return Line(p1, p2)

def edges(poly_points):
    return pairwise(poly_points) + [(poly_points[-1], poly_points[0])]   

def pairwise(iterable):
    import itertools
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b) 
                        
                                    
# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
