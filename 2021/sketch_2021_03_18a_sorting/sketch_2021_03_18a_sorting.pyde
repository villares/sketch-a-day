from __future__ import division

def setup():
    size(900, 600);
    background(0)
    img = loadImage('img.jpg')
    cols, rows = 450, 300
    sx = img.width / float(cols)
    sy = img.height / float(rows)
    pixs = {}
    for i in range(cols):
        x = int(sx / 2 + i * sx)
        for j in range(rows):
            y = int(sy / 2 + j * sy)
            c = img.get(x, y)
            pixs[(i, j)] = c
        
    s = 2 
    for i in range(cols):
        coluna = []
        for j in range(rows):
            c = pixs.get((i, j), 0)
            coluna.append(c)
        for j, c in enumerate(sorted(coluna, key=brightness)):
            noStroke()
            fill(c)
            ellipse(i * s, j * s, s, s)
