def exes(x, y, c, _):
    with pushMatrix():
        translate(x, y)
        line(-c / 2, -c / 2, c / 2, c / 2)
        line(c / 2, -c / 2, -c / 2, c / 2)

def losang(x, y, c, _):
    with pushMatrix():
        translate(x, y)
        rotate(radians(45))
        rect(0, 0, c, c)

SHAPES = [ellipse,
          rect,
          exes,
          losang]

COLORS = [color(0),
          color(255),
          color(255, 0, 0),
          color(0, 0, 255)]
