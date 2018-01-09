
def PlatonicFactory(type_=0, size_=None):
    classes = {0: Tetrahedron,
               1: Hexahedron,
               2: Octahedron,
               3: Dodecahedron,
               4: Icosahedron,
               }
    default_sizes = {0: 36, 1: 28, 2: 44, 3: 36, 4: 36}
    if size_:
        solid_size = size_
    else:
        solid_size = default_sizes[type_]

    return classes[type_](solid_size)

class Tetrahedron():

    def __init__(self, radius):
        self.vert = [0] * 4
        self.radius = radius
        a = radius * 0.6666
        self.vert[0] = PVector(a, a, a)
        self.vert[1] = PVector(-a, -a, a)
        self.vert[2] = PVector(-a, a, -a)
        self.vert[3] = PVector(a, -a, -a)

    # draws tetrahedron
    def create(self):
        vert = self.vert
        beginShape(TRIANGLE_STRIP)
        vertex(vert[0].x, vert[0].y, vert[0].z)
        vertex(vert[1].x, vert[1].y, vert[1].z)
        vertex(vert[2].x, vert[2].y, vert[2].z)
        vertex(vert[3].x, vert[3].y, vert[3].z)
        vertex(vert[0].x, vert[0].y, vert[0].z)
        vertex(vert[1].x, vert[1].y, vert[1].z)
        vertex(vert[3].x, vert[3].y, vert[3].z)
        vertex(vert[2].x, vert[2].y, vert[2].z)
        vertex(vert[1].x, vert[1].y, vert[1].z)
        endShape(CLOSE)


class Hexahedron():

    def __init__(self, radius):
        self.radius = radius
        a = radius / 1.1414
        faces = [0] * 6
        vert = [0] * 8
        vert[0] = PVector(a, a, a)
        vert[1] = PVector(a, a, -a)
        vert[2] = PVector(a, -a, -a)
        vert[3] = PVector(a, -a, a)
        vert[4] = PVector(-a, -a, a)
        vert[5] = PVector(-a, a, a)
        vert[6] = PVector(-a, a, -a)
        vert[7] = PVector(-a, -a, -a)

        faces[0] = (0, 1, 2, 3)
        faces[1] = (4, 5, 6, 7)
        faces[2] = (0, 3, 4, 5)
        faces[3] = (1, 2, 7, 6)
        faces[4] = (2, 3, 4, 7)
        faces[5] = (0, 5, 6, 1)

        self.vert, self.faces = vert, faces

    # draws hexahedron
    def create(self):
        for i in range(6):
            beginShape()
            for j in range(4):
                vertex(self.vert[self.faces[i][j]].x,
                       self.vert[self.faces[i][j]].y,
                       self.vert[self.faces[i][j]].z)
            endShape()


class Octahedron():

    def __init__(self, radius):
        self.radius = radius
        a = radius
        vert = [0] * 6
        vert[0] = PVector(a, 0, 0)
        vert[1] = PVector(0, a, 0)
        vert[2] = PVector(0, 0, a)
        vert[3] = PVector(-a, 0, 0)
        vert[4] = PVector(0, -a, 0)
        vert[5] = PVector(0, 0, -a)
        self.vert = vert

    # draws octahedron
    def create(self):
        vert = self.vert
        beginShape(TRIANGLE_FAN)
        vertex(vert[4].x, vert[4].y, vert[4].z)
        vertex(vert[0].x, vert[0].y, vert[0].z)
        vertex(vert[2].x, vert[2].y, vert[2].z)
        vertex(vert[3].x, vert[3].y, vert[3].z)
        vertex(vert[5].x, vert[5].y, vert[5].z)
        vertex(vert[0].x, vert[0].y, vert[0].z)
        endShape()

        beginShape(TRIANGLE_FAN)
        vertex(vert[1].x, vert[1].y, vert[1].z)
        vertex(vert[0].x, vert[0].y, vert[0].z)
        vertex(vert[2].x, vert[2].y, vert[2].z)
        vertex(vert[3].x, vert[3].y, vert[3].z)
        vertex(vert[5].x, vert[5].y, vert[5].z)
        vertex(vert[0].x, vert[0].y, vert[0].z)
        endShape()

class Icosahedron():

    def __init__(self, radius):
        topPent = [0] * 5  # PVector[5]
        bottomPent = [0] * 5  # PVector[5]
        angle = 0
        c = dist(cos(0) * radius,
                 sin(0) * radius,
                 cos(radians(72)) * radius,
                 sin(radians(72)) * radius)
        b = radius
        a = sqrt(((c * c) - (b * b)))
        triHt = sqrt((c * c) - ((c / 2) * (c / 2)))
        for i in range(5):
            topPent[i] = PVector(cos(angle) * radius,
                                 sin(angle) * radius,
                                 triHt / 2.0)
            angle += radians(72)
        topPoint = PVector(0, 0, triHt / 2.0 + a)
        angle = 72.0 / 2.0
        for i in range(5):
            bottomPent[i] = PVector(cos(angle) * radius,
                                    sin(angle) * radius,
                                    -triHt / 2.0)
            angle += radians(72)
        bottomPoint = PVector(0, 0, -(triHt / 2.0 + a))
        self.topPent, self.bottomPent = topPent, bottomPent
        self.topPoind, self.bottomPoint = topPoint, bottomPoint

        # draws icosahedron
    def create(self):
        topPent, bottomPent = self.topPent, self.bottomPent
        topPoint, bottomPoint = self.topPoind, self.bottomPoint
        for i in range(5):
            # icosahedron top
            beginShape()
            if (i < 5 - 1):
                vertex(topPent[i].x, topPent[i].y, topPent[i].z)
                vertex(topPoint.x, topPoint.y, topPoint.z)
                vertex(
                    topPent[i + 1].x, topPent[i + 1].y, topPent[i + 1].z)
            else:
                vertex(topPent[i].x, topPent[i].y, topPent[i].z)
                vertex(topPoint.x, topPoint.y, topPoint.z)
                vertex(topPent[0].x, topPent[0].y, topPent[0].z)

            endShape(CLOSE)

            # icosahedron bottom
            beginShape()
            if (i < len(bottomPent) - 1):
                vertex(bottomPent[i].x, bottomPent[i].y, bottomPent[i].z)
                vertex(bottomPoint.x, bottomPoint.y, bottomPoint.z)
                vertex(
                    bottomPent[i + 1].x, bottomPent[i + 1].y, bottomPent[i + 1].z)
            else:
                vertex(bottomPent[i].x, bottomPent[i].y, bottomPent[i].z)
                vertex(bottomPoint.x, bottomPoint.y, bottomPoint.z)
                vertex(bottomPent[0].x, bottomPent[0].y, bottomPent[0].z)

            endShape(CLOSE)

        # icosahedron body
        for i in range(5):
            if i < 3:
                beginShape()
                vertex(topPent[i].x, topPent[i].y, topPent[i].z)
                vertex(
                    bottomPent[i + 1].x, bottomPent[i + 1].y, bottomPent[i + 1].z)
                vertex(
                    bottomPent[i + 2].x, bottomPent[i + 2].y, bottomPent[i + 2].z)
                endShape(CLOSE)

                beginShape()
                vertex(
                    bottomPent[i + 2].x, bottomPent[i + 2].y, bottomPent[i + 2].z)
                vertex(topPent[i].x, topPent[i].y, topPent[i].z)
                vertex(
                    topPent[i + 1].x, topPent[i + 1].y, topPent[i + 1].z)
                endShape(CLOSE)
            elif i == 3:
                beginShape()
                vertex(topPent[i].x, topPent[i].y, topPent[i].z)
                vertex(
                    bottomPent[i + 1].x, bottomPent[i + 1].y, bottomPent[i + 1].z)
                vertex(bottomPent[0].x, bottomPent[0].y, bottomPent[0].z)
                endShape(CLOSE)

                beginShape()
                vertex(bottomPent[0].x, bottomPent[0].y, bottomPent[0].z)
                vertex(topPent[i].x, topPent[i].y, topPent[i].z)
                vertex(
                    topPent[i + 1].x, topPent[i + 1].y, topPent[i + 1].z)
                endShape(CLOSE)
            elif i == 4:
                beginShape()
                vertex(topPent[i].x, topPent[i].y, topPent[i].z)
                vertex(bottomPent[0].x, bottomPent[0].y, bottomPent[0].z)
                vertex(bottomPent[1].x, bottomPent[1].y, bottomPent[1].z)
                endShape(CLOSE)

                beginShape()
                vertex(bottomPent[1].x, bottomPent[1].y, bottomPent[1].z)
                vertex(topPent[i].x, topPent[i].y, topPent[i].z)
                vertex(topPent[0].x, topPent[0].y, topPent[0].z)
                endShape(CLOSE)

class Dodecahedron():

    def __init__(self, radius):
        self.radius = radius
        a = radius / 1.618033989
        b = radius
        c = 0.618033989 * a
        faces = [0] * 12
        vert = [0] * 20
        vert[0] = PVector(a, a, a)
        vert[1] = PVector(a, a, -a)
        vert[2] = PVector(a, -a, a)
        vert[3] = PVector(a, -a, -a)
        vert[4] = PVector(-a, a, a)
        vert[5] = PVector(-a, a, -a)
        vert[6] = PVector(-a, -a, a)
        vert[7] = PVector(-a, -a, -a)
        vert[8] = PVector(0, c, b)
        vert[9] = PVector(0, c, -b)
        vert[10] = PVector(0, -c, b)
        vert[11] = PVector(0, -c, -b)
        vert[12] = PVector(c, b, 0)
        vert[13] = PVector(c, -b, 0)
        vert[14] = PVector(-c, b, 0)
        vert[15] = PVector(-c, -b, 0)
        vert[16] = PVector(b, 0, c)
        vert[17] = PVector(b, 0, -c)
        vert[18] = PVector(-b, 0, c)
        vert[19] = PVector(-b, 0, -c)

        faces[0] = (0, 16, 2, 10, 8)
        faces[1] = (0, 8, 4, 14, 12)
        faces[2] = (16, 17, 1, 12, 0)
        faces[3] = (1, 9, 11, 3, 17)
        faces[4] = (1, 12, 14, 5, 9)
        faces[5] = (2, 13, 15, 6, 10)
        faces[6] = (13, 3, 17, 16, 2)
        faces[7] = (3, 11, 7, 15, 13)
        faces[8] = (4, 8, 10, 6, 18)
        faces[9] = (14, 5, 19, 18, 4)
        faces[10] = (5, 19, 7, 11, 9)
        faces[11] = (15, 7, 19, 18, 6)
        self.faces, self.vert = faces, vert

    # draws dodecahedron
    def create(self):
        for i in range(12):
            beginShape()
            for j in range(5):
                vertex(self.vert[self.faces[i][j]].x,
                       self.vert[self.faces[i][j]].y,
                       self.vert[self.faces[i][j]].z)
            endShape()