


def setup():
    size(500, 500)
    noFill()
    strokeWeight(10)
    stroke(100)
    x_mark(300, 200, 30)    
    x_mark(200, 200, 30)
    ellipse(250, 250, 200, 200)
    
def x_mark(x, y, s):
    with pushMatrix():
        translate(x, y)
        line(-s, -s, s, s)
        line(s, -s, -s, s)