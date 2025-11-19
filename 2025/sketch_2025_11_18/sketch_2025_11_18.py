import py5

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)
    
#def draw():
    py5.background(0)
    py5.stroke_weight(10)
    py5.stroke(255, 128, 0 )
    for i in range(12):
        N = 3 + i * 2
        ang = py5.TWO_PI / N
        r  = 9 + 18 * i
        for j in range(N):
            x = 250 + r * py5.cos(ang * j) 
            y = 250 + r * py5.sin(ang * j)  
            py5.stroke(i * 20, 255, 255)
            py5.point(x, y)
            
    py5.save('out.png')

py5.run_sketch(block=False)  # remove block=False if on MacOS
