
from random import choice
from villares.line_geometry import Line, point_in_screen

def setup():
    size(400, 400)
    generate_lines()

def generate_lines():
    global glines
    rw = lambda: choice(range(-width / 2, width / 2, 10))
    glines = []
    while len(glines) < 60:
        gl = GrowingLine((rw(), rw()), (rw(), rw()))
        for other_gl in glines:
            if gl.intersect(other_gl) or gl.a == gl.b:
                break
        else:
            glines.append(gl)

def draw():
    fill(0, 10)
    rect(0, 0, width, height)

    translate(width / 2, height / 2)
    # scale(.5)
    rotate(frameCount / 200.0)
    # background(0)
    for gl in glines:
        for other_gl in glines:
            gl.check_collision(other_gl)
        strokeWeight(2)
        gl.stroke_from_growth()
        # red line
        # if gl.point_over(int(frameCount) % width, height / 2):
        #     stroke(255, 0, 0)
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
        stroke(200 * self.grow_a, 128, 200 * self.grow_b)

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
        if self != other:
            if self.grow_a and other.contains_point(self.a.x,
                                                    self.a.y,
                                                    tolerance=0.01):
                self.grow_a = False
                # glines.remove(other)
                # glines.append(GrowingLine(self.a, other.b))
            if self.grow_b and other.contains_point(self.b.x,
                                                    self.b.y,
                                                    tolerance=0.01):
                self.grow_b = False
                # if other in glines: glines.remove(other)
                # glines.append(GrowingLine(other.a, self.b))
        # else:
        #     glines.remove(self)

    def check_screen_limit(self):
        sp = lambda p: PVector(screenX(p.x, p.y), screenY(p.x, p.y))
        if self.grow_a and not point_in_screen(sp(self.a)):
            self.grow_a = False
        if self.grow_b and not point_in_screen(sp(self.b)):
            self.grow_b = False
