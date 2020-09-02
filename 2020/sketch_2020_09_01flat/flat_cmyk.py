from flat import document, shape, cmyk, overprint

c = shape().stroke(overprint(cmyk(100, 0, 0, 0))).width(40.0)
y = shape().stroke(overprint(cmyk(0, 0, 100, 0))).width(40.0)
d = document(200, 200, 'mm')
p = d.addpage()
p.place(c.line(10, 10, 100, 100))
p.place(y.line(100, 10, 10, 100))
d.pdf('shape.pdf')