from collections import namedtuple

def memoize(f):
    memo = {}
    def memoized_func(*args):
        if args not in memo:
            r = f(*args)
            memo[args] = r
            return r
        return memo[args]
    return memoized_func

class Polycube(object):
    
    hash_count = 0 

    def __init__(self, iterable):
        self.squares = Polycube.translate(tuple(iterable))

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, repr(self.squares))

    def __iter__(self):
        return iter(self.squares)

    def __len__(self):
        return len(self.squares)

    def __eq__(self, other):
        return (self.squares == self.squares
                or hash(self) == hash(other))

    def __hash__(self):
        # Polycube.hash_count += 1
        """
        Determine the hash (an integer "key/id" number) 
        it is the smaller number (hash) of the square tuples
        of itself and its rotated siblings
        """
        p = self
        h = hash(p.squares)
        for _ in range(3):
            p = p.rotate()
            h = min(h, hash(p.squares))
            for _ in range(3):
                p = p.rotateX()
                h = min(h, hash(p.squares))
                for _ in range(4):
                    p = p.rotateY()   
                    h = min(h, hash(p.squares))

        return h

    def rotate(self):
        """Return a Polycube rotated clockwise"""
        return Polycube((-y, x, z) for x, y, z in self)

    def rotateX(self):
        """Return a Polycube rotated on X"""
        return Polycube((x, -z, y) for x, y, z in self)

    def rotateY(self):
        """Return a Polycube rotated on Y """
        return Polycube((-z, y, x) for x, y, z in self)

    def raise_order(self, d=2):
        """Return a list of higher order Polyonominos evolved from self"""
        polycubes = []
        for s in self:
            adjacents = [adjacent for adjacent in (
                (s[0] + 1, s[1], s[2]),
                (s[0] - 1, s[1], s[2]),
                (s[0], s[1] + 1, s[2]),
                (s[0], s[1] - 1, s[2]),
            ) if adjacent not in self]
            if d == 3:
                adjacents += [adjacent for adjacent in (
                    (s[0], s[1], s[2] + 1),
                    (s[0], s[1], s[2] - 1),
                ) if adjacent not in self]

            for adjacent in adjacents:
                polycubes.append(
                    Polycube(list(self) + [adjacent])
                )
        return polycubes

    def draw(self, w):
        order = len(self)
        for x, y, z in self.squares:
            push()
            translate(x * w, y * w, z * w)
            box(w)
            pop()

    @staticmethod
    @memoize
    def translate(squares):
        """Return a Polycube Translated to 0,0"""
        minX = min(s[0] for s in squares)
        minY = min(s[1] for s in squares)
        minZ = min(s[2] for s in squares)
        return tuple(sorted((x - minX, y - minY, z - minZ)
                     for x, y, z in squares))
        
