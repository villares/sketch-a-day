"""
s180113 3D Graphs!
(c)2018 Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

add_library('peasycam')

mm = 0
Z_INC = 20

def setup():
    size(600, 600, P3D)
    cam = PeasyCam(this, 500)
    generate()
    #ellipseMode(CORNER)
    colorMode(HSB)

def draw():
    global mx, my, mm, time
    mm *= 0.95
    # if (mm < 0.04) mm *= 0.2
    mx = mouseX - width / 2
    my = mouseY - height / 2
    time = millis() * 0.001
    background(190)

    #translate(width / 2, height / 2)

    for c in circles:
        c.update()
    for c in circles:
        c.showShadow()
    for c in circles:
        c.showEdges()
    for c in circles:
        c.show()

    # if (frameCount < 200): saveFrame("###.tga") # para salvar frames


def keyPressed():
    generate()

# def mouseClicked():
#     sub()

def mouseMoved():
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
    circles.append(Circle(-50, -50 , 600, color(random(256), 200, 200)))


class Circle:

    def __init__(self, x, y, s, c):
        self.edges = set()
        self.x = x
        self.y = y
        self.ix = x
        self.iy = y
        self.s = s
        self.b = 12
        self.ncol = color(random(256), 200, 200)
        self.col = c
        self.z = 0

    def mouseMovement(self):
        cx = self.x 
        cy = self.y 
        maxDist = 50
        dis = dist(cx, cy, mx, my)
        ang = atan2(cy - my, cx - mx)
        if (dis < maxDist):
            dd = map(dis, 0, maxDist, 1, 0)
            dd = pow(dd, 0.9) * 20 * mm
            self.x += cos(ang) * dd
            self.y += sin(ang) * dd

    def update(self):

        self.x = lerp(self.x, self.ix, 0.09)
        self.y = lerp(self.y, self.iy, 0.09)
        self.col = lerpColor(self.col, self.ncol, 0.05)

        self.mouseMovement()

    def showShadow(self):
        noStroke()
        fill(0, 20)
        ellipse(self.x , self.y, self.s, self.s)

    def showEdges(self):
        strokeWeight(3)
        stroke(self.col)
        for e in self.edges:
            line(self.x, self.y, self.z, e.x, e.y, e.z)

    def show(self):
        stroke(self.col)
        fill(self.col)
        pushMatrix()
        translate(0,0,self.z)
        ellipse(self.x, self.y, self.b, self.b)
        popMatrix()

    def isOn(self, mx, my):
        return dist(self.x, self.y, mx, my) < self.s/2

    def sub(self):
        ms = self.s * 0.5
        mms = ms/2
        c0 = Circle(self.ix-mms, self.iy+mms, ms, self.col)
        c0.edges = self.edges
        c0.z = self.z+Z_INC
        #replace egges from any child
        for c in circles:
            if self in c.edges:
                c.edges.remove(self)
                c.edges.add(c0)            
        circles.append(c0)

        c1 = Circle(self.ix-mms, self.iy-mms, ms, self.col)
        c1.x += self.x - self.ix
        c1.y += self.y - self.iy
        c1.z = self.z+Z_INC
        c1.edges.add(c0)
        circles.append(c1)

        c2 = Circle(self.ix+mms , self.iy-mms, ms, self.col)
        c2.x += self.x - self.ix
        c2.y += self.y - self.iy
        c2.z = self.z+Z_INC
        c2.edges.add(c0)
        circles.append(c2)

        c3 = Circle(self.ix+mms , self.iy+mms , ms, self.col)
        c3.x += self.x - self.ix
        c3.y += self.y - self.iy
        c3.z = self.z+Z_INC
        c3.edges.add(c0)
        circles.append(c3)

        circles.remove(self)