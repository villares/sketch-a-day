import py5

def setup():
    py5.size(600, 600)
    py5.background(0, 200, 200)
    py5.stroke_weight(3)
    for i in range(80):
        if i % 2 == 0:
            py5.stroke(255)
        else:
            py5.stroke(0)
        y = 10 + i * 10
        pts = [(x, y + (5 + i) * py5.sin(x / (10 + i))) for x in range(py5.width)]
        py5.points(pts)
    
    py5.save(__file__[:-3] + '.png')
    
py5.run_sketch(block=False)