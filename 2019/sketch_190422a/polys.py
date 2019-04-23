

class Poly():
    
    text_on = False
    drag = -1
    drag_hole = -1
    drag_drag_pt = -1
    
    def __init__(self, outer_pts, holes=[[(0, 0)]]):
        self.outer_pts = outer_pts
        self.holes = holes
        
    def plot(self, x_offset, y_offset, cell_size):
        pushStyle()
        if len(self.outer_pts) >= 3:
            fill(255)
            beginShape()
            for x, y in self.outer_pts:
                stroke(0)
                sx = (x + x_offset) * cell_size
                sy = (y + y_offset) * cell_size
                vertex(sx, sy)
            for h in self.holes:
              beginContour()
              for x, y in h:
                sx = (x + x_offset) * cell_size
                sy = (y + y_offset) * cell_size
                vertex(sx, sy)
              endContour()
            endShape(CLOSE)
        Poly.annotate_pts(self.outer_pts, color(200, 0, 0), 5)
        Poly.annotate_pts(self.holes[0], color(0, 0, 200), 5)
        popStyle()
        
        def remove_pt(self, i, j):
            pass

    @classmethod
    def annotate_pts(cls, pts, c, scale_m=1):
        if Poly.text_on:
            strokeWeight(5)
            textSize(16)
            fill(c)
            stroke(c)
            for i, j in pts:
                x, y = (i + x_offset) * cell_size, (j + y_offset) * cell_size
                point(x, y)
                text(str((i * scale_m, j * scale_m)), x, y)
