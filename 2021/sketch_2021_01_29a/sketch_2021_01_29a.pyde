
from random import choice
from villares.line_geometry import Line, point_in_screen
from villares.arcs import var_bar

def setup():
    size(500, 500)
    generate_lines()

def generate_lines():
    global glines
    rw = lambda: choice(range(-width / 2 + 20, width / 2, 50))
    step = lambda n: n + choice((-20, 5))
    # step = lambda n: n + choice((-5,-15))

    glines = []
    while len(glines) < 100:
        xa, ya = rw() ,rw()
        xb, yb = step(xa), step(ya)
        gl = GrowingLine((xa, ya), (xb, yb))
        for other_gl in glines:
            if len(set((gl[0], gl[1], other_gl[0], other_gl[1]))) < 4:
                break
            if  gl.intersect(other_gl):
                break
        else:
            glines.append(gl)

def draw():
    translate(width / 2, height / 2)
    # rotate(radians(13))
    background(0)
    for gl in glines:
        for other_gl in glines:
            gl.check_collision(other_gl)
        strokeWeight(2)
        gl.stroke_from_growth()
        gl.draw()
        gl.check_screen_limit()
        gl.grow()

def keyPressed():
    if key == ' ':
        generate_lines()

class GrowingLine(Line):

    def __init__(self, *args):
        Line.__init__(self, *args)
        self.grow_a = True
        self.grow_b = True

    def stroke_from_growth(self):
        colorMode(HSB)
        stroke(map(self.dist(), 0, height * .75, 0, 256),
               255 - 128 * self.grow_a,
               255 - 128 * self.grow_b)
        # stroke(200 * self.grow_a, 128, 200 * self.grow_b)

    def grow(self):
        v = PVector(*self[0]) - PVector(*self[1])
        v.normalize()
        # noStroke()
        # fill(0, 255, 200)
        r = PVector() #.random2D()
        if self.grow_a:
            self[0] += v + r
        # else:
        #     circle(self[0].x, self[0].y, 3)
        if self.grow_b:
            self[1] -= v + r
        # else:
        #     circle(self[1].x, self[1].y, 3)

    def check_collision(self, other):
        if self != other:
            if self.grow_a and other.contains_point(self[0].x,
                                                    self[0].y,
                                                    tolerance=0.1):
                self.grow_a = False
                # glines.remove(other)
                # glines[0]ppend(GrowingLine(self[0], other[1]))
            if self.grow_b and other.contains_point(self[1].x,
                                                    self[1].y,
                                                    tolerance=0.1):
                self.grow_b = False
                # if other in glines: glines.remove(other)
                # glines[0]ppend(GrowingLine(other[0], self[1]))
        # else:
        #     glines.remove(self)

    def check_screen_limit(self):
        # sp = lambda p: PVector(screenX(p.x, p.y), screenY(p.x, p.y))
        if self.grow_a and not point_in_screen(self[0]):
            self.grow_a = False
        if self.grow_b and not point_in_screen(self[1]):
            self.grow_b = False

    def draw(self):
          noFill()
          var_bar(self[0][0], self[0][1], self[1][0], self[1][1], 5, shorter=30)
                                 
