# Avec unique_choices par Julien Palard
# https://mamot.fr/@mdk/110158306945003068
import py5
from random import choice
from itertools import count, groupby
import operator

options = [10, 30, 50, 70]

def unique(iterable):
    return map(next, map(operator.itemgetter(1), groupby(iterable, None)))

def unique_choices(options):
    return unique(choice(options) for _ in count())

def setup():
    py5.size(700, 700)
    py5.color_mode(py5.HSB)
    x, v_choices = 0, unique_choices(options)
    while x < py5.width:
        c = next(v_choices)
        py5.fill(c * 3, 200, 200, 128)
        py5.rect(x, 0, c, py5.height)
        x += c
    y, h_choices = 0, unique_choices(options)
    while y < py5.height:
        c = next(h_choices)
        py5.fill(c * 3, 200, 200, 128)
        py5.rect(0, y, py5.width, c)
        y += c

py5.run_sketch()
