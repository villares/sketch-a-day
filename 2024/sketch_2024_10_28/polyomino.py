"""
Based on a talk by Hamish Campbell
https://pyvideo.org/kiwi-pycon-2013/polyominoes-an-exploration-in-problem-solving-w.html
"""

from collections import namedtuple

import py5

Square = namedtuple('Square', 'x y') 



class Polyomino(object):
    
    REMOVE_MIRRORED = False
    NBS = [ ( 1, 0),
            (-1, 0),
            ( 0, 1),
            ( 0,-1),]

    def __init__(self, iterable):
        self.squares = tuple([Square(*s) for s in sorted(iterable)])

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.squares)})'

    def __iter__(self):
        return iter(self.squares)

    def __len__(self):
        return len(self.squares)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __lt__(self, other):
        return self.squares < other.squares

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
        if self.REMOVE_MIRRORED:
            f = self.flip().translate()
            h = min(h, hash(f.squares))
            for _ in range(3):
                f = f.rotate().translate()
                h = min(h, hash(f.squares))
        return h

    def rotate(self):
        """Return a Polyomino rotated clockwise"""
        return Polyomino((-y, x) for x, y in self)

    def flip(self):
        """Return a Shape flipped"""
        return Polyomino((-x, y) for x, y in self)


    def translate(self):
        """Return a Polyomino Translated to 0,0"""
        minX = min(s.x for s in self)
        minY = min(s.y for s in self)
        return Polyomino((x - minX, y - minY) for x, y in self)

    def raise_order(self):
        """Return a list of higher order Polyonominos evolved from self"""
        
        polyominoes = []
        for s in self:
            adjacents = ((s.x + ox, s.y + oy) for ox, oy in self.NBS if (s.x + ox, s.y + oy) not in self)
            polyominoes.extend(Polyomino(list(self) + [adjacent])
                               for adjacent in adjacents)
        return polyominoes

        
    def draw(self, w, color_func=False):
        """
        draw
        """
        p = self.translate()
        #order = len(p)
        with py5.push_matrix():
            for i, (x, y) in enumerate(p.squares):
                if color_func:
                   color_func(x, y, i)
                py5.rect(x * w, y *w, w, w) 
            

    @classmethod
    def get_polyominoes(cls, target, up_to=False, include_unit=False):
        order = 1
        polyominoes = set([cls(((0,0),))])
        all_p = polyominoes if include_unit else set([]) 
        while order < target:
            order += 1
            next_order_polyominoes = set()
            for polyomino in polyominoes:
                next_order_polyominoes.update(polyomino.raise_order())
            polyominoes = next_order_polyominoes
            all_p.update(next_order_polyominoes)
        if up_to:
            return all_p
        return polyominoes

