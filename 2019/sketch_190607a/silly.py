class Glyph:
    w = 5  # width
    m = 16  # module
    sw = 8 # stroke weight
    f = None # fill

    def __init__(self, id, points=None, paths=None):
        self.id = id  # unicode char
        self.points = points if points else []
        self.paths = paths if paths else []

    def __repr__(self):
        return 'Glyph("{}", {}, {})'.format(
            self.id, self.points, repr(self.paths))

    def plot(self):
        strokeWeight(self.sw)
        if self.f == None:
            noFill()
        else:
            fill(self.f)
            
        for ps in self.paths:
            for p in ps:
                if p == ".":
                    beginShape()
                if p == "-":
                    beginContour()
                if p == "=":
                    endContour()
                if p == ":":
                    endShape()
                if p == ";":
                    endShape(CLOSE)
                if p in "012345679ABCDEF":
                    pt = self.points[unhex(p)]
                    if pt[2]:
                        vertex(pt[0] * self.m, pt[1] * -self.m)
