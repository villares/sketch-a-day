import py5

from py5_tools import animated_gif

mode = 1
N = 5

def setup():
    global w, wa, wb
    py5.size(500, 500)
    py5.rect_mode(py5.CENTER)
    w = py5.width / N

    animated_gif('out.gif', duration=0.2,
                 frame_numbers=range(1, 181, 6))
                
def draw():
    global mode
    ang = py5.radians(py5.frame_count)
    r = 1 / py5.sqrt(2)
    wa = w * r
    wb = w * (1 - r)
    rot = ang / 2
    if mode == 1:
#         py5.background(0)
#         py5.blend_mode(py5.ADD)
#         for i in range(N + 1):
#             for j in range(N + 1):
#                 x = i * w + wa / 2 - w / 2
#                 y = j * w + wa / 2 - w / 2
#                 rr(x + (wa + wb) / 2, y, wa, wb, rot)
# #                 rr(x + w / 2, y + wa / 2 + w / 2, wb, wa, rot)
# #                 rr(x + wa / 2, y + w / 2, wb, wa, rot)
# #                 rr(x + wa / 2 + w / 2, y + w / 2, wa, wb, rot)
#         if py5.frame_count == 180:
#             mode = 0
#     else:
        py5.background(0)
        py5.blend_mode(py5.ADD)
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
            py5.rotate(rot * 2)
            py5.fill(('cyan', 'magenta', 'yellow')[i])
            py5.rect(0, 0, w, h)

                
                
                
        
        
    
    
py5.run_sketch(block=False)
    