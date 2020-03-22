def setup():
    size(1220, 400)
    background(0)
    noStroke()
    colorMode(HSB)
    i = 50
    offset_x, offset_y = 20, 20 
    for x, y in grid(10, 10, 40, 40):
        fill(i * 2.5 % 256, 255, 200)
        s = 5 + abs(35 - (.7 * (i % 100)))
        ellipse(x + offset_x, y + offset_y, s, s)
        i += 1
    i = 1
    offset_x, offset_y = 430, 20 
    for x, y in shuffled_grid(10, 10, 40, 40):
        fill(i * 2.5 % 256, 255, 200)
        s = 5 + abs(35 - (.7 * i))
        ellipse(x + offset_x, y + offset_y, s, s)
        i += 1
    i = 1
    offset_x, offset_y = 840, 20 
    for x, y in shoebot_shuffled(10, 10, 40, 40):
        fill(i * 2.5 % 256, 255, 200)
        s = 5 + abs(35 - (.7 * i))
        ellipse(x + offset_x, y + offset_y, s, s)
        i += 1        
    save_image()

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
            
                                    
def save_image():
    from os import path
    sketch = sketchPath()
    filename = path.basename(sketch) + '.png'
    saveFrame(filename)
    print(filename + ' saved')
