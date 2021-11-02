# A quick proof of concept, PVector-like class for use with my py5 sketches
# based on a previous versions for pyp5js: https://gist.github.com/villares/5c476cbc44c1153fed159eae36fc016b

import math
from numbers import Number

TWO_PI = math.tau

class PVector:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z        

    def mag(self):
        return math.sqrt(self.magSq())

    def magSq(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def setMag(self, magnitude):
        return self.normalize().mult(magnitude)
 
    def normalize(self):
        magnitude = self.mag()
        if magnitude != 0:
            self.mult(1 / magnitude)
        return self

    def limit(self, max_mag):
        mSq = self.magSq()
        if mSq > max_mag * max_mag:
            self.div(math.sqrt(mSq)).mult(max_mag)
        return self

    def heading(self):
        return math.atan2(self.y, self.x)

    def rotate(self, angle):
        new_h = self.heading() + angle
        magnitude = self.mag()
        self.x = math.cos(new_h) * magnitude;
        self.y = math.sin(new_h) * magnitude;
        return self

    def get(self):
        return PVector(self.x, self.y, self.z)

    def copy(self):
        return PVector(self.x, self.y, self.z)
    
    def __iter__(self):
        for c in (self.x, self.y, self.z):
            yield c

    def __getitem__(self, k):
        return getattr(self, ('x', 'y', 'z')[k])

    def __setitem__(self, k, v):
        setattr(self, ('x', 'y', 'z')[k], v)

    def __copy__(self):
        return PVector(self.x, self.y, self.z)

    def __deepcopy__(self, memo):
        return PVector(self.x, self.y, self.z)

    def __repr__(self):  
        return f'PVector({self.x}, {self.y}, {self.z})'

    def set(self, *args):
        if len(args) == 3:
            self.x, self.y, self.z = args
        elif len(args) == 2:
            self.x, self.y = args
        elif len(args) == 1:
            self.x, self.y, self.z = args[0]

    def add(self, *args):
        if len(args) == 3:
            self.set(self.x + args[0], self.y + args[1], self.z + args[2])
        else:
            self.set(self + args[0])
        return self

    def sub(self, *args):
        if len(args) == 3:
            self.set(self.x - args[0], self.y - args[1], self.z - args[2])
        else:
            self.set(self - args[0])
        return self
    
    def mult(self, scalar):
        self.set(self * scalar)
        return self

    def div(self, scalar):
        self.set(self / scalar)
        return self

    def dist(self, other):
        return math.dist(self, other)

    def cross(self, other):     # should this one be "destructive" ?
        x = self.y * other[2] - other[1] * self.z
        y = self.z * other[0] - other[2] * self.x
        z = self.x * other[1] - other[0] * self.y
        return PVector(x, y, z)

    def dot(self, *args):
        if len(args) == 3:
            return self.x * args[0] + self.y * args[1] + self.z * args[2]
        else:
            other = args[0]
            return self.x * other[0] + self.y * other[1] + self.z * other[2]

    def __add__(a, b):
        return PVector(
            a[0] + b[0],
            a[1] + b[1],
            a[2] + b[2],
            )

    def __sub__(a, b):
        return PVector(
            a[0] - b[0],
            a[1] - b[1],
            a[2] - b[2],
            )

    def __isub__(a, b):
        a.sub(b)
        return a

    def __iadd__(a, b):
        a.add(b)
        return a

    def __mul__(a, scalar):
        if not isinstance(scalar, Number):
            raise TypeError(
                "The * operator can only be used to multiply a PVector by a number")
        return PVector(
            a[0] * scalar,
            a[1] * scalar,
            a[2] * scalar,
            )

    def __rmul__(a, b):
        if not isinstance(b, Number):
            raise TypeError(
                "The * operator can only be used to multiply a PVector by a number")
        return PVector.mult(a, float(b))

    def __imul__(a, b):
        if not isinstance(b, Number):
            raise TypeError(
                "The *= operator can only be used to multiply a PVector by a number")
        a.mult(float(b))
        return a

    def __truediv__(a, b):
        if not isinstance(b, Number):
            raise TypeError(
                "The * operator can only be used to multiply a PVector by a number")
        return PVector(a.x / b,
                       a.y / b,
                       a.z / b)

    def __itruediv__(a, b):
        if not isinstance(b, Number):
            raise TypeError(
                "The /= operator can only be used to multiply a PVector by a number")
        a.set(a.x / b,
              a.y / b,
              a.z / b)
        return a

    def __eq__(a, b):
        return a.x == b[0] and a.y == b[1] and a.z == b[2]

    def __lt__(a, b):
        return a.magSq() < b.magSq()

    def __le__(a, b):
        return a.magSq() <= b.magSq()

    def __gt__(a, b):
        return a.magSq() > b.magSq()

    def __ge__(a, b):
        return a.magSq() >= b.magSq()

    def lerp(self, other, t):
        self.set(
            self.x + (other.x - self.x) * t,
            self.y + (other.y - self.y) * t,
            self.z + (other.z - self.z) * t,
            )
        return self
 
    @classmethod
    def fromAngle(cls, angle, length=1):
        # https://github.com/processing/p5.js/blob/3f0b2f0fe575dc81c724474154f5b23a517b7233/src/math/p5.Vector.js
        return PVector(length * math.cos(angle), length * math.sin(angle), 0)

    @classmethod
    def fromAngles(theta, phi, length=1):
        # https://github.com/processing/p5.js/blob/3f0b2f0fe575dc81c724474154f5b23a517b7233/src/math/p5.Vector.js
        cosPhi = math.cos(phi)
        sinPhi = math.sin(phi)
        cosTheta = math.cos(theta)
        sinTheta = math.sin(theta)
        return PVector(length * sinTheta * sinPhi,
                       -length * cosTheta,
                       length * sinTheta * cosPhi)

    @classmethod
    def random2D(cls):  
        import random
        return PVector.fromAngle(random.random() * TWO_PI) 

    @classmethod
    def random3D(cls):
        import random
        angle = random.random() * TWO_PI
        vz = random.random() * 2 - 1
        mult = sqrt(1 - vz * vz)
        vx = mult * math.cos(angle)
        vy = mult * math.sin(angle)
        return PVector(vx, vy, vz)

    @classmethod
    def angleBetween(cls, a, b):
        return math.acos(a.dot(b) / math.sqrt(a.magSq() * b.magSq()))

    # Other harmless p5js methods

    def equals(self, v):
        return self == v

    def toString(self):
        return str(self)


def test():
    """
    Mostly from JDF py.processing tests
    """
    a = PVector()
    assert a.x == 0
    assert a.y == 0
    assert a.z == 0

    a = PVector(5, 7, 11)
    b = PVector(13, 17, 23)
    assert a - b == PVector(-8.0, -10.0, -12.0)
    assert b - a == PVector(8, 10, 12)
    c = PVector(18, 24, 34)
    assert b + a == c
    assert a + b == c
#     assert PVector.add(a, b) == c
#     assert PVector.add(a, b) == c
    a.add(b)
    assert a == c
    a.add(b)
    assert a == PVector(31.0, 41.0, 57.0)

    c = PVector(310.0, 410.0, 570.0)
    assert a * 10 == c
    assert a * 10 == c
#     assert PVector.mult(a, 10) == c

#     assert PVector.mult(a, 10) == c
    a.mult(10)
    assert a == c

    assert int(1000 * PVector.dist(a, b)) == 736116
    assert PVector.cross(a, b) == PVector(-260.0, 280.0, -60.0)
    assert a.cross(b) == PVector(-260.0, 280.0, -60.0)
    #assert PVector.dot(a, b) == 0

    d = a.get()
    d += b
    assert d == a + b
    d = a.get()
    d -= c
    assert d == a - c
    d = a.get()
    d *= 5.0
    assert d == a * 5.0
    d = a.get()

    d /= 5.0
    assert d == a / 5.0

    assert b * 5 == b * 5.0
    assert b / 5 == b / 5.0
    d = b.get()
    d *= 391
    assert d == b * 391.0
    d = b.get()
    d /= 10203
    assert d == b / 10203.0

    d = a.get()
    d += a + a
    assert d == a + a + a

    assert a * 57.0 == 57.0 * a

    assert (a / 5.0) == (1.0 / 5.0) * a

    m, n = b, c
    a += b * 5 - c / 2 + PVector(0, 1, 2)
    assert (m, n) == (b, c)

    import copy
    x = [a, b]
    y = copy.deepcopy(x)

    assert x == y
    x[0].sub(PVector(100, 100, 100))
    assert x != y

    a = PVector(1, 1)
    b = PVector(-2, -2)
    assert a < b
    assert a <= b
    assert b > a
    assert b >= a
    a = PVector(1, 2, 3)
    b = PVector(3, 2, 1)
    assert a != b
    assert a >= b
    assert b >= a
    assert a.magSq() == b.magSq()

    v1 = PVector(10, 20)
    v2 = PVector(60, 80)
    a = PVector.angleBetween(v1, v2)
    # Java implementation gives slightly different value:
    # assert a == 0.17985349893569946  # more or less
    assert int(a * 1e8) == 17985349  # more or less

    # Regression test for https://github.com/jdf/Processing.py-Bugs/issues/67
    assert isinstance(PVector(1, 2), PVector)

    # Regression test for https://github.com/jdf/Processing.py-Bugs/issues/101
    v = PVector(10, 20, 0)
    d = v.dot(60, 80, 0)
    assert d == 2200.0
    v2 = PVector(60, 80, 0)
    d = v.dot(v2)
    assert d == 2200.0

    # PVector.add w/multiple arguments
    v = PVector(40, 20, 0)
    v.add(25, 50, 0)
    assert (v.x, v.y, v.z) == (65, 70, 0)

    # PVector.sub w/multiple arguments
    v = PVector(40, 20, 0)
    v.sub(25, 50, 0)
    assert (v.x, v.y, v.z) == (15, -30, 0)

    # Regression test for https://github.com/jdf/Processing.py-Bugs/issues/102
    start = PVector(0.0, 0.0)
    end = PVector(100.0, 100.0)
    #middle = PVector.lerp(start, end, 0.5)
#     assert middle == PVector(50.0, 50.0)
    assert start == PVector(0, 0)
    start.lerp(end, .75)
    assert start == PVector(75, 75, 0)
    assert end == PVector(100.0, 100.0, 0)
#     end.lerp(200, 200, 0, .5)
#     assert end == PVector(150.0, 150.0)

    # test that instance op returns self
    a = PVector(3, 5, 7)
    b = a * 10
    assert a.mult(10) == b

    # test that a vector can do arithmetic with a tuple
    assert PVector(1, 2, 3) == (1, 2, 3)
    assert (PVector(1, 2, 3) + (3, 3, 3)) == (4, 5, 6)
    assert (PVector(5, 5, 5) - (1, 2, 3)) == (4, 3, 2)

    # Regression test for https://github.com/jdf/processing.py/issues/317
    r = PVector.random2D() * 10
    assert -10 <= r.x <= 10
    assert -10 <= r.y <= 10
    assert r.z == 0

#     PVector.random3D(r)
#     r += (1, 1, 1)
#     assert 0 <= r.x <= 2
#     assert 0 <= r.y <= 2
#     assert 0 <= r.z <= 2

    # Regression test for https://github.com/jdf/processing.py/issues/334
    r = PVector.fromAngle(0) * 10
    assert r.x == 10
    assert r.y == 0
    assert r.z == 0

    # Other p5js methods
    assert r.toString() == 'PVector(10.0, 0.0, 0)'
    r.setMag(100)
    assert r.mag() == 100
    r.normalize()
    assert r.mag() == 1
    r.limit(10)
    assert r.mag() == 1
    r.limit(0.1)
    assert r.mag() == 0.1

    assert r.heading() == 0
    r.rotate(math.pi)
    assert r.heading() == math.pi

    print('OK - ALL PASSED!', 100, 200)
   
    
if __name__ == '__main__':
     test()

