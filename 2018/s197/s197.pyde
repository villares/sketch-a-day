# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s197b"  # 20180713
OUTPUT = ".gif"

from gif_export_wrapper import *
add_library('gifAnimation')

cycles = 5
hatches = []
global_rot = 0
noise_scale = 0.04

def setup():
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    size(500, 500, P2D)
    blendMode(MULTIPLY)
    noStroke()
    
    hatches.append(Hatch(color(0, 255, 255), # cian
                         radians(275)))
    hatches.append(Hatch(color(255, 0, 255), # magenta
                         radians(45)))
    hatches.append(Hatch(color(255, 255, 0), # yellow
                         radians(00)))

def draw():
    global global_rot
    background(200)

    for i, h in enumerate(hatches):
        h.plot()

    global_rot += 0.0314 /2

    if not frameCount % 5:
        gif_export(GifMaker, filename=SKETCH_NAME)

    if global_rot > TWO_PI:
        gif_export(GifMaker, finish=True)
        noLoop()


class Hatch():

    def __init__(self, c, rot):
        self.n = width / 6
        self.space = 10
        l = self.n * self.space
        self.x =  width  / 2
        self.y = height  / 2 
        self.rot = rot
        self.c = c
        #println((self.x, self.y, s))

    def plot(self):
        with pushMatrix():
            translate(self.x, self.y)
            rotate(self.rot)
            wx = cos(global_rot) * 2
            #wy = sin(global_rot) * 3
            s, l = self.space, self.n * self.space
            for i in range(1, self.n):
                for j in range(1, self.n):
                    fill(self.c)
                    d = 1.5 * s * noise(i * noise_scale - wx)
                    ellipse(
                        s / 2 + s * i - l / 2. ,
                        s / 2 + s * j - l / 2. ,
                        d, d)


def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
