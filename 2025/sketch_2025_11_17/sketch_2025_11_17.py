import py5   
def setup():
    py5.size(500, 500)
    py5.background(0)
    py5.stroke_weight(5)
    py5.stroke(255)
    for i in range(18):
        N = 36 - i
        ang = py5.TWO_PI / N
        for j in range(N):
            x = 250 + py5.cos(ang * j) * (220 - i * 12)
            y = 250 + py5.sin(ang * j) * (220 - i * 12) 
            py5.point(x, y)
    py5.save('out.png')

py5.run_sketch(block=False)  # remove block=False if on MacOS

