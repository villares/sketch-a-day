import py5



def setup():
    py5.size(400, 400)
    N = 7
    w = py5.width / N
    h = py5.height / 3
    py5.color_mode(py5.HSB)
    y = 0
    colors = [py5.color(10 + 255 / N * i, 255 , 255) for i in range(N)]
    for i, c in enumerate(colors):
        x = i * w
        py5.fill(c)
        py5.rect(x, y, w, h)
    y += h
    w = py5.width / N 
    colors = [py5.color(255 / N * i, 255 , 255) for i in range(N)]
    for i, c in enumerate(colors):
        x = i * w
        py5.fill(c)
        py5.rect(x, y, w, h)
    y += h
    N = 6
    w = py5.width / N 
    colors = [py5.color(255 / N * i, 255 , 255) for i in range(N)]
    for i, c in enumerate(colors):
        x = i * w
        py5.fill(c)
        py5.rect(x, y, w, h)

    py5.save('out.png')

py5.run_sketch()