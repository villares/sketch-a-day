from itertools import permutations
import py5
import numpy as np

N = 4 # number of colors

def setup():
    global grids
    py5.size(600, 600)
    py5.color_mode(py5.HSB)
    Grid.CS = 65
    Grid.colors = [py5.color((12 + (255 / N) * i) , 200 , 200) for i in range(4)]
    grids = [Grid(shape=(3, 3, 4))]
    for _ in range(3):
        grids.append(grids[-1].rotated90())
        #grids.append(grids[-1].alternate())

def draw():
    py5.background(200)
    py5.translate(Grid.CS, Grid.CS)
    x = y = 0
    for g in grids:
        with py5.push_matrix():
            py5.translate(x, y)
            g.draw()
        x += Grid.CS * (g.shape[1] + 1)
        if x > py5.width - Grid.CS * 2:
            x = 0
            y += Grid.CS * (g.shape[0] + 1)
        
    
class Grid:
    
    colors = [0]
    CS = 40  # Cell size
    
    def __init__(self, elements=None, shape=(4, 4, 4)):
        self.shape = shape
        color_indices = range(len(self.colors))
        if elements is None:
            elements = py5.random_sample(color_indices, shape[0] * shape[1] * shape[2])
        self.array = np.array(elements).reshape(shape)

    def rotated90(self):
        i, j, k = self.shape
        return Grid(self.rot90(self.array), shape=(j, i, k))

    def alternate(self):
        return Grid((self.array + 1) % len(self.colors), shape=self.shape)

    def roll(self):
        self.array = np.roll(self.array, 1, axis=2)

    @staticmethod
    def rot90(a):
        """
        This will have more stuff later...
        ... it will need to roll the sub-elements
        """
        return np.rot90(a)

    def draw(self):
        rows, cols, subelements = self.array.shape
        for r in range(rows):
            y = self.CS * r
            for c in range(cols):
                x = self.CS * c
                for s in range(subelements):
                    z = s * self.CS / 6
                    py5.fill(self.colors[self.array[r, c, s]])
                    py5.square(x + z, y + z, self.CS / 2)
                    
        
def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    elif py5.key == ' ':
        for g in grids:
            g.roll()

py5.run_sketch(block=False)