add_library('GifAnimation')
from gif_animation_helper import gif_export

# based onhttps://twitter.com/Hau_kun/status/1248949717930631168?s=20
t = 0
m = 255
s = sin
def setup():
    size(510, 510)
    noStroke()
def draw():
    global t
    clear()
    t += .01
    r = 0
    while r < TAU:
        x = y = m
        d = 0
        while d < 1:
            a = r + bezierTangent(s(r), s(t), s(t - r), 0, d)
            x += cos(a) * 2
            y += s(a) * 2
            fill(y % m, d * m, x % m)
            circle(x, y, d * 9)
            d += .01
        r += PI / 8
    if t < TWO_PI:
        gif_export(GifMaker, "animation")
    else:
        gif_export(GifMaker, "animation", finish=True)


def settings():
    """ print markdown to add at the sketc-a-day page"""
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".png"
    println(
        """
![{0}]({2}/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT, year())
    )
