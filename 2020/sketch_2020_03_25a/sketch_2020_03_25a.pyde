# Based on https://www.openprocessing.org/sketch/862451
# by @takawo https://twitter.com/takawo

from random import choice

movers = []
mover_num = 350
pallete = ["#DA00DA", "#DE000C", "#3A00A8", "#A800CC",
           "#0A1D00", "#CD4600", "#C0AE00", "#838C00"]

def setup():
    global ns, offset
    size(600, 600)
    # pixelDensity(1)
    colorMode(HSB, 360, 100, 100, 100)
    # angleMode(DEGREES) # unavailabe in Python mode
    background(0, 0, 0)

    ns = random(1000)
    offset = width / 10

    for i in range(mover_num):
        x = random(offset, width - offset)
        y = random(offset, height - offset)
        movers.append(Mover(x, y))

    # image(img, 0, 0, width, height)


def draw():
    global ns
    fill(0, 4)
    noStroke()
    rect(0, 0, width, height)
    if frameCount % 1000 == 0:
        ns = random(10000)
        background(0)
    noiseSeed(int(ns))

    for m in movers:
        m.update()
        m.display()

def keyPressed():
    if key == 's':
        saveFrame("###.png")
    if key == ' ':
        background(0)

class Mover:

    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.prev_pos = self.pos.copy()
        self.vel = PVector(0, 0)
        self.noiseScale = 400
        self.len = 1
        self.strokeColor = choice(pallete)
        self.strokeBlurColor = self.strokeColor

    def update(self):
        n = int(noise(self.pos.x / self.noiseScale,
                      self.pos.y / self.noiseScale) * 7)
        angle = radians(n * 360 / 6)  # adjusted for Python mode
        self.vel = PVector(cos(angle) * self.len, sin(angle) * self.len)
        self.pos.add(self.vel)
        isBorder = False
        if not (offset < self.pos.x < width - offset and
                offset < self.pos.y < height - offset):
            isBorder = True

        if (random(100) < 1 or isBorder):
            self.pos.x = random(offset, width - offset)
            self.pos.y = random(offset, height - offset)
            self.prev_pos = self.pos.copy()
            self.strokeColor = choice(pallete)
            self.strokeBlurColor = self.strokeColor

    def display(self):
        # drawingContext.shadowColor = self.strokeBlurColor
        # drawingContext.shadowBlur = 5
        stroke(self.strokeColor)
        line(self.pos.x, self.pos.y, self.prev_pos.x, self.prev_pos.y)
        self.prev_pos = self.pos.copy()
