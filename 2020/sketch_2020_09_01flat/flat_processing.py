import random
from bezmerizing import Polyline, Path
from flat import document, shape, rgb, rgba, command, path
import numpy as np
from numpy.random import uniform, normal, choice
from scipy.stats import truncnorm

import builtins

def size(w, h):
    # global page, d
    builtins.width = w
    builtins.height = h
    builtins.d = document(width, height, 'mm')
    builtins.page =  d.addpage()

current_fill = rgb(255, 255, 255)
current_stroke = rgb(0, 0, 0)
black = rgb(0, 0, 0)
white = rgb(255, 255, 255)

def fill(r, *args):
    global current_fill
    current_fill = color_from_args(r, args)

def stroke(r, *args):
    global current_stroke
    current_stroke = color_from_args(r, args)

def color_from_args(r, args):
    if len(args) == 0:
        return rgb(r, r, r)
    elif len(args) == 1:
        return rgba(r, r, r, args[0])
    elif len(args) == 2:
        return rgb(r, args[0], args[1])
    else:    
        return rgba(r, args[0], args[1], args[2])

def background(r, *args):
    if len(args) == 0:
        g = b = r
    else:
        g, b = args
    fig = shape().fill(rgb(r, g, b)).nostroke()
    page.place(fig.rectangle(0, 0, width, height))

def ellipse(x, y, w, h):
    global page
    fig = shape().fill(current_fill).stroke(current_stroke)
    page.place(fig.ellipse(x, y, w / 2, h / 2))


def rect(x, y, w, h):
    global page
    fig = shape().fill(current_fill).stroke(current_stroke)
    page.place(fig.rectangle(x, y, w, h))


def triangle(xa, ya, xb, yb, xc, yc):
    global page
    fig = shape().fill(current_fill).stroke(current_stroke)
    page.place(fig.polygon(Polyline([(xa, ya), (xb, yb), (xc, yc)])))


# def size(w, h):
#     # doesn't work
#     global width, height, d
#     width, height = w, h
#     d = document(width, height, 'mm')


def flatten(t):
    from itertools import chain
    return list(chain(*t))
