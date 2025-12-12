import py5

def setup():
    py5.size(800, 800)
    w = 40
    n = py5.height // w
    for i in range(0, n, 2):
        if i % 4 == 0:
            py5.stroke(128, 0, 0)
        else:
            py5.stroke(0, 0, 128)
        y = i * w
        for x in range(-w, py5.width, 4):
            py5.line(x, y, x + w, y + w)
    for j in range(0, n, 2):
        if j % 4 == 0:
            py5.stroke(128, 0, 0)
        else:
            py5.stroke(0, 0, 128)
        x = j * w
        for y in range(-w + 2, py5.height, 4):
            py5.line(x, y, x + w, y + w)
    py5.save_frame('out.png')

py5.run_sketch()


