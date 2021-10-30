"""
Based on a talk by Hamish Campbell
https://pyvideo.org/kiwi-pycon-2013/shapes-an-exploration-in-problem-solving-w.html
"""
from collections import namedtuple

Square = namedtuple('Square', 'x y') 

class Shape(object):
    
    remove_flipped = False

    def __init__(self, iterable):
        self.squares = tuple([Square(*s) for s in sorted(iterable)])

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, repr(self.squares))

    def __iter__(self):
        return iter(self.squares)

    def __len__(self):
        return len(self.squares)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        """
        Determine the hash (an integer "key/id" number) 
        it is the smaller number (hash) of the square tuples
        of itself and its 3 rotated siblings
        """
        p = self.translate()
        h = hash(p.squares)
        for _ in range(3):
            p = p.rotate().translate()
            h = min(h, hash(p.squares))
        if Shape.remove_flipped:
            f = self.flip().translate()
            h = min(h, hash(f.squares))
            for _ in range(3):
                f = f.rotate().translate()
                h = min(h, hash(f.squares))
        return h

    def rotate(self):
        """Return a Shape rotated clockwise"""
        return Shape((-y, x) for x, y in self)

    def flip(self):
        """Return a Shape flipped"""
        return Shape((-x, y) for x, y in self)

    def translate(self):
        """Return a Shape Translated to 0,0"""
        minX = min(s.x for s in self)
        minY = min(s.y for s in self)
        return Shape((x - minX, y - minY) for x, y in self)

    def raise_order(self, size_limit=3):
        """Return a list of higher order Polyonominos evolved from self"""
        shapes = []
        for s in self:
            adjacents = (adjacent for adjacent in (
                (s.x + 1, s.y),
                (s.x - 1, s.y),
                (s.x, s.y + 1),
                (s.x, s.y - 1),
            ) if adjacent not in self)
            for adjacent in adjacents:
                new_shape = translate(Shape(list(self) + [adjacent]))
                if shape_under_limit(new_shape, size_limit):
                    shapes.append(new_shape)
        return shapes

    @staticmethod
    def shape_under_limit(shp, size_limit):
        return (max(s.x for s in shp) <= size_limit and 
                max(s.y for s in shp) <= size_limit)

    def render(self):
        """
        Returns a string map representation of the Shape
        """
        p = self.translate()
        order = len(p)
        return ''.join(
            ["\n %s" % (''.join(
                ["X" if (x, y) in p.squares else "-" for x in range(order)]
            )) for y in range(order)]
        )
        
    def draw(self, w, c=False):
        """
        draw
        """
        p = self.translate()
        #order = len(p)
        push()
        for i, (x, y) in enumerate(p.squares):
            if c:
                fill(128, x * 85, y * 85)
            rect(x * w, y *w, w, w) 
        pop()
