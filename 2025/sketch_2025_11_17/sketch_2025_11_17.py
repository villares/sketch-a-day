import py5

def setup():
    py5.size(500, 500)
    py5.background(0)
    py5.stroke_weight(5)
    py5.stroke(255)
    for i in range(18):
        N = 36 - i
        r = 220 - i * 12
        ang = py5.TWO_PI / N
        for j in range(N):
            x = 250 + r * py5.cos(ang * j)
            y = 250 + r * py5.sin(ang * j) 
            py5.point(x, y)
    py5.save('out.png')

py5.run_sketch(block=False)

