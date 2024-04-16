# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need py5 https://abav.lugaralgum.com/como-instalar-py5/index-EN.html

from itertools import product

import py5

from shape import Shape

grid = product((0, 1, 2), (0, 1, 2))  # 3X3
pts = list(grid)
space, border = 150, 75
name = "shapes"

def setup():
    global shapes
    py5.size(1050, 1050)
    
    W = int(py5.width - border * 2) // space
    H = int(py5.height - border * 2) // space

    shapes = []
    m = py5.millis()
    for i in [4]: # 3 to 7, as no non-intersecting shapes exist with 8 or 9 pts.
        shapes.extend(Shape.all_from_points(pts, i))
    print(py5.millis() - m)
    
    def shape_area(s):
        return s.area
    shapes.sort(key=shape_area)
    
    print(f'shapes: {len(shapes)} Cols: {W} Rows: {H} Visible grid: {W*H}')

    f = py5.create_graphics(py5.width * 10,  # for big PDF export
                            py5.height * 10, py5.PDF, name + '.pdf')
    # begin PDF export
    py5.begin_record(f)
    f.scale(10)
    py5.translate(20, 170)
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
                py5.fill(0, 0, 100)
                shp.draw(space * 0.4)
                py5.fill(255, 0, 0)
            i += 1
    # end PDF export 
    py5.end_record()  
    py5.save_frame(name + '.png')


py5.run_sketch(block=False)