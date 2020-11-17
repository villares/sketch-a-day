
from random import shuffle
from villares.line_geometry import edges_as_sets, line_intersect, Line
from villares.colors import random_hue_saturated

class Cell:

    cells = []

    def __init__(self, pts):
        self.pts = list(pts)
        self.edges = self.recalc_edges()
        self.colour = random_hue_saturated(200)
        
    def recalc_edges(self):
        return edges_as_sets(self.pts, frozen=False)

    def draw(self, debug=False):
        for i, (a, b) in sorted_edges(self.edges, enum=True):
            stroke(self.colour)
            line(a[0], a[1], b[0], b[1])
            if debug:
                mid = Line(a, b).midpoint()
                names = "ABCDEFGHIJKLMNIOPQ"
                text("{}".format(names[i]), mid.x, mid.y)

        for i, p in enumerate(self.pts):
            fill(0)
            textSize(12)
            if debug:
                text("{}".format(i), p[0], p[1])

    def __add__(self, other):
        new_edges = sorted_edges(set(self.edges) ^ set(other.edges))
        pts = []
        for a, b in new_edges:
            pts.append(a)
            pts.append(b)
        new_cell = Cell(set(pts))
        new_cell.edges = new_edges
        return new_cell

    def move_point(self, mx, my, dx, dy):
        for i, (x, y, z) in enumerate(self.pts):
            if dist(x, y, mx, my) < 30:
                self.pts[i].set(x + dx, y + dy)
                return True
        return False

    def edges_intersect(self):
        intersection_pt = None
        for edge in self.edges:
            for other in self.edges:
                if len(edge | other) == 4:
                    pt = line_intersect(tuple(edge), tuple(other))
                    if pt:
                        shuffle(self.pts)
                        self.edges = self.recalc_edges()
                        circle(pt.x, pt.y, 10)
                        intersection_pt = pt
        return intersection_pt
    
    @classmethod
    def draw_cells(cls):
        for cell in cls.cells:
            translate(6, 3)
            cell.draw(debug=(cell==cls.cells[-1]))
            cell.edges_intersect()
    
    @classmethod
    def drag_cells(cls):
        dx, dy = (mouseX - pmouseX), (mouseY - pmouseY)
        # print "dragged {}, {}".format(dx, dy)
        for cell in cls.cells:            
            if cell.move_point(mouseX, mouseY, dx, dy):
                break
    
def sorted_edges(edges_set, enum=False):
    edges = list(edges_set)
    result = [edges.pop()]
    while edges:
        e0 = edges.pop(0)
        if len(e0 | result[-1]) == 3:
            result.append(e0)
        else:
            edges.append(e0)    
    assert len(result) == len(edges_set)
    if enum:
        return enumerate(result)
    else:
        return result
