from villares.helpers import sketch_name

# Two approaches for grids - a simple study

def setup():
    size(840, 840);
    background(240)
    noFill()
    smooth(); strokeWeight(2)
    
    s = 20 # must be int
    for x in range(s // 2, width, s):
        for y in range(s // 2, height, s):
            stroke(0, 150, 0)
            circle(x, y, s)

    s = 21.0 # can be float
    cols, rows = int(width / s), int(height / s)
    for ix in range(cols):
        x = s / 2.0 + ix * s
        for iy in range(rows):
            y = s / 2.0 + iy * s
            stroke(0, 0, 150)
            circle(x, y, s)
            
    saveFrame(sketch_name() + '.png')
