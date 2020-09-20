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
    
    hash_memo = {}
    hash_count = 0 # for debug

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
        """
        Determine the hash (an integer "key/id" number) 
        it is the smaller number (hash) of the square tuples
        of itself and its rotated siblings
        """
        hash_memo = Polycube.hash_memo
        s = self.squares
        equivalents = []
        if s in hash_memo:
            return hash_memo[s]
        h = hash(s)
        for _ in range(3):
            s = Polycube.rotate(s, 0)
            equivalents.append(s)
            # h = min(h, hash(s))
            for _ in range(3):
                s = Polycube.rotate(s, 1)
                equivalents.append(s)
                # h = min(h, hash(s))
                for _ in range(4):
                    s = Polycube.rotate(s, 2)
                    equivalents.append(s)
                    # h = min(h, hash(s))
        # Polycube.hash_count += 1   
        hs = sorted(map(hash, equivalents))
        hash_memo.update(dict.fromkeys(equivalents, hs[0]))
        hash_memo[self.squares] = hs[0]
        return hs[0]

    def raise_order(self, d=2):
        """Return a list of higher order Polyonominos evolved from self"""
        Polycubes = []
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
                Polycubes.append(
                    Polycube(list(self) + [adjacent])
                )
        return Polycubes

    def draw(self, w):
        order = len(self)
        for x, y, z in self.squares:
            push()
            translate(x * w, y * w, z * w)
            box(w)
            pop()

    @staticmethod
    @memoize
    def translate(iterable):
        squares = sorted(iterable)
        """Return a Polycube Translated to 0,0"""
        minX = min(s[0] for s in squares)
        minY = min(s[1] for s in squares)
        minZ = min(s[2] for s in squares)
        return tuple(sorted((x - minX, y - minY, z - minZ)
                     for x, y, z in squares))
        
    @staticmethod
    @memoize
    def rotate(squares, axis=0):
        """Return Polycube squares rotated clockwise"""
        if axis == 0:
            return Polycube.translate(tuple((-y, x, z) for x, y, z in squares))
        elif axis == 1:
            return Polycube.translate(tuple((x, -z, y) for x, y, z in squares))
        else:
           return Polycube.translate(tuple((-z, y, x) for x, y, z in squares))


        
