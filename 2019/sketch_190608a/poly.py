
class Poly():

    selected = -1
    text_on = False
    selected_drag = -1
    drag_hole = -1
    drag_pt = -1
    id = 0

    def __init__(self, outer_pts, holes=None, closed=True, lw=1):
        self.outer_pts = outer_pts
        self.holes = holes if holes else [[]]
        self.closed = closed
        self.lw = lw
    
    @classmethod
    def setup_grid(cls, cell_size, order, x_offset, y_offset):
        cls.cell_size = cell_size
        cls.order = order
        cls.x_offset, cls.y_offset = x_offset, y_offset

    def plot(self):
        for i, p in enumerate(Poly.polys):
            self.id = i if self == p else self.id
        pushStyle()
        strokeJoin(ROUND)
        strokeWeight(self.lw)
        if Poly.selected_drag == self.id:
            stroke(200, 0, 0)
        else:
            stroke(0)
        if len(self.outer_pts) >= 2:
            if self.closed:
                fill(100)
            else:
                noFill()
            beginShape()
            for x, y in self.outer_pts:
                sx = (x + Poly.x_offset) * Poly.cell_size
                sy = (y + Poly.y_offset) * Poly.cell_size
                vertex(sx, sy)
            for h in self.holes:
                beginContour()
                for x, y in h:
                    sx = (x + Poly.x_offset) * Poly.cell_size
                    sy = (y + Poly.y_offset) * Poly.cell_size
                    vertex(sx, sy)
                endContour()
            if self.closed:
                endShape(CLOSE)
            else:
                endShape()
        if Poly.text_on:    
            Poly.annotate_pts(self.id, self.outer_pts, color(200, 0, 0), 5)
            Poly.annotate_pts(self.id, self.holes[0], color(0, 0, 200), 5)
        popStyle()

    def remove_pt(self):
        snap = Poly.mouse_snap()
        if snap:
          for pt in self.outer_pts:
            if pt == snap:
                self.outer_pts.remove(pt)
                return True
            for h in self.holes:
                for pt in h:
                    if pt == snap:
                        h.remove(pt)
                        return True

    def set_drag(self): #, io, jo):
        snap = Poly.mouse_snap()
        if snap:
            for ipt, pt in enumerate(self.outer_pts):
                if pt == snap: #(io, jo):
                    Poly.drag_pt = ipt
                    return True
            for ih, h in enumerate(self.holes):
                for ipt, pt in enumerate(h):
                    if pt == snap: #(io, jo):
                        Poly.drag_hole = ih
                        Poly.drag_pt = ipt
                        return True
        return False
    
    @classmethod
    def annotate_pts(cls, id, pts, c, scale_m=1):
            strokeWeight(5)
            textSize(12)
            fill(c)
            stroke(c)
            for i, j in pts:
                x = (i + cls.x_offset) * cls.cell_size
                y = (j + cls.y_offset) * cls.cell_size
                point(x, y)
                text(str(id)+":"+str((i * scale_m, j * scale_m)), x, y)

    @classmethod
    def draw_grid(cls):
        stroke(128)
        noFill()
        for x in range(cls.order):
            for y in range(cls.order):
                rect(x * cls.cell_size, y * cls.cell_size,
                     cls.cell_size, cls.cell_size)

    @staticmethod
    def clockwise_sort(xy_pairs):
        # https://stackoverflow.com/questions/51074984/sorting-according-to-clockwise-point-coordinates
        data_len = len(xy_pairs)
        if data_len > 2:
            x, y = zip(*xy_pairs)
        else:
            return xy_pairs
        centroid_x, centroid_y = sum(x) / data_len, sum(y) / data_len
        xy_sorted = sorted(xy_pairs,
                           key=lambda p: atan2((p[1] - centroid_y), (p[0] - centroid_x)))
        xy_sorted_xy = [
            coord for pair in list(zip(*xy_sorted)) for coord in pair]
        half_len = int(len(xy_sorted_xy) / 2)
        return list(zip(xy_sorted_xy[:half_len], xy_sorted_xy[half_len:]))
    
    @classmethod
    def mouse_snap(cls):
        for i in range(Poly.order):
            x = i * Poly.cell_size
            for j in range(Poly.order):
                y = j * Poly.cell_size
                io, jo = i - Poly.x_offset, j - Poly.y_offset  # grid origin correction
                if dist(mouseX, mouseY, x, y) < Poly.cell_size / 2:
                    return (io, jo)
        return None
                
    
