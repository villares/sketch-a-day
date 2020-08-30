import random
from bezmerizing import Polyline
from flat import document, shape, rgb, rgba
from numpy.random import uniform, normal, choice
from scipy.stats import truncnorm

from scipy.stats import truncnorm


def t_normal(a, b, mu, sigma):
    tn = truncnorm((a-mu)/sigma, (b-mu)/sigma, loc=mu, scale=sigma)
    return tn.rvs(1)[0]

def flatten(t):
    from itertools import chain
    return list(chain(*t))

# def draw():
#     size = 200
#     black = rgba(0,0,0,255)
#     gray = rgba(200, 200, 200, 200)
#     d = document(size, size, 'mm')
#     page = d.addpage()
#     fig = shape().fill(gray).stroke(black)
#     pa = fig.polygon((10, 10, 100, 10, 10, 100))
#     pb = fig.polygon((20, 20, 110, 20, 20, 110))
#     page.place(pb)
#     d.pdf("test.pdf")
#     return page.svg("test.svg")
# draw()

def make_char():
    pts = []
    for i in range(int(t_normal(4, 12, 8, 2))):
        x = (choice([-.5, 0.5, 0]))
        y = (choice([-.5, 0.5, 0]))
        pts.append([x, y])
    return Polyline(pts)

chars = [make_char() for i in range(26)]    
d = document(150, 150, 'mm')
page = d.addpage()
line_fig = shape().stroke(rgba(128, 0, 128, 255)).nofill()
curve_fig = shape().stroke(rgba(0, 128, 128, 255)).nofill()
for row in range(10):
    line = choice(chars)
    for col in range(1, 10):
        # scale(normal(...)) adds a bit of size variation to the glyphs
        line += choice(chars).scale(normal(1, 0.25)).translate(col*1.5, 0)
    # translate the row to the right place on the screen and make it bigger
    line = line.translate(1, 1+row*1.5).scale(9)
    smooth = line.smooth_path()
    #page.place(line_fig.polyline(line)) # uncomment to see original polylines
    page.place(curve_fig.path(smooth))
page.svg('test2.svg')
page.image(ppi=92, kind="rgba").png("sketch_2020_08_29.png")