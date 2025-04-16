import numpy as np

def setup():
    size(500, 500)
    
    fill(200, 0, 0)
    y = 25
    for _ in range(5):
        x = 25
        for _ in range(5):
            circle(x, y, 40)
            x = x + 50
        y = y + 50
    
    # np.arange would allow non-int steps.
    fill(0, 200, 0)  
    for x in np.arange(25, 250, 50):
        for y in np.arange(25, 250, 50):
            circle(250 + x, y, 40)

    # I like to know the row and column numbers.
    fill(0, 0, 200)
    for i in range(5):
        for j in range(5):
            circle(25 + i * 50, 250 + 25 + j * 50, 40)

    text_align(CENTER, CENTER)
    w = 50
    for i in range(5):
        x = 250 + w / 2 + i * w
        for j in range(5):
            y = 250 + w / 2 + j * w
            fill(0)
            circle(x, y, w - 10)
            fill(255)
            text(f'{i}, {j}', x, y)
      
      
    save('out.png')
        
