def setup():
    size(1220, 400)
    frameRate(10)

def draw():
    from random import seed
    seed(1)
    background(0)
    for function in (grid, shuffled_grid, shoebot_shuffled):
        g = make_a_grid(function, frameCount % 100)
        plot_a_grid(g)
        translate(410, 0)
                        
def plot_a_grid(a_grid):    
    noStroke()
    for x, y, s, c in a_grid:
        fill(c)
        ellipse(x, y, s, s)

def shuffled_grid(cols, rows, colSize=1, rowSize=1):
    from random import shuffle
    sg = list(grid(cols, rows, colSize, rowSize))
    shuffle(sg)
    return sg

def grid(cols, rows, colSize=1, rowSize=1):
    """
    Returns an iterator that contains coordinate tuples.
    As seen in Shoebot & Nodebox (minus 'shuffled mode')
    A common way to use is:
    #    for x, y in grid(10, 10, 12, 12):
    #        rect(x, y, 10, 10)
    """
    rowRange = range(int(rows))
    colRange = range(int(cols))
    for y in rowRange:
        for x in colRange:
            yield (x * colSize, y * rowSize)

def shoebot_shuffled(cols, rows, colSize=1, rowSize=1):
    from random import shuffle
    rowRange = list(range(int(rows)))
    colRange = list(range(int(cols)))
    shuffle(rowRange)
    shuffle(colRange)
    for y in rowRange:
        for x in colRange:
            yield (x * colSize, y * rowSize)
            
def make_a_grid(grid_function, offset=50):  
    colorMode(HSB)  
    i = offset
    a_grid = []
    offset_x, offset_y = 20, 20 
    for x, y in grid_function(10, 10, 40, 40):
        c = color(i * 2.5 % 256, 255, 200)
        s = 5 + abs(35 - (.7 * (i % 100)))
        a_grid.append((x + offset_x, y + offset_y, s, c))
        i += 1
    return a_grid
                                    
def save_image():
    from os import path
    sketch = sketchPath()
    filename = path.basename(sketch) + '.png'
    saveFrame(filename)
    print(filename + ' saved')
