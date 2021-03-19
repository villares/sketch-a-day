from __future__ import division

def setup():
    global cols, rows, pixs, dump
    size(900, 600);
    background(0)
    img = loadImage('img.jpg')
    # image(img, 0, 0)
    cols, rows = 300, 200
    sx = img.width / float(cols)
    sy = img.height / float(rows)
    pixs = {}
    for i in range(cols):
        x = int(sx / 2 + i * sx)
        for j in range(rows):
            y = int(sy / 2 + j * sy)
            c = img.get(x, y)
            pixs[(i, j)] = c
            
    dump = []        
    for i in range(rows):
        fila = []
        for j in range(cols):
            c = pixs.get((j, i), 0)
            fila.append((c, j, i))
        for j, (c, oj, oi) in enumerate((sorted(fila, key=lambda t:saturation(t[0])))):  
            # c=color, oi=original i, oj=original j 
            dump.append((c, j, i, oj, oi))
            
def draw():
    background(0)
    s = 3 
    t = map(mouseX, 0, width, 0, 1)
    t = (1 + cos(frameCount / 10.0)) / 2.1
    for i in range(rows):
        fila = []
        for j in range(cols):
            c = pixs.get((j, i), 0)
            fila.append((c, j))
        new_fila = []
        sorted_fila = (sorted(fila, key=lambda t:hue(t[0])))
        for j, (c, oj) in enumerate(sorted_fila):  
            nj = lerp(j, oj, t)
            new_fila.append((c, nj))
        sorted_new_fila = sorted(new_fila, key=lambda t:t[1])
        for j, (c, nj) in enumerate(sorted_new_fila):    
            noStroke()
            fill(c)
            rect(j * s, i * s, s, s)
