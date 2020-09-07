from bezmerizing import Polyline, Path
from flat import document, shape, rgb, rgba, command, path

import builtins

def size(w, h):
    # global page, d
    builtins.width = w
    builtins.height = h
    builtins.d = document(w, h, 'pt')
    builtins.page =  d.addpage()

stroke_weight = 1
current_fill = rgb(255, 255, 255)
current_stroke = rgb(0, 0, 0)
black = rgb(0, 0, 0)
white = rgb(255, 255, 255)


def fill(r, *args):
    global current_fill
    current_fill = color_from_args(r, args)

def noFill():
    global current_fill
    current_fill = None

def noStroke():
    global current_stroke
    current_stroke = None

def stroke(r, *args):
    global current_stroke
    current_stroke = color_from_args(r, args)

def apply_attrs(fig):
    fig = fig.stroke(current_stroke) if current_stroke else fig.nostroke()
    fig = fig.fill(current_fill) if current_fill else fig.noFill()
    return fig
 
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
    fig = apply_attrs(shape())
    page.place(fig.ellipse(x, y, w / 2, h / 2))


def rect(x, y, w, h):
    global page
    fig = apply_attrs(shape())
    page.place(fig.rectangle(x, y, w, h))


def triangle(xa, ya, xb, yb, xc, yc):
    global page
    fig = apply_attrs(shape())
    page.place(fig.polygon(Polyline([(xa, ya), (xb, yb), (xc, yc)])))


# def flatten(t):
#     from itertools import chain
#     return list(chain(*t))
