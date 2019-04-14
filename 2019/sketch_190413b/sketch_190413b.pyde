SKETCH_NAME = "sketch_190413b"

add_library('GifAnimation')
from gif_exporter import gif_export
from parts import Face
faces = []

def setup():
    size(500, 500, P3D)
    l4 = ((-4, -2),  (-3, -2), (-3, 1), (-2, 1), (-2, -1), (-1,-1),
          (-1, 1), (0, 1), (0, 2), (-1, 2), (-1, 3), (-2, 3), (-2, 2),
          (-4, 2))
    faces.append(Face(l4, 20))
    l3 = ((0, -2),  (3, -2), (3, -1), (2, 0), (3, 1), (3,2),
          (2, 3), (1, 3), (0, 2), (2, 2), (2, 1), (1, 0), (2, -1),
          (0, -1))
    faces.append(Face(l3, 20))
            
def draw():
    background(200, 210, 220)
    for f in faces:
        f.draw_3D(frameCount/-30.)
        # f.draw_2D()
        
    if frameCount/30. < TWO_PI:
        if frameCount % 2:
            gif_export(GifMaker, filename=SKETCH_NAME)
    else:
        exit()
    
        
