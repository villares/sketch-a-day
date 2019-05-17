from random import choice
from polys import poly, poly_arc_augmented


class Ensamble:
    W, H = 700, 700
    SPACING, MARGIN = 150, 150
    rad_list = [60, 40, 20] 
    X_LIST = [x for x in range(MARGIN, 1 + W - MARGIN, SPACING)]
    Y_LIST = [y for y in range(MARGIN, 1 + H - MARGIN, SPACING)]

    def __init__(self):
        self.create_list()
        
    def __eq__(self, other):
        return self.p_list == other.p_list

    def plot(self):
        rad_list = self.rad_list
        noFill()
        strokeWeight(10)
        stroke(200, 0, 0)
        strokeJoin(ROUND)
        poly(self.p_list)
        strokeWeight(4)
        stroke(0, 0, 0)
        for _ in rad_list:
            poly_arc_augmented(self.p_list, rad_list)
            rad_list[:] = [rad_list[-1]] + rad_list[:-1]
            
    def create_list(self):
        self.p_list = []
        for r in self.rad_list:
            new_p = PVector(choice(self.X_LIST),
                            choice(self.Y_LIST))
            while new_p in self.p_list:
                ellipse(new_p.x, new_p.y, 10, 10)
                new_p = PVector(choice(self.X_LIST),
                                choice(self.Y_LIST))
            self.p_list.append(new_p)
