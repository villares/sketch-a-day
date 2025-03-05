import py5

from py5_tools import animated_gif

mode = 1
N = 5

def setup():
    global w, wa, wb
    py5.size(500, 500)
    py5.rect_mode(py5.CENTER)
    py5.no_stroke()
    w = py5.width / N

    animated_gif('out.gif', duration=0.2,
                 frame_numbers=range(1, 181, 3))
                
def draw():
    global mode
    ang = py5.radians(py5.frame_count)
    r = 1 / py5.sqrt(2)
    wa = w * r
    wb = w * (1 - r)
    rot = ang * 2
    if mode == 1:
        py5.background(255)
        for i in range(N + 1):
            x = i * w + wb / 2 - w / 2
            for j in range(N + 1):
                y = j * w + wb / 2 - w / 2
                py5.fill(0)
                rr(x,  y + (wa + wb) / 2, wa, wb, rot)
                rr(x + (wa + wb) / 2, y, wb, wa, rot)
        for i in range(N + 1):
            x = i * w + wb / 2 - w / 2
            for j in range(N + 1):
                y = j * w + wb / 2 - w / 2
                py5.fill(255)
                rr(x, y, wb, wb, rot + py5.QUARTER_PI)
                rr(x + (wa + wb) / 2,
                   y + (wa + wb) / 2, wb, wb,
                   rot + py5.QUARTER_PI)
        if py5.frame_count == 90:
            mode = 0
    else:
        py5.background(0)
        for i in range(N + 1):
            x = i * w + wb / 2 - w / 2
            for j in range(N + 1):
                y = j * w + wb / 2 - w / 2
                py5.fill(255)
                rr(x, y, wa, wa, rot)
                rr(x + (wa + wb) / 2,
                   y + (wa + wb) / 2, wb, wb, rot)
                rr(x + (wa + wb) / 2,
                   y + (wa + wb) / 2, wb, wb,
                   rot + py5.QUARTER_PI)

def rr(x, y, w, h, rot):
    with py5.push_matrix():
        py5.translate(x, y)
        py5.rotate(rot)
        py5.rect(0, 0, w, h)

                
                
                
        
        
    
    
py5.run_sketch(block=False)
    