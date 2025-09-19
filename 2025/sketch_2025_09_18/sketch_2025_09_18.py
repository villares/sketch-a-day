import py5
from py5_tools import animated_gif

import shapely

circles = [py5.Py5Vector2D()]
current = None
R = 4

def setup():
    global base
    py5.size(500, 500)
    py5.color_mode(py5.CMAP, py5.mpl_cmaps.TWILIGHT, 360)
    py5.no_stroke()
    base = shapely.Point(0, 0).buffer(R)
    animated_gif('out.gif', frame_numbers=range(1, 1500, 5), duration=0.1)        
    
def draw():
    global current, base
    py5.background('black')
    py5.translate(py5.width / 2, py5.height / 2)
    py5.no_stroke()
    for c in circles:
        py5.fill(py5.degrees(c.heading + py5.PI))
        py5.circle(c.x, c.y, R * 2)
    for _ in range(int(py5.width/R)):
        if current is None:
            current = py5.Py5Vector2D.random() * py5.width 
            #print(current)
        else:
            p = shapely.Point(current.x, current.y).buffer(R)
            #py5.shape(p)
            if not base.intersects(p):
                current.mag = current.mag - R
            else:
                base = base.union(p)
                circles.append(current)
                current = None
   
def key_pressed():
    py5.save('out.png')
        
py5.run_sketch(block=False)
