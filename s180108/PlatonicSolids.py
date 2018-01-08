class Icosahedron():

    def __init__(self, radius):
        topPent = [PVector()] * 5  # PVector[5]
        bottomPent = [PVector()] * 5  # PVector[5]
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