# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need py5 https://abav.lugaralgum.com/como-instalar-py5/index-EN.html
from itertools import product

import py5

from shape import all_from_points

grid = product((-1, 0, 1), (-1, 0, 1))  # 3X3
pts = list(grid)
space, border = 50, 50

def setup():
    global shapes
    py5.size(500, 350)
    W = int(py5.width - border * 2) // space
    H = int(py5.height - border * 2) // space

    shapes = []
    tm = 0
    for i in [6]: # 3 to 7, as no non-intersecting shapes exist with 8 or 9 pts.
        m = py5.millis()
        shapes.extend(all_from_points(pts, i)) #, remove_flipped=True))
        dt = py5.millis() - m
        print(i, dt)
        tm += dt
    print(f'total: {tm} millisegundos')
    
    def shape_area(s):
        return s.area
    shapes.sort(key=shape_area)
    
    print(f'shapes: {len(shapes)} Cols: {W} Rows: {H} Visible grid: {W*H}')

    py5.stroke_join(py5.ROUND)
    py5.background(0, 0, 200)
    py5.no_stroke()
    i = 0
    b = py5.create_graphics(int(space), int(space))
    for y, x in product(range(H), range(W)):
        if i < len(shapes):
            shp = shapes[i]
            with py5.push_matrix():
                py5.translate(border + (space + 1) * x + space / 2,
                              border + (space + 1) * y + space / 2)
                py5.fill(len(shp) * 35, 255, 150)
                #shp.draw(space * 0.3)
                b.begin_draw()
                b.background(0)
                b.no_stroke()
                b.fill(255)
                b.scale(space * 0.5)
                #b.translate(space * 0.05, space * 0.05)
                with b.begin_closed_shape():
                    b.vertices(shp.points)
                b.end_draw()
                py5.image_mode(py5.CENTER)
                py5.image(b, 0, 0)
            i += 1
        
def key_pressed():
    py5.save_frame('###.png')

py5.run_sketch(block=True)