import py5
import numpy as np

N = 4

def setup():
    py5.size(500, 180)
    py5.color_mode(py5.HSB)
    py5.translate(20, 40)
    
    Grid.colors = [py5.color(12 + 255 / N * i, 255 , 255) for i in range(4)]
    grids = [Grid(order=5)]
    for _ in range(3):
        grids.append(grids[-1].rotated90())
        #grids.append(grids[-1].alternate())
        
    for g in grids:
        g.draw()
        py5.translate(Grid.CS * (g.order + 1), 0)

    py5.save('out.png')

class Grid:
    
    colors = [0]
    CS = 20  # Cell size
    
    def __init__(self, elements=None, order=3):
        self.order = order
        color_indices = range(len(self.colors))
        if elements is None:
            elements = py5.random_sample(color_indices, order * order)
        self.array = np.array(elements).reshape(order, order)

    def rotated90(self):
        return Grid(np.rot90(self.array), order=self.order)

    def alternate(self):
        return Grid((self.array + 1) % len(self.colors), order=self.order)


    def draw(self):
        rows, cols = self.array.shape
        for r in range(rows):
            y = self.CS * r
            for c in range(cols):
                x = self.CS * c
                py5.fill(self.colors[self.array[r, c]])
                py5.square(x, y, self.CS)
                
                

py5.run_sketch(block=False)
