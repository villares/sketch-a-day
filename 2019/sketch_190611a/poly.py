from copy import deepcopy
from arcs import *

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
        cls.mode = 0

    @classmethod
    def grid_to_screen(cls, *args):
        if len(args) == 1:
            x, y = args[0][0], args[0][1]
        else:
            x, y = args
        return ((x + cls.x_offset) * cls.cell_size,
                (y + cls.y_offset) * cls.cell_size)

    @classmethod
    def screen_to_grid(cls, x, y):
        return (int(x / cls.cell_size) - cls.x_offset,
                int(y / cls.cell_size) - cls.y_offset)

    @classmethod
    def draw_grid(cls):
        stroke(128)
        noFill()
        for x in range(cls.order):
            for y in range(cls.order):
                rect(x * cls.cell_size, y * cls.cell_size,
                     cls.cell_size, cls.cell_size)

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
            Poly.draw_pts(self.pts)
            for hole in self.holes:
                beginContour()
                Poly.draw_pts(hole)
                endContour()
            if self.closed:
                endShape(CLOSE)
            else:
                endShape()
        if self.text_on:
            self.annotate_pts(self.id, self.pts, color(200, 0, 0), 5)
            self.annotate_pts(self.id, self.holes[0], color(0, 0, 200), 5)
        popStyle()

    @classmethod
    def draw_pts(cls, pts):
        for i, pt in enumerate(pts):
            if len(pt) == 2:
                print pt
            x, y, corner = pt
            sx, sy = cls.grid_to_screen(x, y)
            if corner == 0:
                vertex(sx, sy)
            elif corner > 0:
                pp = cls.grid_to_screen(pts[i - 1])
                np = cls.grid_to_screen(pts[(i + 1) % len(pts)])
                r = corner * cls.cell_size
                b_roundedCorner((sx, sy), np, pp, r)  # pt[2])
            else:
                if keyPressed:
                    vertex(sx, sy)

    @classmethod
    def annotate_pts(cls, id, pts, c, scale_m=1):
        strokeWeight(5)
        textSize(12)
        fill(c)
        stroke(c)
        for pt in pts:
            i, j = pt[0], pt[1]
            sx, sy = cls.grid_to_screen(i, j)
            point(sx, sy)
            text(str(id) + ":" + str((i * scale_m, j * scale_m)), sx, sy)

    def set_drag(self):  # , io, jo):
        snap = Poly.mouse_snap()
        if snap:
            for ipt, pt in enumerate(self.pts):
                if pt[:2] == snap:  # (io, jo):
                    Poly.drag_pt = ipt
                    return True
            for ih, h in enumerate(self.holes):
                for ipt, pt in enumerate(h):
                    if pt[:2] == snap:  # (io, jo):
                        Poly.drag_hole = ih
                        Poly.drag_pt = ipt
                        return True
        return False

    def remove_pt(self):
        snap = self.mouse_snap()
        if snap:
            for pt in self.pts:
                if pt[:2] == snap:
                    self.pts.remove(pt)
                    return True
                for hole_points in self.holes:
                    for pt in hole_points:
                        if pt[:2] == snap:
                            hole_points.remove(pt)
                            return True

    def change_pt(self, value):
        snap = self.mouse_snap()
        if snap:
            for i, pt in enumerate(self.pts):
                if pt[:2] == snap:
                    self.pts[i] = (pt[0], pt[1], value)
                    return True
                for hole_points in self.holes:
                    for i, pt in enumerate(hole_points):
                        if pt[:2] == snap:
                            hole_points[i] = (pt[0], pt[1], value)
                            return True

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
    def mouse_pressed(cls):
        for ip, p in enumerate(cls.polys):
            if p.set_drag():  # io, jo):
                cls.selected_drag = ip
                return
        cls.selected_drag = -1  # click outside known vertices deselects

    @classmethod
    def mouse_dragged(cls):
        if cls.selected_drag >= 0 and not keyPressed:
            # a Poly point has been selected to be dragged
            # and no modifier key is pressed...
            if cls.drag_hole == -1:  # if no hole was selected
                poly = cls.polys[cls.selected_drag]
                i, j = cls.screen_to_grid(mouseX, mouseY)
                if len(poly.pts[cls.drag_pt]) == 2:
                    print poly.pts[cls.drag_pt]
                poly.pts[cls.drag_pt] = (i, j, poly.pts[cls.drag_pt][2])
            else:
                poly = cls.polys[cls.selected_drag]
                hole = poly.holes[cls.drag_hole]
                i, j = cls.screen_to_grid(mouseX, mouseY)
                hole[cls.drag_pt] = (i, j, hole[cls.drag_pt][2])

        elif cls.selected_drag >= 0 and key == "m":
            poly = cls.polys[cls.selected_drag]
            dragged_pt = poly.pts[cls.drag_pt]
            mx, my = cls.screen_to_grid(mouseX, mouseY)
            dx, dy = mx - dragged_pt[0], my - dragged_pt[1]
            pts = poly.pts
            for i, pt in enumerate(pts):
                pts[i] = (pt[0] + dx, pt[1] + dy, pt[2])
            for hole in poly.holes:
                for i, pt in enumerate(hole):
                    hole[i] = (pt[0] + dx, pt[1] + dy, pt[2])

    @classmethod
    def mouse_released(cls):
        if cls.selected_drag >= 0 and keyPressed and keyCode == SHIFT:
        # a Poly point has been selected to be dragged
        # and SHIFT key is pressed...
            if cls.drag_hole == -1:  # if no hole wase selected
                poly = cls.polys[cls.selected_drag]
                i, j = cls.screen_to_grid(mouseX, mouseY)
                poly.pts.insert(cls.drag_pt, (i, j, 0))
            else:
                poly = cls.polys[cls.selected_drag]
                hole = poly.holes[Poly.drag_hole]
                i, j = cls.screen_to_grid(mouseX, mouseY)
                hole.insert(cls.drag_pt, (i, j, 0))
        elif cls.selected_drag >= 0 and keyPressed and keyCode == CONTROL:
            for p in cls.polys:
                if p.remove_pt():  # io, jo):
                    return
        elif cls.selected_drag >= 0 and keyPressed and key in "-0123456789":
            if key == "-":
                v = -1
            else:
                v = int(key)
            for p in cls.polys:
                if p.change_pt(v):  # io, jo):
                    return

        # Poly.selected_drag = -1  # No poly selected
        Poly.drag_hole = -1  # No hole selected
        Poly.drag_pt = -1  # No point selected

    @classmethod
    def duplicate_selected(cls, offset=1):
        if Poly.selected_drag >= 0:
            new_poly = deepcopy(cls.polys[cls.selected_drag])
            for i, pt in enumerate(new_poly.pts):
                new_poly.pts[i] = (pt[0] + offset, pt[1] + offset, pt[2])
            for h in new_poly.holes:
                for i, pt in enumerate(h):
                    h[i] = (pt[0] + offset, pt[1] + offset, pt[2])
            cls.polys.append(new_poly)

    @staticmethod
    def clockwise_sort(pts):
        if len(pts) < 3:
            return pts
        d = {(x, y): z for x, y, z in pts}
        xy_pairs = [(x, y) for x, y, z in pts]
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
        s = list(zip(xy_sorted_xy[:half_len], xy_sorted_xy[half_len:]))
        s_and_z = [(x, y, d[(x, y)]) for x, y in s]
        print s_and_z
        return s_and_z
