# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s193"  # 20180710
OUTPUT = ".gif"
seed = 328 #int(random(1000))
println(seed)
randomSeed(seed)  # 634 326 630 17

from gif_export_wrapper import *
add_library('gifAnimation')

cycles = 5
hatches = []
global_rot = 0

def setup():
    blendMode(MULTIPLY)
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    size(500, 500, P2D)
    noStroke()
    hatches.append(Hatch(color(0, 255, 255)))
    hatches.append(Hatch(color(255, 0, 255)))
    hatches.append(Hatch(color(255, 255, 0)))
    hatches.append(Hatch(color(0)))

def draw():
    global global_rot
    background(200)

    for i, h in enumerate(hatches):
        f = frameCount / 200
        h.plot(do_rotation=(f % cycles == i))

    global_rot += 0.0314 / 4

    if frameCount % 2:
        gif_export(GifMaker, filename=SKETCH_NAME)

    if global_rot > PI * cycles:
        gif_export(GifMaker, finish=True)
        noLoop()


class Hatch:

    def __init__(self, c):
        self.n = int(random(30, 40))
        self.space = random(7.5, 15)
        l = self.n * self.space
        self.x = random(l / 2, width - l / 2)
        self.y = random(l / 2, height - l / 2)
        self.rot = random(TWO_PI)
        self.c = c
        #println((self.x, self.y, s))

    def plot(self, do_rotation):
        with pushMatrix():
            translate(self.x, self.y)
            rotate(self.rot)
            if do_rotation:
                # rotateX(global_rot)
                rotate(global_rot)
            s, l = self.space, self.n * self.space
            for i in range(1, self.n):
                for j in range(1, self.n):
                    fill(self.c)
                    ellipse(
                        s * i - l / 2.,
                        s * j - l / 2.,
                        s * .60, s * .60)


def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
