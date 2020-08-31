import random
from bezmerizing import Polyline, Path
from flat import document, shape, rgb, rgba, command, path
import numpy as np
from numpy.random import uniform, normal, choice
from scipy.stats import truncnorm

width, height = 100, 100
d = document(width, height, 'mm')
page = d.addpage()
black = rgb(0, 0, 0)

current_fill = rgb(255, 255, 255)
current_stroke = rgb(0, 0, 0)

def background(r, *args):
    if len(args) == 0:
        g = b = r
    else:
        g, b = args
    fig = shape().fill(rgb(r, g, b)).nostroke()
    page.place(fig.rectangle(0, 0, width, height))

def ellipse(x, y, w, h):
    fig = shape().fill(current_fill).stroke(current_stroke)
    page.place(fig.ellipse(x, y, w, h))


def rect(x, y, w, h):
    fig = shape().fill(current_fill).stroke(current_stroke)
    page.place(fig.rectangle(x, y, w, h))

def size(w, h):
    # doesn't work
    global width, height, d
    width, height = w, h
    d = document(width, height, 'mm')


def flatten(t):
    from itertools import chain
    return list(chain(*t))
