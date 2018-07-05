# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s186" #20180703
OUTPUT = ".png"

num_hatches = 12
hatches = []

def setup():
    size(500, 500)
    smooth()
    for _ in range(num_hatches):
        hatches.append(Hatch())

def draw():
    background(100)
    stroke(255)
    for h in hatches:
        h.plot()

class Hatch:

    def __init__(self):
        self.n = int(random(10, 40))
        self.space = random(5, 15)
        self.half = self.n * self.space / 2.
        self.x = random(self.half, width - self.half)
        self.y = random(self.half, height - self.half)
        self.rot = random(TWO_PI)

    def plot(self):
        with pushMatrix():
            translate(self.x, self.y)
            rotate(self.rot + mouseX / 50.)
            s, l = self.space, self.half
            #ellipse(0, 0, 5,5)
            for i in range(self.n):
                line(s * i - l, -l, s * i - l, l)
