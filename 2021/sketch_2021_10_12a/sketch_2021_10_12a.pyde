from collections import deque
steps = deque((2, 3, 4, 5, 6, 8, 9, 10, 12, 15))

def setup():
    size(500, 500)
    frameRate(3)
    
def draw():
    background(0)
    translate(250, 250)
    noFill()
    colorMode(HSB)
    s = 5
    f = steps.popleft()
    steps.append(f)
    i_step = enumerate(reversed(steps))
    for i , step in i_step:
        t = 2.5 #+ 1 * sin(radians(frameCount / 3.0))
        r = 10 + 10 * i * t
        stroke(20 * step % 256, 255, 255)
        for a in range(0, 360, step):
            x = r * cos(radians(a + i * 2))
            y = r * sin(radians(a + i * 2)) 
            circle(x, y, step)
    # if frameCount < 11:
    #     saveFrame('##.png')
