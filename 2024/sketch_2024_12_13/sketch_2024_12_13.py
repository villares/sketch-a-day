from itertools import permutations, combinations_with_replacement
import py5
import numpy as np


def setup():
    global grids, quadrant_options, quadrant_colors
    py5.size(600, 600)
    Grid.setup(cell_size=24)
    grids = set()
    for config in combinations_with_replacement((0, 1, 2, 3), 16):
        grids.add(Grid(config))
        
    grids = {g for g in grids if good_grid(g)}
    
def good_grid(g):
    for row in g.array:
        for col in row:
            if len(set(col)) > 2:
                return False
            elif col[0] != col[3] and (col[0] != col[1] or col[2] != col[3]):          
                return False
            elif col[0] == col[3] and col[1] != col[2]:
                return False
    return True

def draw():
    py5.background(200)
    py5.translate(Grid.CS, Grid.CS) 
    x = y = 0
    for g in sorted(grids):
        with py5.push_matrix():
            py5.translate(x, y)
            g.draw()
        x += Grid.CS * (g.array.shape[1] + 1)
        if x > py5.width - Grid.CS * (g.array.shape[1] + 2):
            x = 0
            y += Grid.CS * (g.array.shape[0] + 1)
        
    
class Grid:
    
    @classmethod
    def setup(cls, cell_size):
        N = 4  # per "4 color map theorem"
        py5.color_mode(py5.HSB)
        cls.colors = [py5.color((12 + (255 / N) * i) , 200 , 200) for i in range(N)]
        #cls.colors = [py5.color(255 / (N - 1) * i) for i in range(N)]  
        cls.CS = cell_size  # Cell size
    
    def __init__(self, elements=None, shape=(2, 2, 4)):
        color_indices = range(len(self.colors))
        if elements is None:
            elements = py5.random_sample(color_indices, shape[0] * shape[1] * shape[2])
        self.array = np.array(elements).reshape(shape)

    def rotated90(self):
        i, j, k = self.array.shape
        return Grid(self.rot90_and_roll(self.array), shape=(j, i, k))

    def alternate(self):
        return Grid((self.array + 1) % len(self.colors), shape=self.array.shape)

    def roll(self):
        self.array = np.roll(self.array, 1, axis=2)

    @staticmethod
    def rot90_and_roll(a):
        """
        Rotates array and rolls axis 2 (subelements) making the visual
        representation look visualy rotated.
        """
        return np.roll(np.rot90(a, 1), -1, axis=2)

    def __eq__(self, other):
        return hash(self) == hash(other)
        
    def __lt__(self, other):
        return len(np.unique(self.array)) < len(np.unique(other.array))
        
    def recolor(self):
        values, inverse_indices = np.unique(self.array, return_inverse=True)
        self.array = inverse_indices
        
    def __hash__(self):
        """
        Makes rotations and different color alternatives equivalent.
        """
        a = self.array
        values, inverse_indices = np.unique(a, return_inverse=True)
        a = inverse_indices
        h = hash(tuple(inverse_indices.flatten()))
#         # broken attempt
#         for vs in permutations(values):
#             a = np.array(vs)[inverse_indices]
#             h = min(h, hash(tuple(a.flatten())))f
        for _ in range(3):
            a = self.rot90_and_roll(a)                
            h = min(h, hash(tuple(a.flatten())))

                    # not working
#                     fa = np.flip(a, axis=0)
#                     h = min(h, hash(fa.tobytes()))
#                     fb = np.flip(a, axis=1)
#                     h = min(h, hash(fb.tobytes()))
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
                    py5.stroke_weight(0.5)
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
            #g.recolor()

py5.run_sketch(block=False)