import py5
import shapely

def setup():
    py5.size(200, 200)
    
    py5.shape_mode(py5.CENTER) 

    shp = py5.create_shape(py5.GROUP)
    square = py5.create_shape(py5.RECT, 0, 0, 80, 80)
    shp.add_child(square)
    py5.shape(shp, 100, 100)  # seemengly drawn from corner
    
    other = py5.create_shape()
    other.begin_shape()
    other.no_fill()
    other.vertex(0, 0)
    other.vertex(80, 0)
    other.vertex(80, 80)
    other.vertex(0, 80)
    other.end_shape(py5.CLOSE)    
    py5.shape(other, 100, 100)  # drawn as espected
    
py5.run_sketch(block=False)
