from grid_shapes import Shape

# SQUARE_SIZE = 40
# GRID_SIZE = 3
SQUARE_SIZE = 5
GRID_SIZE = 4

def setup():
    size(1528, 1004)
    # noStroke()
    background(0)
    #Shape.remove_flipped = True
    order = GRID_SIZE
    shapes = Shape.generate_shapes(order)
    print(len(shapes))
    x = y = w = SQUARE_SIZE
    sorted_shapes = sorted(shapes, key=len) # in Python 3 this is not a list!
    for p in sorted_shapes:
        push()
        translate(x, y)
        p.draw(w, c=True)
        x += (order + 1) * w
        pop()
        if x > width - order * w:
            x = w
            y += (order + 1) * w
            if y > height:
                print('ugh!')
            
    saveFrame('grid_shapes_order_{}.png'.format(order))
