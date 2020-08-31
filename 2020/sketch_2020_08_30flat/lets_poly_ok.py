from random import sample
from bezmerizing import Polyline, Path
#from flat import document, shape, rgb, rgba, command, path
from flat_processing import *



background(0, 200, 0)
ellipse(50, 50, 50, 50)

pts = [sample([10, 20, 30, 40, 50, 60, 70, 80], 2) for _ in range(5)]
poly_style = shape().fill(rgb(200, 0, 200)).stroke(black)
page.place(poly_style.polygon(Polyline(pts)))

d.pdf("test2.pdf")
page.svg('test2.svg')
#page.image(ppi=92, kind="rgb").png("sketch_2020_08_29.png")