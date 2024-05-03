"""
s180109 Balls for Manoloid!
(c)2018 Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
This is directly inspired by & derived from 
Manuel Gamboa Naon's sketch 
https://gist.github.com/manoloide/16ea9e1d68c6ba1700fcb008fd38aab0
posted at twitter.com/manoloidee
"""

mm = 0

def setup():
    size(720, 720)
    generate()
    ellipse_mode(CORNER)
    color_mode(HSB)

def draw():
    global mx, my, mm, time
    mm *= 0.95
    # if (mm < 0.04) mm *= 0.2
    mx = mouse_x - width / 2
    my = mouse_y - height / 2
    time = millis() * 0.001
    background(190)

    translate(width / 2, height / 2)

    for c in circles:
        c.update()
        c.showShadow()
        c.show()


def key_pressed():
    generate()


def mouse_moved():
    global mm
    mm += 0.05
    sub()

def sub():
    for c in circles:
        if c.isOn(mx, my):
            c.sub()
            break


def generate():
    global circles
    circles = []
    circles.append(Circle(-300, -300, 600, color(random(256), 200, 200)))


class Circle:

    def __init__(self, x, y, size_, color_):
        self.x = x
        self.y = y
        self.ix = x
        self.iy = y
        self.s = size_
        self.b = 10
        self.ncol = color(random(256), 200, 200)
        self.col = color_

    def mouseMovement(self):
        cx = self.x + self.s * 0.5
        cy = self.y + self.s * 0.5
        maxDist = 200
        dis = dist(cx, cy, mx, my)
        ang = atan2(cy - my, cx - mx)
        if (dis < maxDist):
            dd = remap(dis, 0, maxDist, 1, 0)
            dd = pow(dd, 0.9) * 20 * mm
            self.x += cos(ang) * dd
            self.y += sin(ang) * dd

    def update(self):

        self.x = lerp(self.x, self.ix, 0.09)
        self.y = lerp(self.y, self.iy, 0.09)
        self.col = lerp_color(self.col, self.ncol, 0.05)

        self.mouseMovement()

    def showShadow(self):
        no_stroke()
        fill(0, 20)
        ellipse(self.x + self.b, self.y + self.b, self.s, self.s)

    def show(self):
        stroke(255, 2)
        fill(self.col)
        ellipse(self.x, self.y, self.s, self.s)

    def isOn(self, mx, my):
        return (self.x + self.s > mx >= self.x and
                self.y + self.s > my >= self.y)

    def sub(self):
        ms = self.s * 0.5

        c = Circle(self.ix, self.iy + ms, ms, self.col)
        circles.append(c)

        c = Circle(self.ix, self.iy, ms, self.col)
        c.x += self.x - self.ix
        c.y += self.y - self.iy
        circles.append(c)

        c = Circle(self.ix + ms, self.iy, ms, self.col)
        c.x += self.x - self.ix
        c.y += self.y - self.iy
        circles.append(c)

        c = Circle(self.ix + ms, self.iy + ms, ms, self.col)
        c.x += self.x - self.ix
        c.y += self.y - self.iy
        circles.append(c)

        circles.remove(self)
