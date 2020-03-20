def setup():
    size(550, 550)
    background(0)
    noStroke()
    colorMode(HSB)
    i = 0
    for x, y in shuffled_grid(10, 10, 50, 50):
        fill(i * 4, 255, 200)
        ellipse(x + 50, y + 50, 25, 25)
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
            
def save_image():
    from os import path
    sketch = sketchPath()
    filename = path.basename(sketch) + '.png'
    saveFrame(filename)
    print(filename + ' saved')
