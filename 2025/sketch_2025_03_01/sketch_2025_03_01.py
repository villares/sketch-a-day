import py5

from py5_tools import animated_gif

mode = 1
N = 5
R = 0.333

def setup():
    global w, wa, wb
    py5.size(500, 500)
    py5.rect_mode(py5.CENTER)
    w = py5.width / N
    wa = w * R
    wb = w * (1 - R)
    animated_gif('out.gif', duration=0.1,
                 frame_numbers=range(1, 361, 6))
                
def draw():
    if mode == 1:
        py5.background(255)
        py5.fill(0)
        for i in range(N + 1):
            for j in range(N + 1):
                x = i * w + wa / 2 - w / 2
                y = j * w + wa / 2 - w / 2
                rr(x, y, wa, wa)
                rr(x + (wa + wb) / 2,
                   y + (wa + wb) / 2, wb, wb)

def rr(x, y, w, h):
    with py5.push_matrix():
        py5.translate(x, y)
        py5.rotate(py5.radians(py5.frame_count))
        py5.rect(0, 0, w, h)

                
                
                
        
        
    
    
py5.run_sketch(block=False)
    