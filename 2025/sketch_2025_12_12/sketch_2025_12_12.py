import py5

def setup():
    py5.size(800, 800)
    ww = 80
    w = ww - 20
    n = py5.height // w
    for i in range(0, n):
        if i % 2 == 0:
            py5.stroke(128, 0, 0)
        else:
            py5.stroke(0, 0, 128)
        y = i * ww
        for x in range(-w, py5.width, 4):
            py5.line(x, y, x + w, y + w)
        py5.stroke(240, 240, 0)
        for x in range(-w, py5.width, 4):
            py5.line(x, y + w / 2 - 2, x + 4, y + w / 2 - 2 + 4)
    for j in range(0, n):
        if j % 2 == 0:
            py5.stroke(128, 0, 0)
        else:
            py5.stroke(0, 0, 128)
        x = j * ww
        for y in range(-w + 2, py5.height, 4):
            py5.line(x, y, x + w, y + w)
        py5.stroke(240, 240, 0)
        for y in range(-w + 2, py5.height, 4):
            py5.line(x + w / 2 - 2, y, x + w / 2 - 2 + 4, y + 4)            

    py5.save_frame('out.png')

py5.run_sketch()


