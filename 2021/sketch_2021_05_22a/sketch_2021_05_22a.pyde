from shapes import Shape

def setup():
    size(700, 700)
    Shape([(0, 0), (width, 0),
           (width, height), (0, height)])
    
    
def draw():
    Shape.update_all()
    

    
