import py5

from py5_tools import animated_gif

mode = 1
N = 5

def setup():
    global w, wa, wb
    py5.size(500, 500)
    py5.rect_mode(py5.CENTER)
    w = py5.width / N

    animated_gif('out.gif', duration=0.15,
                 frame_numbers=range(1, 361, 6))
                
def draw():
    ang = py5.radians(py5.frame_count)
    r = (2 + py5.sin(ang)) / 3
    wa = w * r
    wb = w * (1 - r)
    rot = ang / 2
    if mode == 1:
        py5.background(255)
        py5.blend_mode(py5.SUBTRACT)
        for i in range(N + 1):
            for j in range(N + 1):
                x = i * w + wa / 2 - w / 2
                y = j * w + wa / 2 - w / 2
                rr(x, y, wa, wa, rot)
                rr(x + (wa + wb) / 2,
                   y + (wa + wb) / 2, wb, wb, rot)

def rr(x, y, w, h, rot):
    with py5.push_matrix():
        py5.translate(x, y)
        for i in range(3):
            py5.rotate(rot)
            py5.fill(('cyan', 'magenta', 'yellow')[i])
            py5.rect(0, 0, w, h)

                
                
                
        
        
    
    
py5.run_sketch(block=False)
    