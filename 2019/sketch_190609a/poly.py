
class Poly():

    selected = -1
    text_on = False
    selected_drag = -1
    drag_hole = -1
    drag_pt = -1
    id = 0

    def __init__(self, pts, holes=None, closed=True, lw=1):
        self.pts = pts
        self.holes = holes if holes else [[]]
        self.closed = closed
        self.lw = lw

    @classmethod
    def setup_grid(cls, cell_size, order, x_offset, y_offset):
        cls.cell_size = cell_size
        cls.order = order
        cls.x_offset, cls.y_offset = x_offset, y_offset
        cls.polys = []
        cls.text_on = False

    def plot(self):
        for i, p in enumerate(self.polys):
            self.id = i if self == p else self.id
        pushStyle()
        strokeJoin(ROUND)
        strokeWeight(self.lw)
        if self.selected_drag == self.id:
            stroke(200, 0, 0)
        else:
            stroke(0)
        if len(self.pts) >= 2:
            if self.closed:
                fill(100)
            else:
                noFill()
            beginShape()
            for x, y in self.pts:
                sx = (x + self.x_offset) * self.cell_size
                sy = (y + self.y_offset) * self.cell_size
                vertex(sx, sy)
            for h in self.holes:
                beginContour()
                for x, y in h:
                    sx = (x + self.x_offset) * self.cell_size
                    sy = (y + self.y_offset) * self.cell_size
                    vertex(sx, sy)
                endContour()
            if self.closed:
                endShape(CLOSE)
            else:
                endShape()
        if self.text_on:
            self.annotate_pts(self.id, self.pts, color(200, 0, 0), 5)
            self.annotate_pts(self.id, self.holes[0], color(0, 0, 200), 5)
        popStyle()

    def remove_pt(self):
        snap = self.mouse_snap()
        if snap:
            for pt in self.pts:
                if pt == snap:
                    self.pts.remove(pt)
                    return True
                for h in self.holes:
                    for pt in h:
                        if pt == snap:
                            h.remove(pt)
                            return True

    def set_drag(self):  # , io, jo):
        snap = Poly.mouse_snap()
        if snap:
            for ipt, pt in enumerate(self.pts):
                if pt == snap:  # (io, jo):
                    Poly.drag_pt = ipt
                    return True
            for ih, h in enumerate(self.holes):
                for ipt, pt in enumerate(h):
                    if pt == snap:  # (io, jo):
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
            text(str(id) + ":" + str((i * scale_m, j * scale_m)), x, y)

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
        for i in range(cls.order):
            x = i * cls.cell_size
            for j in range(cls.order):
                y = j * cls.cell_size
                # grid origin correction
                io, jo = i - cls.x_offset, j - cls.y_offset
                if dist(mouseX, mouseY, x, y) < cls.cell_size / 2:
                    return (io, jo)
        return None

    @classmethod
    def mousePressed(cls):
        if keyPressed and keyCode == CONTROL:
            for p in cls.polys:
                if p.remove_pt():  # io, jo):
                    return
        else:
            for ip, p in enumerate(cls.polys):
                if p.set_drag():  # io, jo):
                    cls.selected_drag = ip
                    return
        cls.selected_drag = -1  # click outside known vertices deselects

    @classmethod
    def mouseDragged(cls):
        if cls.selected_drag >= 0 and not keyPressed:
            # a Poly point has been selected to be dragged
            # and no modifier key is pressed...
            if cls.drag_hole == -1:  # if no hole was selected
                poly = cls.polys[cls.selected_drag]
                poly.pts[cls.drag_pt] = cls.mouse_pos()
            else:
                poly = cls.polys[cls.selected_drag]
                hole = poly.holes[cls.drag_hole]
                hole[cls.drag_pt] = cls.mouse_pos()

        elif cls.selected_drag >= 0 and key == "m":
            poly = cls.polys[cls.selected_drag]
            dragged_pt = poly.pts[cls.drag_pt]
            mx, my = cls.mouse_pos()
            dx, dy = mx - dragged_pt[0], my - dragged_pt[1]
            for i, pt in enumerate(poly.pts):
                poly.pts[i] = (pt[0] + dx, pt[1] + dy)
            for hole in poly.holes:
                for i, pt in enumerate(hole):
                    hole[i] = (pt[0] + dx, pt[1] + dy)
                    
            

    @classmethod
    def mouse_pos(cls):
        return (int(mouseX / cls.cell_size) - cls.x_offset,
                int(mouseY / cls.cell_size) - cls.y_offset)

    @classmethod
    def mouseReleased(cls):
        if cls.selected_drag >= 0 and keyPressed and keyCode == SHIFT:
        # a Poly point has been selected to be dragged
        # and SHIFT key is pressed...
            if cls.drag_hole == -1:  # if no hole wase selected
                poly = cls.polys[cls.selected_drag]
                poly.pts.insert(cls.drag_pt, cls.mouse_pos())
            else:
                poly = cls.polys[cls.selected_drag]
                hole = poly.holes[Poly.drag_hole]
                hole.insert(cls.drag_pt, cls.mouse_pos())
        # Poly.selected_drag = -1  # No poly selected
        Poly.drag_hole = -1  # No hole selected
        Poly.drag_pt = -1  # No point selected
