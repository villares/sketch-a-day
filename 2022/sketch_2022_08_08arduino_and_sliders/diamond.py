import py5

def diamond(x, y, c, _):
    with py5.push_matrix():
        py5.translate(x, y)
        py5.rotate(py5.radians(45))
        py5.rect(0, 0, c, c)
