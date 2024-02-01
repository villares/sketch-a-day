
def setup():
    size(900, 300)
    background(200, 100, 200)
    no_fill()
    for x in range(100, 801, 10):
        ra = 40
        rb = 80
        n = 2 + x // 50
        star(x, 150, ra, rb, n, radians(x))
    save('out.png')

def star(cx, cy, ra, rb, n, start_ang=0):  # "estrela"
    step = TWO_PI / n   # 360° / number of star (outer) points
    begin_shape()       # start poly shape
    for i in range(n):  # for each tip/point
        ang = start_ang + step * i # angle used to calculate vertex position
        ax = cx + cos(ang) * ra
        ay = cy + sin(ang) * ra
        vertex(ax, ay)  # add vertex calculated from radius ra
        bx = cx + cos(ang + step / 2.0) * rb  # note half steo added to angle
        by = cy + sin(ang + step / 2.0) * rb
        vertex(bx, by)  # add vertex calculated from raidius rb
    end_shape(CLOSE)    # end poly shape, and connect to first vertex
        
    
        
       