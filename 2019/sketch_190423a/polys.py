
class Poly():

    text_on = False
    drag = -1
    drag_hole = -1
    drag_drag_pt = -1
    x_offset = y_offset = 0
    cell_size = 10

    def __init__(self, outer_pts, holes=[[(0, 0)]]):
        self.outer_pts = outer_pts
        self.holes = holes

    def plot(self, x_offset, y_offset):
        Poly.x_offset, Poly.y_offset =  x_offset, y_offset
        pushStyle()
        if len(self.outer_pts) >= 3:
            fill(255)
            beginShape()
            for x, y in self.outer_pts:
                stroke(0)
                sx = (x + x_offset) * Poly.cell_size
                sy = (y + y_offset) * Poly.cell_size
                vertex(sx, sy)
            for h in self.holes:
                beginContour()
                for x, y in h:
                    sx = (x + x_offset) * Poly.cell_size
                    sy = (y + y_offset) * Poly.cell_size
                    vertex(sx, sy)
                endContour()
            endShape(CLOSE)
        Poly.annotate_pts(self.outer_pts, color(200, 0, 0), 5)
        Poly.annotate_pts(self.holes[0], color(0, 0, 200), 5)
        popStyle()

    def remove_pt(self, i, j):
        for pt in self.outer_pts:
            if (i, j) == pt:
                self.outer_pts.remove(pt)
                return True
            for h in self.holes:
                for pt in h:
                    if (i, j) == pt:
                        h.remove(pt)
                        return True

    @classmethod
    def annotate_pts(cls, pts, c, scale_m=1):
        if Poly.text_on:
            strokeWeight(5)
            textSize(16)
            fill(c)
            stroke(c)
            for i, j in pts:
                x = (i + cls.x_offset) * cls.cell_size
                y = (j + cls.y_offset) * cls.cell_size
                point(x, y)
                text(str((i * scale_m, j * scale_m)), x, y)

    @classmethod
    def grid(cls, order):
        stroke(128)
        noFill()
        for x in range(order):
            for y in range(order):
                rect(x * cls.cell_size, y * cls.cell_size,
                     cls.cell_size, cls.cell_size)
