from itertools import product
from shape import Shape



def setup():
    size(1800, 900)
    noSmooth()
    background(0)
    print(count_shapes(order=4))
    saveFrame('a.png')
    
def count_shapes(order=3):
    global x, y
    grid = list(product(range(order), repeat=2))
    grid_size = order * order
    shapes = set([])    
    for n in range(1, 2 ** grid_size):
        squares = []
        template = '{{:0{}b}}'.format(grid_size)
        binary_sequence = template.format(n)
        for i, digit in enumerate(binary_sequence):
            if int(digit):
                squares.append(grid[i])
        # print(squares)
        shapes.add(Shape(squares))

    w = 2
    noStroke()
    x = y = w
    for p in sorted(shapes, key=len):
        push()
        translate(x, y)
        p.draw(w, c=True)
        x += (order + 1.5) * w
        pop()
        if x > width - order * w:
            x = w
            y += (order + 1) * w
            if y > height:
                print('ugh!')
    
    return len(shapes)
