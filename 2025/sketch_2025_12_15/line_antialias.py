import py5

def setup():
    py5.size(200, 200)
    py5.stroke_weight(2)
    # a line that will drawn once only
    py5.line(10, 10, 190, 90)  

def draw():
    # you could clean the frame here with background(200)
    # this other line will be redrawn many times
    py5.line(10, 110, 190, 190) 

def key_pressed():
    py5.save('out.png')
    
py5.run_sketch()