# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need py5 https://abav.lugaralgum.com/como-instalar-py5/index-EN.html

"""
3 74
4 276
5 1370
6 5819
7 17720
total: 25259 millisegundos
shapes: 125 Cols: 25 Rows: 5 Visible grid: 125
"""

from itertools import product

import py5

from shape import all_from_points

grid = product((0, 1, 2), (0, 1, 2))  # 3X3
pts = list(grid)
space, border = 50, 25
name = "shapes2"

def setup():
    global shapes
    py5.size(1300, 300)
    W = int(py5.width - border * 2) // space
    H = int(py5.height - border * 2) // space

    shapes = []
    tm = 0
    for i in [3, 4, 5, 6, 7]: # 3 to 7, as no non-intersecting shapes exist with 8 or 9 pts.
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

    f = py5.create_graphics(py5.width * 10,  # for big PDF export
                            py5.height * 10, py5.PDF, name + '.pdf')
    # begin PDF export
    py5.begin_record(f) # begin PDF export
    py5.color_mode(py5.HSB)
    f.scale(10)
    py5.stroke_join(py5.ROUND)
    py5.background(240)
    py5.no_stroke()
    i = 0
    for y, x in product(range(H), range(W)):
        if i < len(shapes):
            shp = shapes[i]
            with py5.push_matrix():
                py5.translate(border + space * x,
                              border + space * y)
                py5.fill(len(shp) * 35, 255, 150)
                shp.draw(space * 0.4)
            i += 1
    # end PDF export
    py5.end_record()  
    py5.save_frame(name + '.png')

py5.run_sketch(block=True)