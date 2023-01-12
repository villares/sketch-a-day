from random import choice

from villares.line_geometry import point_inside_poly, rect_points

rects = []
dims = (40, 80, 120, 160, 200)

def setup():
    size(700, 700)
    #no_loop() # for debug
   
def draw():
    background(200)
    
    if len(rects) < 10:
        ox, oy = random(100, width - 100), random(100, height - 100)
        w = choice(dims)
        h = choice(dims)
        a = radians(45 + random(-1, 1) * 2)
        nr = rect_points(ox, oy, w, h, mode=CENTER, angle=a)
        good = True
        for r in rects:
            if good == False:
                break
            for p in r:
                if point_inside_poly(p, nr):
                    #circle(*p, 5)
                    good = False
                    break
            for p in nr:
                if point_inside_poly(p, r):
                    #circle(*p, 5)
                    good = False
                    break
        if good == False:
            return
        rects.append(nr)
        
    #no_fill()
    fill(0)
    for r in rects:
        with begin_closed_shape():
            vertices(r)
            
def key_pressed():
    rects[:] = []
    