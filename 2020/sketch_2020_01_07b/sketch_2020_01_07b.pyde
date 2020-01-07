
def setup():
    size(500, 500)
    global grid
    grid = make_grid(width, height, 50)
    
def make_grid(w, h, s, margin=None):
    off = s / 2
    margin = off if margin is None else margin
    cols, rows = (w - margin * 2) // s, (h - margin * 2) // s
    points = dict()
    for i in range(cols):
        x = off + i * s + margin
        for j in range(rows):
            y = off + j * s + margin
            points[(i, j)] = (x, y)
    return points
    
def draw():
    background(240, 250, 250)
    for x, y  in grid.values():
        circle(x, y, 10)
