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
    #for g in set(grids):  # to test duplicate removal
    for g in [grids[1], grids[0]] + grids[2:]:
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
        return Grid(self.rot90_and_roll(self.array), shape=(j, i, k))

    def alternate(self):
        return Grid((self.array + 1) % len(self.colors), shape=self.shape)

    def roll(self):
        self.array = np.roll(self.array, 1, axis=2)

    @staticmethod
    def rot90_and_roll(a):
        """
        This will have more stuff later...
        ... it will need to roll the sub-elements
        """
        return np.roll(np.rot90(a, 1), -1, axis=2)

    def __eq__(self, other):
        return hash(self) == hash(other)
        
    def __hash__(self):
        """
        Makes rotations and different color alternatives equivalent.
        """
        a = self.array
        h = hash(a.tobytes())
        values, inverse_indices = np.unique(a, return_inverse=True)
        for vs in permutations(values):
            a = np.array(vs)[inverse_indices].reshape(self.shape)
            h = min(h, hash(a.tobytes()))
            for _ in range(3):
                    a = self.rot90_and_roll(a)                
                    h = min(h, hash(a.tobytes()))
        return h

    def draw(self):
        rows, cols, subelements = self.array.shape
        CS = self.CS
        for r in range(rows):
            y = self.CS * r
            for c in range(cols):
                x = CS * c        
                tris = np.array((
                    ((0, 0), (1, 0), (0.5, 0.5)),
                    ((1, 0), (1, 1), (0.5, 0.5)),
                    ((1, 1), (0, 1), (0.5, 0.5)),
                    ((0, 1), (0, 0), (0.5, 0.5)),
                )) * CS + [x, y]
                for s in range(subelements):
                    py5.stroke_weight(0.1)
                    py5.fill(self.colors[self.array[r, c, s]])
                    py5.stroke(self.colors[self.array[r, c, s]])
                    #py5.triangle(*tris[s][0], *tris[s][1], *tris[s][2])                    
                    with py5.begin_closed_shape():
                        py5.vertices(tris[s])
        
def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    elif py5.key == ' ':
        for g in grids:
            g.roll()

py5.run_sketch(block=False)