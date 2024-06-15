import py5

def setup():
    global shp
    py5.size(300, 300, py5.P2D)
    shp = py5.load_shape('a.svg')
    path = shp.get_children()[1].get_children()[0]
    py5.translate(50, 100)
    py5.shape(shp, 10, 10)
    path.set_stroke(py5.color(255))
    path.set_fill(py5.color(255, 0, 0, 10))
    py5.shape(path, 0, 0)
    py5.save('out.png')
    
py5.run_sketch(block=False)