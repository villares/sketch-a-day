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
