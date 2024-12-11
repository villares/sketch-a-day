from itertools import permutations
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
        
    #for g in set(grids):  # testing for duplicate removal
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

    def __eq__(self, other):
        return hash(self) == hash(other)
        
    def __hash__(self):
        """
        Makes rotations and different colors equivalent.
        """
        a = self.array
        h = hash(a.tobytes())
        values, inverse_indices = np.unique(a, return_inverse=True)
        for vs in permutations(values):
            a = np.array(vs)[inverse_indices].reshape(self.order, self.order)
            h = min(h, hash(a.tobytes()))
            for _ in range(3):
                    a = np.rot90(a, 1)                    
                    h = min(h, hash(a.tobytes()))
        return h

    def draw(self):
        rows, cols = self.array.shape
        for r in range(rows):
            y = self.CS * r
            for c in range(cols):
                x = self.CS * c
                py5.fill(self.colors[self.array[r, c]])
                py5.square(x, y, self.CS)
                
                
py5.run_sketch(block=False)
