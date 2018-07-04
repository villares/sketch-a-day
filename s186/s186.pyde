# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s186" #20180703
OUTPUT = ".png"

add_library('gifAnimation')

num_hatches = 12
hatches = []

def setup():
    print_text_for_readme(SKETCH_NAME, OUTPUT)
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


def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
