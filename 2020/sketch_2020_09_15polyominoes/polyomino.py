class Polyomino(object):

    def __init__(self, iterable):
        self.squares = tuple(sorted(iterable))

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, repr(self.squares))

    def __iter__(self):
        return iter(self.squares)

    def __len__(self):
        return len(self.squares)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        """Determine the one-sided key for this Poylomino"""
        p = self.translate()
        k = p.key()
        for _ in range(3):
            p = p.rotate().translate()
            k = min(k, p.key())
        return k

    def key(self):
        return hash(self.squares)

    def rotate(self):
        """Return a Polyomino rotated clockwise"""
        return Polyomino((-y, x) for x, y in self)

    def translate(self):
        """Return a Polyomino Translated to 0,0"""
        minX = min(s[0] for s in self)
        minY = min(s[1] for s in self)
        return Polyomino((x-minX, y-minY) for x, y in self)

    def raise_order(self):
        """Return a list of higher order Polyonominos evolved from self"""
        polyominoes = []
        for square in self:
            adjacents = (adjacent for adjacent in (
                (square[0] + 1, square[1]),
                (square[0] - 1, square[1]),
                (square[0], square[1] + 1),
                (square[0], square[1] - 1),
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
        
    def draw(self, w):
        """
        draw
        """
        p = self.translate()
        order = len(p)
        for x in range(order):
            for y in range(order):
                if (x, y) in p.squares:
                    rect(x * w, y *w, w, w) 
