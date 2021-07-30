
from itertools import product, permutations

colors = []

def setup():
    global color_tuples
    size(350, 290)
    colormode(HSB)
    colorrange(255)
    colors.append(color(0, 255, 255))
    colors.append(color(42, 255, 255))
    colors.append(color(84, 255, 255))
    colors.append(color(126, 255, 255))
    colors.append(color(170, 255, 255))
    colors.append(color(212, 255, 255))

    # color_tuples = list(product(colors, colors))
    color_tuples = list(permutations(colors, 2))
    print(len(color_tuples))

def draw():
    background(0)
    i = 0
    for y in range(5):
        for x in range(6):
            a, b = color_tuples[i]
            fill(a)
            rect(11 + x * 55, 11 +  y * 55, 50, 25)
            fill(b)
            rect(11 + x * 55, 11 + y * 55 + 25, 50, 25)
            i += 1
