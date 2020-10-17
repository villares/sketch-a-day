from villares.line_geometry import Line

from random import choice

def setup():
    size(400, 400)
    generate_lines()

def generate_lines():
    global glines
    rw = lambda: choice(range(10, width, 10))
    # glines = [GrowingLine((-width, -height), (width * 2, -height)),
    #          GrowingLine((-width, -height), (-width, height * 2)),
    #          GrowingLine((-width, height * 2), (width * 2, height * 2)),
    #          GrowingLine((width * 2, -height), (width * 2, height * 2)),]
    glines = []
    while len(glines) < 60:
        gl = GrowingLine((rw(), rw()), (rw(), rw()))
        for other_gl in glines:
            if gl.intersect(other_gl):
                break
        else:
            glines.append(gl)

def draw():
    background(0)
    # lines.sort(key = lambda li : li.dist())
    for gl in glines:
        for other_gl in glines:
            gl.check_collision(other_gl)
        # red line
        # if gl.point_over(int(frameCount) % width, height / 2):
        #     stroke(255, 0, 0)
        # else:
        #     stroke(0, 0, 200)
        strokeWeight(2)
        gl.draw()
        gl.check_screen_limit()
        gl.grow()


def keyPressed():
    if key == ' ':
        generate_lines()


def point_in_screen(p):
    return 0 <= v[0] <= width and 0 <= p[1] <= height

class GrowingLine(Line):

    def __init__(self, *args):
        Line.__init__(self, *args)
        self.grow_a = True
        self.grow_b = True

    def draw(self):
        stroke(200 * self.grow_a, 128, 200 * self.grow_b)        
        Line.draw(self)

    def grow(self):
        v = PVector(*self.a) - PVector(*self.b)
        v.normalize()
        # noStroke()
        # fill(0, 255, 200)
        if self.grow_a:
            self.a += v / 2.0
        # else:
        #     circle(self.a.x, self.a.y, 3)
        if self.grow_b:
            self.b -= v / 2.0
        # else:
        #     circle(self.b.x, self.b.y, 3)

    def check_collision(self, other):
        if self is not other:            
            if self.grow_a and other.contains_point(self.a.x,
                                                    self.a.y,
                                                    tolerance=0.01):
                self.grow_a = False
                
            if self.grow_b and other.contains_point(self.b.x,
                                                    self.b.y,
                                                    tolerance=0.01):
                self.grow_b = False
                
    def check_screen_limit(self):
            if not point_in_screen(self.a):
                self.grow_a = False
            if not point_in_screen(self.b):
                self.grow_b = False
