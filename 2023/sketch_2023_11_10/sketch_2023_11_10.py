import py5_tools

def setup():
    size(800, 400)
    py5_tools.animated_gif('out.gif', 63, 0.1, 0.1)
    
def draw():
    background(200)
    for x in range(0, width, 5):
        ya = 200 + 50 * sin(x / 50 + frame_count / 10)
        yb = 200 + 25 * sin(x / 25 + frame_count / 10)
        line(x, ya, x, yb)
        
        
