import py5
from polyskel import skeletonize

poly = list(reversed([
    (0, 0), (450, 0), (500, 500), (0, 500)
    ]))

holes = [list(reversed([
    (100, 100), (100, 400), (300, 400), (400, 100)
    ]))]

skeleton = skeletonize(poly, holes)

def setup():
    py5.size(600, 600)
    py5.stroke_weight(2)
    py5.fill(255, 100)
    py5.translate(50, 50)
    py5.stroke(0, 0, 200)
    with py5.begin_closed_shape():
        py5.vertices(poly)
        for hole in holes:
            with py5.begin_contour():
                py5.vertices(hole)
    py5.stroke(255, 0, 0)
    for a in skeleton:
        for sink in a.sinks:
            py5.line(a.source.x, a.source.y, sink.x, sink.y)

py5.run_sketch(block=False)