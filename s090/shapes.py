COLORS = [color(0), color(0), color(0),
          color(255), color(255),
          color(200, 0, 100),
          ]

def circle(x, y, s):
    ellipse(x, y, s, s)
    
def square(x, y, s):
    rectMode(CENTER)
    rect(x, y, s, s)


def exes(x, y, s):
    with pushMatrix():
        translate(x, y)
        line(-s / 2, -s / 2, s / 2, s / 2)
        line(s / 2, -s / 2, -s / 2, s / 2)

def losang(x, y, s):
    with pushMatrix():
        translate(x, y)
        rotate(radians(45))
        rect(0, 0, s, s)
