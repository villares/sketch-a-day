import py5

a = 2
b = 1024
c = 256
m = 0

def setup():
    py5.size(800, 800)
    py5.color_mode(py5.HSB)
#     py5_tools.animated_gif(
#         'out2.gif',
#         frame_numbers=range(1, 361, 5),
#         duration=0.16
#    )

def draw():
    py5.background(255)  
    t = 0 # py5.frame_count
    for y in range(py5.height):
        for x in range(py5.width):
            v = abs((x + y - t) ^ (x - y + t))
            test = (m * 100 + pow(v, a)) % b;
            if test < c:
                py5.point(x, y)
    py5.update_pixels()      

def key_pressed():
    global a, m
    if py5.key == 'a':
        a +=  1
    elif py5.key == 'z':
        a -= 1
    elif py5.key == 's':
        m += 1
    elif py5.key == 'x':
        m -= 1
    elif py5.key == 'p':
        py5.save_frame('###.png')
  
    
py5.run_sketch(block=False)

