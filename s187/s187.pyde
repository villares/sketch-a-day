# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s187" #20180704
OUTPUT = ".png"

add_library('gifAnimation')

num_hatches = 30
hatches = []
global_rot = 0

def setup():
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    size(600, 600)
    #smooth(4)
    for _ in range(num_hatches):
        hatches.append(Hatch())

def draw():
    global global_rot
    background(100)
    stroke(0)
    for i, h in enumerate(hatches):
        stroke(map(i, 0, len(hatches)-1, 0, 255))
        h.plot()
        
    global_rot += 0.01
    if global_rot > TWO_PI: noLoop()

class Hatch:

    def __init__(self):
        self.n = int(random(10, 40))
        self.space = random(5, 15)
        self.half = self.n * self.space / 2.
        self.x = random(width)
        self.y = random(height)
        self.rot = random(TWO_PI)

    def plot(self):
        with pushMatrix():
            translate(self.x, self.y)
            rotate(self.rot + global_rot)
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
