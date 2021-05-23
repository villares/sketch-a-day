from shapes import Shape

def setup():
    size(600, 600)
    frameRate(10)
    Shape([(0, 0), (width, 0),
           (width, height), (0, height)])
    
    
def draw():
    clear()
    Shape.update_all(divide=True)

def mousePressed():
    Shape.shapes.clear()
    Shape([(0, 0), (width, 0),
           (width, height), (0, height)])
