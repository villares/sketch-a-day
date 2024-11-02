import py5

def setup():
    py5.size(200, 200)
    py5.stroke_weight(10)
    py5.stroke_cap(py5.PROJECT)
    py5.point(75, 100)
    py5.stroke_cap(py5.ROUND) # the default
    py5.point(125, 100)

py5.run_sketch(block=False)