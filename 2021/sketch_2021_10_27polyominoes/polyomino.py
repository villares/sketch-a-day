from collections import namedtuple

Square = namedtuple('Square', 'x y') 

class Polyomino(object):

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
        return h

    def rotate(self):
        """Return a Polyomino rotated clockwise"""
        return Polyomino((-y, x) for x, y in self)

    def translate(self):
        """Return a Polyomino Translated to 0,0"""
        minX = min(s.x for s in self)
        minY = min(s.y for s in self)
        return Polyomino((x - minX, y - minY) for x, y in self)

    def raise_order(self):
        """Return a list of higher order Polyonominos evolved from self"""
        polyominoes = []
        for s in self:
            adjacents = (adjacent for adjacent in (
                (s.x + 1, s.y),
                (s.x - 1, s.y),
                (s.x, s.y + 1),
                (s.x, s.y - 1),
            ) if adjacent not in self)
            for adjacent in adjacents:
                polyominoes.append(
                    Polyomino(list(self) + [adjacent])
                )
        return polyominoes

    def render(self):
        """
        Returns a string map representation of the Polyomino
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
        colorMode(HSB)
        for i, (x, y) in enumerate(p.squares):
            if c:
                fill(256 - i * 38, 255, 200)
            rect(x * w, y *w, w, w) 
        pop()
